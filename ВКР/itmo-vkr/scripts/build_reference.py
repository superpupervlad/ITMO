"""Build a pandoc reference.docx that enforces ITMO VKR formatting.

Usage:
    python build_reference.py

Produces: reference.docx — pass to pandoc via `--reference-doc=reference.docx`.

Style rules implemented (from ЛНАОБУЧ-СМК-05-05-2020, section 4):
- A4, margins L30/R15/T20/B20 mm
- Times New Roman 14 pt, black, 1.5 line spacing, justified
- First-line indent 1.25 cm in body text
- Page numbers: bottom center, Arabic
- Heading 1 = structural element (ВВЕДЕНИЕ, ЗАКЛЮЧЕНИЕ, ...): centered, ALL CAPS,
  bold, page break before
- Heading 2 = numbered section: bold, indent, capitalized
- Heading 3 = numbered subsection: bold, indent
- Captions: figures centered below, tables left above
- Source list / bibliography: numbered, indented
"""

from docx import Document
from docx.shared import Pt, Cm, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


FONT_NAME = "Times New Roman"
FONT_SIZE = Pt(14)
LINE_SPACING = 1.5
INDENT = Cm(1.25)


def set_run_font(run, *, bold=False, italic=False, caps=False, size=FONT_SIZE):
    run.font.name = FONT_NAME
    run.font.size = size
    run.font.color.rgb = RGBColor(0, 0, 0)
    run.bold = bold
    run.italic = italic
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), FONT_NAME)
    if caps:
        caps_el = OxmlElement("w:caps")
        caps_el.set(qn("w:val"), "1")
        rPr.append(caps_el)


def set_paragraph_format(
    para,
    *,
    alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
    first_line_indent=INDENT,
    space_before=Pt(0),
    space_after=Pt(0),
    line_spacing=LINE_SPACING,
    keep_with_next=False,
    page_break_before=False,
):
    pf = para.paragraph_format
    pf.alignment = alignment
    pf.first_line_indent = first_line_indent
    pf.space_before = space_before
    pf.space_after = space_after
    pf.line_spacing = line_spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.keep_with_next = keep_with_next
    pf.page_break_before = page_break_before


def configure_style(
    style,
    *,
    bold=False,
    italic=False,
    caps=False,
    alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
    first_line_indent=INDENT,
    space_before=Pt(0),
    space_after=Pt(0),
    line_spacing=LINE_SPACING,
    keep_with_next=False,
    page_break_before=False,
    size=FONT_SIZE,
):
    font = style.font
    font.name = FONT_NAME
    font.size = size
    font.bold = bold
    font.italic = italic
    font.color.rgb = RGBColor(0, 0, 0)

    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    # Word prefers asciiTheme/hAnsiTheme over explicit ascii/hAnsi when both
    # are present, which in heading styles falls back to Calibri Light. Drop
    # the theme attributes so the explicit Times New Roman wins.
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rFonts.get(qn(attr)) is not None:
            del rFonts.attrib[qn(attr)]
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(attr), FONT_NAME)
    if caps:
        for existing in rPr.findall(qn("w:caps")):
            rPr.remove(existing)
        caps_el = OxmlElement("w:caps")
        caps_el.set(qn("w:val"), "1")
        rPr.append(caps_el)

    pf = style.paragraph_format
    pf.alignment = alignment
    pf.first_line_indent = first_line_indent
    pf.space_before = space_before
    pf.space_after = space_after
    pf.line_spacing = line_spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.keep_with_next = keep_with_next
    pf.page_break_before = page_break_before


