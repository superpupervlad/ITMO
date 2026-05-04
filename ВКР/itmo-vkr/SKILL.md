---
name: itmo-vkr
description: Author or edit an ITMO graduation thesis (ВКР) in Markdown and convert it to a DOCX/PDF compliant with ЛНАОБУЧ-СМК-05-05-2020 (ГОСТ 7.32-2017). Trigger on any Russian-language request mentioning ВКР, ИТМО, ITMO, дипломная работа, бакалаврская работа, выпускная квалификационная работа, магистерская диссертация, ГОСТ 7.32, or "оформление по требованиям ИТМО". Also trigger when the user asks to write/edit a chapter, introduction, conclusion, or section of a Russian academic thesis — they will want it formatted so it converts cleanly. Use whenever the user wants to convert their Russian thesis Markdown into Word/PDF, or asks for help with VKR formatting (figures, tables, formulas, source list, structural elements). Apply this skill in addition to (not instead of) substantive guidance about the thesis content.
---

# ITMO ВКР — Markdown → DOCX/PDF

This skill has two jobs:

1. **Help the user author the thesis itself in Markdown** — drafting introductions, chapters, conclusions, source-list entries, and so on, in prose that conforms to ЛНАОБУЧ-СМК-05-05-2020 / ГОСТ 7.32-2017. That means engaging with the substance of the work *and* applying the standard's heading conventions, prose-style rules, and references format as you write.
2. **Convert the finished Markdown into DOCX/PDF** that satisfies ITMO's submission requirements, using the bundled `convert.sh` pipeline.

All form-style requirements — Times New Roman 14 pt, A4, 1.5 line spacing, justified text, 30/15/20/20 mm margins, paragraph indent 1.25 cm, ALL-CAPS centred structural-element headings on new pages, bordered tables, centred figures with captions below, formulas with right-aligned numbers, source list per ГОСТ Р 7.0.5-2008 — are encoded in the bundled `reference.docx` style template, so when authoring you only need to keep the Markdown structure right and the styling falls out automatically on conversion.

## Host dependencies

Before the skill works, the machine needs:

- `pandoc` ≥ 3 — required for any conversion
- `python3` ≥ 3.10 — to build `reference.docx` via `python-docx`
- `libreoffice` (a.k.a. `soffice`) — only required for `--update-toc` / `--pdf-libre`; plain DOCX conversion runs without it

If the user is on a fresh checkout and `scripts/reference.docx` is missing, run **`scripts/setup.sh`** once. It creates a `scripts/venv/`, installs `python-docx` into it, and regenerates `reference.docx`. The venv is intentionally not committed — it's not portable across machines.

## Bundled tooling

The skill ships with everything required for conversion under `scripts/`:

- `scripts/setup.sh` — one-time setup that builds the Python venv and `reference.docx`
- `scripts/convert.sh` — pandoc wrapper that produces DOCX (and optionally PDF / populated TOC)
- `scripts/build_reference.py` — regenerates `reference.docx`; called by `setup.sh`
- `scripts/update_toc.py` — UNO bridge helper used by `--update-toc`
- `scripts/reference.docx` — pre-built style template (committed; rebuild via `setup.sh` if missing)
- `assets/template.md` — minimal starter document showing every supported element
- `references/требования_вкр.pdf` — full text of the standard

The `convert.sh` script is path-independent: invoke it with absolute paths to the input and output and it Does The Right Thing.

## Conversion workflow

**Always pass absolute paths** so the script's internal `cd` to its own directory doesn't break input/output resolution. Resolve `<skill-dir>` to the directory containing this `SKILL.md` (do not hard-code an absolute path — it varies per user / per project).

```bash
# Plain DOCX
<skill-dir>/scripts/convert.sh /abs/path/thesis.md /abs/path/thesis.docx

# DOCX with the table of contents auto-populated
# (pandoc inserts a TOC field; without --update-toc Word/LO fills it on first open + F9)
<skill-dir>/scripts/convert.sh --update-toc /abs/path/thesis.md

# DOCX + PDF, both with populated TOC
<skill-dir>/scripts/convert.sh --update-toc --pdf-libre /abs/path/thesis.md
```

Each LibreOffice flag adds ~10–30 s to the run; the script prints a "this takes 10–30 seconds…" notice when those phases start.

If the user already has a working `vkr_template/` in their project root with the same scripts, prefer that copy — it's likely been tweaked and rebuilt with project-specific styling.

## Markdown structure

The reference doc maps Markdown heading levels to ITMO's heading hierarchy. Use the right level — getting this wrong is by far the most common cause of broken output.

