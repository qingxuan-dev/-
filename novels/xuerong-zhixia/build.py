# -*- coding: utf-8 -*-
"""Build the reader page, EPUB and Word versions of 雪融之夏 from the original markdown.

Usage: python3 build.py
The original text is never modified. The only typographic change is turning straight
quotes into Chinese curly quotes (“” and ‘’), pairing them within each line.
Add new chapters as a new file named xuerong-zhixia-chN.original.md (N = first chapter number in it) and re-run.

English: en/ch1.md, en/ch2.md, ... hold a paragraph-for-paragraph translation (same chapters,
sections and paragraph count as the original). The build checks the alignment and stops on a mismatch.
A Chinese chapter without an English file is listed as "translation coming" in English mode.
"""
import base64, glob, html, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
# originals, one file per batch of chapters, read in chapter order: xuerong-zhixia-ch1-6.original.md, xuerong-zhixia-ch7.original.md, ...
SRC_GLOB = os.path.join(HERE, 'xuerong-zhixia-ch*.original.md')
OUT = os.path.join(HERE, 'dist')
TEMPLATE = os.path.join(HERE, 'reader-template.html')
EN_DIR = os.path.join(HERE, 'en')
EN_TITLE = 'Snowmelt Summer'
os.makedirs(OUT, exist_ok=True)


def curly(line):
    """Pair straight quotes within a line: " -> “ ” and ' -> ‘ ’."""
    for q, (o, c) in (('"', '“”'), ("'", '‘’')):
        if line.count(q) % 2:
            raise ValueError('unbalanced quotes: ' + line[:40])
        out, opening = [], True
        for ch in line:
            if ch == q:
                out.append(o if opening else c); opening = not opening
            else:
                out.append(ch)
        line = ''.join(out)
    return line


def parse(text):
    lines = text.split('\n')
    book = {'title': lines[0].lstrip('# ').strip(), 'chapters': []}
    ch = sec = None
    quote = None
    for raw in lines[1:]:
        line = raw.rstrip()
        if line.startswith('> ') or line.strip() == '>':
            if quote is None:
                quote = {'type': 'quote', 'lines': []}; sec['blocks'].append(quote)
            quote['lines'].append(curly(line[2:].strip())); continue
        quote = None
        if not line.strip():
            continue
        if line.startswith('# '):
            num, _, name = line[2:].strip().partition('　')
            ch = {'num': num, 'name': name, 'sections': []}; book['chapters'].append(ch); sec = None; continue
        if line.startswith('## '):
            sec = {'title': line[3:].strip(), 'blocks': []}; ch['sections'].append(sec); continue
        if line.strip() == '---':
            sec['blocks'].append({'type': 'break'}); continue
        t = curly(line.strip())
        m = re.fullmatch(r'\*\*(.+)\*\*', t)
        if m:  # in-game chat line, e.g. **<冬眠> 谁知道呢**
            sec['blocks'].append({'type': 'msg', 'text': m.group(1).strip()}); continue
        sec['blocks'].append({'type': 'msg' if t.startswith(('【', '[')) else 'p', 'text': t})
    # drop trailing scene breaks (the --- before each new chapter)
    for c in book['chapters']:
        b = c['sections'][-1]['blocks']
        while b and b[-1]['type'] == 'break':
            b.pop()
    return book


def count(c):
    return sum(len(re.findall(r'[一-鿿]', blk.get('text', '') + ''.join(blk.get('lines', []))))
               for s in c['sections'] for blk in s['blocks'])


def words(c):
    return sum(len(re.findall(r"[A-Za-z0-9’'-]+", blk.get('text', '') + ' ' + ' '.join(blk.get('lines', []))))
               for s in c['sections'] for blk in s['blocks'])


def load_english(zh):
    files = sorted(glob.glob(os.path.join(EN_DIR, 'ch*.md')), key=lambda f: int(re.findall(r'\d+', os.path.basename(f))[0]))
    if not files:
        return None
    en = parse(f'# {EN_TITLE}\n\n' + '\n\n'.join(open(f, encoding='utf-8').read() for f in files))
    norm = lambda bl: ['p' if b['type'] == 'msg' else b['type'] for b in bl]
    for i, ce in enumerate(en['chapters']):
        cz = zh['chapters'][i]
        if len(ce['sections']) != len(cz['sections']):
            raise SystemExit(f'English chapter {i + 1}: section count differs from the original')
        for j, (se, sz) in enumerate(zip(ce['sections'], cz['sections'])):
            if norm(se['blocks']) != norm(sz['blocks']):
                raise SystemExit(f'English chapter {i + 1}, section {j + 1}: paragraphs do not line up with the original')
    return en