def add_table_style_with_borders(doc, style_id):
    """Create or replace a table style with full single-line borders.

    python-docx's high-level API can't set <w:tblBorders>, so we inject the
    XML directly. Borders are 4 eighths of a point (= 0.5 pt), colour 'auto'.
    """
    styles_element = doc.styles.element
    # Drop any existing style with the same id so we don't get duplicates.
    for existing in styles_element.findall(qn("w:style")):
        if existing.get(qn("w:styleId")) == style_id:
            styles_element.remove(existing)

    style_xml = f'''<w:style xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" w:styleId="{style_id}" w:type="table">
        <w:name w:val="{style_id}"/>
        <w:basedOn w:val="TableNormal"/>
        <w:uiPriority w:val="59"/>
        <w:pPr>
            <w:spacing w:after="0" w:line="276" w:lineRule="auto"/>
            <w:ind w:firstLine="0"/>
        </w:pPr>
        <w:rPr>
            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman"/>
            <w:sz w:val="28"/>
        </w:rPr>
        <w:tblPr>
            <w:tblBorders>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>
                <w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>
                <w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/>
            </w:tblBorders>
        </w:tblPr>
    </w:style>'''
    from docx.oxml import parse_xml
    styles_element.append(parse_xml(style_xml))


def add_page_number(paragraph):
    """Insert a PAGE field at center bottom of footer."""
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    set_run_font(run)

    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = "PAGE \\* MERGEFORMAT"
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")

    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)