| Markdown | Renders as | When to use |
|---|---|---|
| `# Введение` | Heading 1: centred, **ALL CAPS**, bold, page break before, no number | Structural elements: ВВЕДЕНИЕ, ЗАКЛЮЧЕНИЕ, СОДЕРЖАНИЕ, СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ, ПРИЛОЖЕНИЕ А, СПИСОК СОКРАЩЕНИЙ И УСЛОВНЫХ ОБОЗНАЧЕНИЙ, ТЕРМИНЫ И ОПРЕДЕЛЕНИЯ |
| `## 1 Анализ` | Heading 2: bold, indented, page break before | Numbered chapters of the основная часть |
| `### 1.1 Постановка задачи` | Heading 3: bold, indented, **no** page break | Subsections inside a chapter |
| `#### 1.1.1 Подпункт` | Heading 4 | Sub-subsections (rarely needed) |

Source the heading text in plain mixed-case Russian — capitalisation is applied by the docx style, so you write `# Введение` and the rendered output is `ВВЕДЕНИЕ`.

### Critical rules from §4.4 of the standard

These are easy to violate accidentally and the document will not pass review:

- **No period after a section number.** `## 1 Анализ`, never `## 1. Анализ`. Same for `### 1.1`, `#### 1.1.1`.
- **Structural elements are not numbered.** `# Введение`, never `# 1 Введение` or `## Введение`.
- **No abbreviations or hyphenation in headings.** Spell out acronyms on first use in body text instead.
- **One canonical structural-element name.** Don't paraphrase — use the exact wording from the spec (ВВЕДЕНИЕ / ЗАКЛЮЧЕНИЕ / СОДЕРЖАНИЕ / СПИСОК ИСПОЛЬЗОВАННЫХ ИСТОЧНИКОВ).
- **Reference figures, tables, and formulas in text *before* they appear.** "На рисунке 1 показано…", "В таблице 2 приведены…", "по формуле (1)".

### Document structure

A complete VKR follows this order:

1. Титульный лист — official form, inserted into the DOCX manually
2. Задание — official form, inserted manually
3. Аннотация — official form, inserted manually
4. `# Содержание` — auto-populated when you pass `--update-toc` (otherwise the TOC field stays empty until first open in Word/LO)
5. `# Введение`
6. `## 1 …`, `## 2 …`, … — chapters of the основная часть
7. `# Заключение`
8. `# Список использованных источников`
9. `# Приложение А`, `# Приложение Б`, … — optional appendices

The first three are blank forms you cannot generate from Markdown — tell the user to insert them into the produced DOCX manually if they're building a final thesis (vs. a draft).

### Figures

```markdown
На рисунке 1 представлена схема системы.

![Рисунок 1 – Схема системы](path/to/diagram.png){width=60%}
```

The Markdown alt text becomes the figure's caption. The reference doc styles it centred, below the image, no period at end. Use `{width=60%}` (or another percentage) to control size — full-width images often look too large with A4 margins. The image path is resolved relative to the Markdown file's directory.

### Tables

```markdown
В таблице 1 приведены характеристики алгоритма.

| Параметр              | Значение | Единицы |
|-----------------------|----------|---------|
| Сложность по времени  | O(n²)    | —       |
| Точность              | 0,97     | —       |

: Таблица 1 – Характеристики алгоритма
```

Two specifics:

- The line beginning with `:` is the caption — pandoc renders it left-aligned above the table (per §4.6.3) with no paragraph indent.
- Pandoc emits the table with a `Table` style which the reference doc defines with single 0.5 pt borders on every side, including inside borders.
- Cells use the `Compact` style (left-aligned, no first-line indent) — short values won't be pushed right by the body's 1.25 cm indent.

### Formulas

Display formulas (numbered, on their own line):

```markdown
Среднеквадратичная ошибка вычисляется по формуле (1):

$$\mathrm{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \quad (1)$$

где $n$ — число наблюдений, $y_i$ — истинное значение,
$\hat{y}_i$ — предсказанное значение.
```

Place the formula number at the right of the line as `\quad (N)` — pandoc renders display math centred, and the `\quad` provides enough whitespace that the number reads as right-aligned. Reference the formula in text as "по формуле (1)".

Inline math: `$E = mc^2$`, `$\sigma$`, etc. Don't number inline math.

### Lists

Bulleted (use hyphens), each item ending with a comma except the last:

```markdown
Информационно-сервисная служба включает следующие модули:

- удалённый заказ,
- виртуальная справочная служба,
- виртуальный читальный зал.
```

Numbered:

```markdown
Этапы работы по оцифровке:

1. первичный осмотр и структурирование исходных материалов,
2. сканирование документов,
3. обработка и проверка полученных образов.
```

For nested lists indent four spaces.

### Code listings

Per §4.11.1, listings normally belong in приложения, not in the main flow. Inline short snippets are tolerable; long programmes belong at the back:

```markdown
# Приложение А

Listing А.1 – Основной алгоритм.

` ` `python
def example():
    ...
` ` `
```

The reference doc renders code blocks left-aligned (no justification) so listings keep their original whitespace. The font is still Times New Roman per the spec — that's by design even though it looks unusual for code.

### References / source list

In body text, cite as `[1]`, `[2, 3]`. The source list itself:

