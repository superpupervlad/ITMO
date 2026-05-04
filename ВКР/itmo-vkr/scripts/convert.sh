#!/usr/bin/env bash
# Convert markdown VKR source to a DOCX styled per ITMO ЛНАОБУЧ-СМК-05-05-2020.
#
# Usage:
#   ./convert.sh [--update-toc] [--pdf-libre] input.md [output.docx]
#
# Flags:
#   --update-toc, -u   After conversion, run LibreOffice headless to populate
#                      the TOC field (pandoc leaves it un-rendered by default).
#   --pdf-libre        Also export a PDF alongside the DOCX, via LibreOffice.
#                      Combine with --update-toc to get a populated TOC in
#                      the PDF. Output: same name as DOCX, .pdf extension.
#
# Requires: pandoc. The LO flags additionally need `soffice` / `libreoffice`.
# Uses reference.docx (run `python build_reference.py` once to generate it).

set -euo pipefail

cd "$(dirname "$0")"

UPDATE_TOC=0
PDF_LIBRE=0
while [[ $# -gt 0 ]]; do
    case "$1" in
        --update-toc|-u) UPDATE_TOC=1; shift ;;
        --pdf-libre)     PDF_LIBRE=1;  shift ;;
        --) shift; break ;;
        -*) echo "Unknown option: $1" >&2; exit 2 ;;
        *) break ;;
    esac
done

INPUT="${1:-vkr.md}"
OUTPUT="${2:-${INPUT%.md}.docx}"

if [[ ! -f reference.docx ]]; then
    echo "reference.docx is missing — generating it..."
    if [[ -d venv ]]; then
        # shellcheck disable=SC1091
        source venv/bin/activate
    fi
    python build_reference.py
fi

pandoc "$INPUT" \
    --from=markdown+pipe_tables+grid_tables+raw_tex \
    --to=docx \
    --reference-doc=reference.docx \
    --output="$OUTPUT" \
    --top-level-division=chapter \
    --toc \
    --toc-depth=3 \
    --metadata=toc-title:"СОДЕРЖАНИЕ"

echo "Wrote $OUTPUT"

if [[ "$UPDATE_TOC" == "1" ]]; then
    SOFFICE=""
    for cand in soffice libreoffice; do
        if command -v "$cand" >/dev/null 2>&1; then
            SOFFICE="$cand"
            break
        fi
    done
    if [[ -z "$SOFFICE" ]]; then
        echo "--update-toc requested but neither soffice nor libreoffice found on PATH" >&2
        exit 1
    fi

    # Find LibreOffice's program/ dir so we can import the bundled `uno`
    # module from system Python.
    LO_PROG="$(dirname "$(realpath "$(command -v "$SOFFICE")")")"
    if [[ ! -f "$LO_PROG/uno.py" ]]; then
        echo "Could not locate LibreOffice's uno.py (looked in $LO_PROG)" >&2
        exit 1
    fi

    tmp_profile=$(mktemp -d)
    UNO_PORT=2202

    cleanup_lo() {
        # kill -9 because SIGTERM can leave soffice spinning on shutdown.
        # Don't `wait` — waiting on a backgrounded daemon hangs the shell.
        pkill -9 -f "port=$UNO_PORT;urp" 2>/dev/null || true
        rm -rf "$tmp_profile"
        # If we crashed mid-update, LibreOffice may have left a lock file
        # next to the output that blocks the *next* run from loading it.
        rm -f "$(dirname "$OUTPUT")/.~lock.$(basename "$OUTPUT")#"
    }
    trap cleanup_lo EXIT

    # A leftover lock from a previous crashed run silently makes
    # loadComponentFromURL return None, so wipe it before we start.
    rm -f "$(dirname "$OUTPUT")/.~lock.$(basename "$OUTPUT")#"

    echo "Updating TOC via LibreOffice headless — this takes 10-30 seconds..."

    "$SOFFICE" --headless --norestore --nologo --nofirststartwizard \
        --accept="socket,host=localhost,port=$UNO_PORT;urp;StarOffice.ServiceManager" \
        "-env:UserInstallation=file://$tmp_profile" \
        >/dev/null 2>&1 &
    LO_PID=$!
    disown "$LO_PID" 2>/dev/null || true

    abs_output="$(realpath "$OUTPUT")"
    PYTHONPATH="$LO_PROG" \
        URE_BOOTSTRAP="vnd.sun.star.pathname:$LO_PROG/fundamentalrc" \
        LD_LIBRARY_PATH="$LO_PROG${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" \
        python3 "$(dirname "$0")/update_toc.py" "$abs_output" "$UNO_PORT"

    echo "Updated TOC in $OUTPUT (via $SOFFICE)"
fi

if [[ "$PDF_LIBRE" == "1" ]]; then
    SOFFICE="${SOFFICE:-}"
    if [[ -z "$SOFFICE" ]]; then
        for cand in soffice libreoffice; do
            if command -v "$cand" >/dev/null 2>&1; then
                SOFFICE="$cand"
                break
            fi
        done
    fi
    if [[ -z "$SOFFICE" ]]; then
        echo "--pdf-libre requested but neither soffice nor libreoffice found on PATH" >&2
        exit 1
    fi

    echo "Exporting PDF via LibreOffice headless — this takes 10-30 seconds..."

    pdf_profile=$(mktemp -d)
    pdf_outdir="$(dirname "$(realpath "$OUTPUT")")"
    # Strip any stale lock so the .docx is loadable.
    rm -f "$pdf_outdir/.~lock.$(basename "$OUTPUT")#"
    "$SOFFICE" --headless --norestore --nologo --nofirststartwizard \
        "-env:UserInstallation=file://$pdf_profile" \
        --convert-to pdf --outdir "$pdf_outdir" "$OUTPUT" >/dev/null 2>&1
    rm -rf "$pdf_profile"

    pdf_path="${OUTPUT%.docx}.pdf"
    if [[ -f "$pdf_path" ]]; then
        echo "Wrote $pdf_path"
    else
        echo "PDF export failed (expected $pdf_path)" >&2
        exit 1
    fi
fi