def cleaned_markdown(book):
    """Markdown with curly quotes, for pandoc."""
    out = []
    for c in book['chapters']:
        out += [f'# {c["num"]}　{c["name"]}', '']
        for s in c['sections']:
            out += [f'## {s["title"]}', '']
            for b in s['blocks']:
                if b['type'] == 'break':
                    out += ['::: {.break custom-style="Scene Break"}', '＊　＊　＊', ':::', '']
                elif b['type'] == 'quote':
                    out += [('> ' + l + '  ') if l else '>' for l in b['lines']] + ['']
                else:
                    out += [b['text'].replace('<', '\\<').replace('>', '\\>'), '']
    return '\n'.join(out)


def render_html(book, lang='zh'):
    parts = []
    pre = '' if lang == 'zh' else 'en-'
    for i, c in enumerate(book['chapters'], 1):
        secs = []
        for s in c['sections']:
            body = []
            for b in s['blocks']:
                if b['type'] == 'p':
                    body.append(f'<p>{html.escape(b["text"], quote=False)}</p>')
                elif b['type'] == 'msg':
                    body.append(f'<p class="msg">{html.escape(b["text"], quote=False)}</p>')
                elif b['type'] == 'quote':
                    body.append('<blockquote>' + '<br>'.join(html.escape(l, quote=False) for l in b['lines']) + '</blockquote>')
                else:
                    body.append('<div class="break" aria-hidden="true"><span></span><span></span><span></span></div>')
            secs.append(f'<section class="sec"><h3>{html.escape(s["title"])}</h3>{"".join(body)}</section>')
        parts.append(
            f'<article class="chapter" id="{pre}ch{i}" data-ch="{i}" data-lang="{lang}" lang="{"zh-CN" if lang == "zh" else "en"}" aria-labelledby="{pre}ch{i}-t">'
            f'<header class="ch-head"><div class="ch-num">{html.escape(c["num"])}</div>'
            f'<h2 id="{pre}ch{i}-t">{html.escape(c["name"])}</h2>'
            + (f'<div class="ch-meta">{count(c):,} 字 · 约 {max(1, round(count(c) / 450))} 分钟</div></header>' if lang == 'zh'
               else f'<div class="ch-meta">{words(c):,} words · about {max(1, round(words(c) / 230))} min</div></header>')
            + ''.join(secs) +
            f'<nav class="ch-nav" aria-label="{"章节导航" if lang == "zh" else "Chapter navigation"}"></nav></article>')
    return '\n'.join(parts)


def format_docx(src, dst):
    """Chinese book formatting: 宋体 body, 2-character first-line indent, 1.5 spacing, chapters on new pages."""
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.shared import Pt, RGBColor, Cm
    doc = Document(src)
    for sec in doc.sections:
        sec.top_margin = sec.bottom_margin = Cm(2.54); sec.left_margin = sec.right_margin = Cm(3.0)
    def font(style, east, size=None, bold=None, color=None):
        style.font.name = east
        rpr = style.element.get_or_add_rPr()
        rf = rpr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts'); rpr.append(rf)
        for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
            rf.set(qn(a), east)
        for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
            if rf.get(qn(a)) is not None:
                del rf.attrib[qn(a)]
        if size: style.font.size = Pt(size)
        if bold is not None: style.font.bold = bold
        if color: style.font.color.rgb = RGBColor.from_string(color)
    def indent_chars(style, n):
        ppr = style.element.get_or_add_pPr()
        ind = ppr.find(qn('w:ind'))
        if ind is None:
            ind = OxmlElement('w:ind'); ppr.append(ind)
        ind.set(qn('w:firstLineChars'), str(n * 100))
    st = {s.name: s for s in doc.styles}
    for name in ('Normal', 'Body Text', 'First Paragraph', 'Compact'):
        if name in st:
            s = st[name]; font(s, '宋体', 12)
            s.paragraph_format.line_spacing = 1.5
            s.paragraph_format.space_after = Pt(0); s.paragraph_format.space_before = Pt(0)
            s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            indent_chars(s, 2)
    for name, size in (('Title', 26), ('Heading 1', 18), ('Heading 2', 12)):
        if name in st:
            s = st[name]; font(s, '黑体' if name != 'Heading 2' else '宋体', size, True, '1E2320' if name != 'Heading 2' else '2E5B4E')
            s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            s.paragraph_format.space_before = Pt(24 if name != 'Heading 2' else 18); s.paragraph_format.space_after = Pt(12)
    st['Heading 1'].paragraph_format.page_break_before = True
    for name in ('Block Text',):
        if name in st:
            s = st[name]; font(s, '楷体', 11.5); s.paragraph_format.left_indent = Cm(1.2); s.paragraph_format.right_indent = Cm(1.2)
    if 'Scene Break' in st:
        s = st['Scene Break']; s.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        s.paragraph_format.space_before = Pt(12); s.paragraph_format.space_after = Pt(12)
        ppr = s.element.get_or_add_pPr(); ind = ppr.find(qn('w:ind'))
        if ind is not None: ppr.remove(ind)
    for p in doc.paragraphs:
        if p.style.name == 'Scene Break':
            p.paragraph_format.first_line_indent = Cm(0)
    doc.core_properties.title = '雪融之夏'
    doc.save(dst)