```markdown
# Список использованных источников

1. Иванов И.И. Заголовок работы // Журнал. – 2020. – N 1. – С. 1–10.
2. ГОСТ 7.32-2017 СИБИД. Отчет о научно-исследовательской работе. Структура и правила оформления. – М.: Стандартинформ, 2017. – 32 с.
```

Format individual entries per ГОСТ Р 7.0.5-2008: author(s), title, source, year, issue, pages. Strip hyperlinks from URLs (per the spec footnote in §4.10).

### Inline emphasis

`**bold**` for emphasis, `*italic*` for object names and terms, `` `monospace` `` for filenames/commands/variables. Don't underline.

## Authoring the thesis

When the user asks for help writing the work itself — drafting an introduction, expanding an outline into prose, summarising research for a chapter, writing the conclusion, formatting a source-list entry — engage with the substance directly. Produce real content, not placeholder text, and apply the standard's structural and prose-style requirements while you do so. A few specific patterns:

**Введение** (per §3.5) covers, in order: актуальность темы исследования, степень её разработанности, решаемая проблема, цель и задачи, практическая значимость. For a master's thesis (магистерская диссертация) also include научная новизна, методы исследования, методологическая и теоретическая основы, положения, выносимые на защиту, и степень достоверности и апробация результатов. When asked to write an introduction, structure it around these elements — call them out explicitly or weave them into prose, but cover all of them.

**Основная часть** chapters should each map to one of the goals stated in the introduction. When proposing chapter structures, derive the chapters from the задачи you wrote in введение rather than inventing fresh divisions. Each chapter typically pairs theoretical analysis with practical work — for an НИР-style thesis, theory tends to dominate; for a практико-ориентированный thesis, the implementation does.

**Заключение** (per §3.7) summarises results, draws conclusions, gives recommendations, and outlines further research directions. It should answer the задачи from введение one by one and avoid introducing new claims.

**Source-list entries** follow ГОСТ Р 7.0.5-2008. Common patterns:

- Article: `Иванов И.И. Заголовок статьи // Название журнала. – 2020. – Т. 5, N 3. – С. 12–25.`
- Book: `Петров П.П. Заголовок книги: учебник для вузов. – М.: Издательство, 2018. – 432 с.`
- Conference paper: `Сидоров С.С. Заголовок доклада // Материалы конференции. – СПб.: Изд., 2021. – С. 45–52.`
- Web resource: `Заголовок ресурса. – URL: https://example.com/page (дата обращения: 04.05.2026).` — strip the active hyperlink, leave plain text.
- Standard: `ГОСТ 7.32-2017 СИБИД. Отчет о научно-исследовательской работе. Структура и правила оформления. – М.: Стандартинформ, 2017. – 32 с.`

When you draft body text that cites a source, also add the corresponding entry to `# Список использованных источников` and number `[N]` references in body text in **order of first appearance** (per §4.10.3) — re-number all subsequent citations if you insert a new one in the middle.

**Captions** are part of the prose: figure captions ("Рисунок N – Schema системы") and table titles ("Таблица N – Сравнение методов") need to be written, not just referenced. When you propose a figure or table for an argument, draft the caption in the same step.

**Don't insert placeholder text** like "[здесь добавить описание]" or "TODO". If you don't have the information to draft a section, say so in the conversation and ask — don't leave gaps in the document.

## Style of writing (§3.9)

The standard explicitly forbids in the body text:

- разговорная речь, техницизмы, профессионализмы
- multiple synonyms for the same concept (pick one term, use it consistently throughout)
- foreign words when a Russian equivalent exists
- arbitrary or invented word formations
- abbreviations not authorised by the orthography
- abbreviated unit names appearing without numbers (write "несколько секунд", not "несколько с")

Apply these when authoring or editing prose. Be especially watchful when translating or adapting English-language source material — terms like "implement"/"deploy"/"workflow" often have established Russian equivalents.

## Boundaries

A few things genuinely sit outside what this skill can produce, even when authoring the work in full:

- **Титульный лист, задание, and аннотация are official ITMO blank forms.** They aren't generated from Markdown — when the user is preparing a final submission, remind them to fill in the official forms and insert the resulting pages into the produced DOCX before turning it in. For drafts in progress, ignore them.
- **The populated table of contents requires LibreOffice.** Without `--update-toc`, the `СОДЕРЖАНИЕ` heading appears but the entries underneath stay empty until Word or LibreOffice opens the file and processes the field on F9.
- **Page-count targets are the user's call, not a hard checkpoint.** Recommended ranges: 40–50 страниц для бакалавра, 50–75 для специалиста, 60–80 для магистра, без учёта приложений. Mention the target if the draft is far below it; don't pad to hit the number.

## Reference material

The full text of the standard (in Russian) is bundled at `references/требования_вкр.pdf` (resolve relative to this skill's directory) if you need to look up specific paragraph numbers. The detailed style implementation is in `scripts/build_reference.py` — the most reliable way to answer "is this exact formatting allowed?" is to read both that file and the relevant section of the PDF.
