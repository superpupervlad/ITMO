#!/usr/bin/env bash
# One-time setup: build a venv with python-docx and generate reference.docx.
# Idempotent — safe to re-run.

set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -d venv ]]; then
    python3 -m venv venv
fi
./venv/bin/pip install --quiet python-docx
./venv/bin/python build_reference.py