def main():
    srcs = sorted(glob.glob(SRC_GLOB), key=lambda f: int(re.search(r'ch(\d+)', os.path.basename(f)).group(1)))
    text = '\n\n'.join(open(f, encoding='utf-8').read().strip() for f in srcs)
    book = parse(text)
    total = sum(count(c) for c in book['chapters'])
    toc = [{'num': c['num'], 'name': c['name'], 'chars': count(c),
            'sections': [s['title'] for s in c['sections']]} for c in book['chapters']]
    md = cleaned_markdown(book)
    md_path = os.path.join(OUT, 'xuerong-zhixia.md')
    open(md_path, 'w', encoding='utf-8').write(md)

    en = load_english(book)
    en_ch = en['chapters'] if en else []
    en_total = sum(words(c) for c in en_ch)
    ordinals = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
    toc_en = [({'num': c['num'], 'name': c['name'], 'chars': words(c), 'sections': [s['title'] for s in c['sections']]}
               if c else {'missing': True, 'num': f'Chapter {ordinals[i]}' if i < len(ordinals) else f'Chapter {i + 1}'})
              for i, c in enumerate(en_ch + [None] * (len(book['chapters']) - len(en_ch)))]

    # blurbs, chapter hooks and character portraits for the contents page
    blurbs = json.load(open(os.path.join(HERE, 'blurbs.json'), encoding='utf-8'))
    for lg, tc in (('zh', toc), ('en', toc_en)):
        for i, c in enumerate(tc):
            hooks = blurbs[lg]['chapters']
            c['teaser'] = hooks[i] if i < len(hooks) else ''
    imgs = {}
    for person in blurbs['zh']['cast']:
        f = os.path.join(HERE, 'art', person['img'] + '.jpg')
        if os.path.exists(f):
            imgs[person['img']] = 'data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
    extras = {'zh': {k: blurbs['zh'][k] for k in ('book', 'cast_title', 'cast')},
              'en': {k: blurbs['en'][k] for k in ('book', 'cast_title', 'cast')}, 'img': imgs}

    # reader page
    page = open(TEMPLATE, encoding='utf-8').read()
    page = page.replace('__EXTRAS__', json.dumps(extras, ensure_ascii=False))
    page = (page.replace('__CHAPTERS__', render_html(book) + '\n' + (render_html(en, 'en') if en else ''))
                .replace('__TOC__', json.dumps({'zh': toc, 'en': toc_en}, ensure_ascii=False))
                .replace('__EN_TOTAL__', f'{en_total:,}')
                .replace('__EN_MINUTES__', str(round(en_total / 230)))
                .replace('__EN_RANGE__', f'Chapters One to {ordinals[len(en_ch) - 1]}' if en_ch else '')
                .replace('__TOTAL__', f'{total:,}')
                .replace('__MINUTES__', str(round(total / 450)))
                .replace('__NCH__', str(len(book['chapters'])))
                .replace('__RANGE__', '第一至' + book['chapters'][-1]['num'][1:]))
    open(os.path.join(HERE, 'reader.html'), 'w', encoding='utf-8').write(page)

    # EPUB and Word via pandoc
    meta = ['--metadata', f'title={book["title"]}', '--metadata', 'lang=zh-CN', '--metadata', 'toc-title=目录']
    css = os.path.join(HERE, 'epub.css')
    cover = os.path.join(OUT, 'cover.png')
    epub_args = ['pandoc', md_path, '-o', os.path.join(OUT, 'xuerong-zhixia.epub'), '--split-level=1', '--toc', '--toc-depth=1', '--css', css] + meta
    if os.path.exists(cover):
        epub_args += ['--epub-cover-image', cover]
    subprocess.run(epub_args, check=True)
    raw = os.path.join(OUT, 'xuerong-zhixia.raw.docx')
    subprocess.run(['pandoc', md_path, '-o', raw] + meta, check=True)
    format_docx(raw, os.path.join(OUT, 'xuerong-zhixia.docx'))
    os.remove(raw)
    if en:
        en_md = os.path.join(OUT, 'snowmelt-summer.en.md')
        open(en_md, 'w', encoding='utf-8').write(cleaned_markdown(en).replace('＊　＊　＊', '·  ·  ·'))
        en_args = ['pandoc', en_md, '-o', os.path.join(OUT, 'snowmelt-summer.en.epub'), '--split-level=1', '--toc', '--toc-depth=1',
                   '--css', os.path.join(HERE, 'epub-en.css'), '--metadata', f'title={EN_TITLE}', '--metadata', 'lang=en', '--metadata', 'toc-title=Contents']
        if os.path.exists(os.path.join(OUT, 'cover.png')):
            en_args += ['--epub-cover-image', os.path.join(OUT, 'cover.png')]
        subprocess.run(en_args, check=True)
        print(f'English: {len(en_ch)} chapters, {en_total} words')
    print(f'{len(book["chapters"])} chapters, {total} characters')
    for c in toc:
        print(c['num'], c['name'], c['chars'], len(c['sections']))


if __name__ == '__main__':
    main()