def main():
    doc = Document()

    # Page setup
    section = doc.sections[0]
    section.page_height = Mm(297)
    section.page_width = Mm(210)
    section.left_margin = Mm(30)
    section.right_margin = Mm(15)
    section.top_margin = Mm(20)
    section.bottom_margin = Mm(20)

    # Default 'Normal' style — body text
    normal = doc.styles["Normal"]
    configure_style(
        normal,
        alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
        first_line_indent=INDENT,
    )

    # Heading 1 — structural element (ВВЕДЕНИЕ, ЗАКЛЮЧЕНИЕ, ...)
    h1 = doc.styles["Heading 1"]
    configure_style(
        h1,
        bold=True,
        caps=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        first_line_indent=Cm(0),
        space_before=Pt(0),
        space_after=Pt(18),
        keep_with_next=True,
        page_break_before=True,
    )

    # Heading 2 — numbered chapter ("1 Название раздела")
    # Per 4.4.2 each chapter starts on a new page (same as structural elements).
    h2 = doc.styles["Heading 2"]
    configure_style(
        h2,
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.LEFT,
        first_line_indent=INDENT,
        space_before=Pt(0),
        space_after=Pt(12),
        keep_with_next=True,
        page_break_before=True,
    )

    # Heading 3 — subsection ("1.1 Название подраздела")
    h3 = doc.styles["Heading 3"]
    configure_style(
        h3,
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.LEFT,
        first_line_indent=INDENT,
        space_before=Pt(0),
        space_after=Pt(6),
        keep_with_next=True,
    )

    # Heading 4 — sub-subsection
    h4 = doc.styles["Heading 4"]
    configure_style(
        h4,
        bold=True,
        alignment=WD_ALIGN_PARAGRAPH.LEFT,
        first_line_indent=INDENT,
        space_before=Pt(0),
        space_after=Pt(6),
        keep_with_next=True,
    )

    # Title (used by pandoc for document title — we keep it bold centered, big)
    if "Title" in doc.styles:
        title = doc.styles["Title"]
        configure_style(
            title,
            bold=True,
            caps=True,
            alignment=WD_ALIGN_PARAGRAPH.CENTER,
            first_line_indent=Cm(0),
            space_before=Pt(0),
            space_after=Pt(24),
            size=Pt(14),
        )

    # TOC Heading — pandoc applies this to the TOC title ("СОДЕРЖАНИЕ").
    # Per 4.4.1 it's a structural element: centered, ALL CAPS, bold, no period.
    from docx.enum.style import WD_STYLE_TYPE
    toc_heading_name = "TOC Heading"
    if toc_heading_name in doc.styles:
        toc_h = doc.styles[toc_heading_name]
    else:
        toc_h = doc.styles.add_style(toc_heading_name, WD_STYLE_TYPE.PARAGRAPH)
    configure_style(
        toc_h,
        bold=True,
        caps=True,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        first_line_indent=Cm(0),
        space_before=Pt(0),
        space_after=Pt(18),
        keep_with_next=True,
        page_break_before=True,
    )

    # TOC entry styles — Normal-like, no first-line indent, dotted leader is added by Word
    for tname in ("TOC 1", "TOC 2", "TOC 3"):
        if tname in doc.styles:
            t = doc.styles[tname]
        else:
            t = doc.styles.add_style(tname, WD_STYLE_TYPE.PARAGRAPH)
        configure_style(
            t,
            alignment=WD_ALIGN_PARAGRAPH.LEFT,
            first_line_indent=Cm(0),
            space_before=Pt(0),
            space_after=Pt(0),
        )

    # Caption — figure/table caption (pandoc uses 'Image Caption' / 'Table Caption')
    for cap_name, alignment in (
        ("Caption", WD_ALIGN_PARAGRAPH.CENTER),
        ("Image Caption", WD_ALIGN_PARAGRAPH.CENTER),
        ("Table Caption", WD_ALIGN_PARAGRAPH.LEFT),
    ):
        if cap_name in doc.styles:
            cap = doc.styles[cap_name]
        else:
            cap = doc.styles.add_style(cap_name, WD_STYLE_TYPE.PARAGRAPH)
        configure_style(
            cap,
            bold=False,
            italic=False,
            alignment=alignment,
            first_line_indent=Cm(0),
            space_before=Pt(6),
            space_after=Pt(6),
        )

    # List paragraphs
    if "List Paragraph" in doc.styles:
        lp = doc.styles["List Paragraph"]
        configure_style(
            lp,
            alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
            first_line_indent=INDENT,
        )

    # Source code (pandoc 'Source Code') and verbatim — left-aligned, no
    # justification, no first-line indent so listings keep their original
    # whitespace.
    source_code_name = "Source Code"
    if source_code_name in doc.styles:
        sc = doc.styles[source_code_name]
    else:
        sc = doc.styles.add_style(source_code_name, WD_STYLE_TYPE.PARAGRAPH)
    configure_style(
        sc,
        alignment=WD_ALIGN_PARAGRAPH.LEFT,
        first_line_indent=Cm(0),
    )

    # 'Compact' is pandoc's style for tight-list items and table cells. It
    # inherits Normal by default, which gives table cells a 1.25 cm
    # first-line indent and justified alignment — wrong for both lists and
    # cells. Force left-aligned, no first-line indent.
    compact_name = "Compact"
    if compact_name in doc.styles:
        cp = doc.styles[compact_name]
    else:
        cp = doc.styles.add_style(compact_name, WD_STYLE_TYPE.PARAGRAPH)
    configure_style(
        cp,
        alignment=WD_ALIGN_PARAGRAPH.LEFT,
        first_line_indent=Cm(0),
    )

    # Pandoc wraps each image in a paragraph styled 'Captioned Figure' (and
    # older versions use 'Figure'). Centre them so images sit in the middle
    # of the page rather than inheriting the justified body alignment.
    for fig_name in ("Captioned Figure", "Figure"):
        if fig_name in doc.styles:
            fs = doc.styles[fig_name]
        else:
            fs = doc.styles.add_style(fig_name, WD_STYLE_TYPE.PARAGRAPH)
        configure_style(
            fs,
            alignment=WD_ALIGN_PARAGRAPH.CENTER,
            first_line_indent=Cm(0),
            space_before=Pt(6),
            space_after=Pt(6),
        )

    # Table style — pandoc tags every table with <w:tblStyle w:val="Table"/>
    # but doesn't define the style itself, so without intervention tables
    # render borderless. Define 'Table' with single 0.5 pt borders all around.
    add_table_style_with_borders(doc, "Table")

    # Quote
    if "Quote" in doc.styles:
        q = doc.styles["Quote"]
        configure_style(
            q,
            italic=True,
            alignment=WD_ALIGN_PARAGRAPH.JUSTIFY,
            first_line_indent=INDENT,
        )

    # Footer with page number
    footer_para = section.footer.paragraphs[0]
    add_page_number(footer_para)

    # Sample placeholder paragraph so pandoc has a body to mimic
    p = doc.add_paragraph("Образец основного текста.")
    set_paragraph_format(p)
    for run in p.runs:
        set_run_font(run)

    out = "reference.docx"
    doc.save(out)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
