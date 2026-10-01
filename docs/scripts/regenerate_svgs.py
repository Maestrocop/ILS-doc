from pathlib import Path

images_dir = Path(__file__).resolve().parent.parent / 'images'
images_dir.mkdir(parents=True, exist_ok=True)


def save_svg(name, content):
    path = images_dir / name
    path.write_text(content, encoding='utf-8')
    return path


def escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def svg_box(x, y, width, height, label, font_size=12):
    lines = label.replace('<br/>', '\n').split('\n')
    line_height = font_size * 1.2
    total_height = line_height * len(lines)
    start_y = y + (height - total_height) / 2 + font_size
    text_parts = [f'<text x="{x + width/2}" y="{start_y}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{font_size}" fill="#0d1b41">']
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        text_parts.append(f'  <tspan x="{x + width/2}" dy="{dy}">{escape(line)}</tspan>')
    text_parts.append('</text>')
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" ry="8" fill="#f5f7ff" stroke="#3f51b5" stroke-width="2" />\n' + '\n'.join(text_parts)


def svg_line(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#233d8a" stroke-width="2" marker-end="url(#arrowhead)" />'


def svg_container(width, height, inner):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">\n  <defs>\n    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">\n      <polygon points="0 0, 10 3.5, 0 7" fill="#233d8a" />\n    </marker>\n  </defs>\n  <rect width="{width}" height="{height}" fill="#ffffff" />\n  {inner}\n</svg>'''


def bottom_center(box):
    x, y, w, h = box[1:5]
    return x + w / 2, y + h


def top_center(box):
    x, y, w, h = box[1:5]
    return x + w / 2, y


def generate_architecture():
    boxes = [
        ('Learning Evidence', 40, 30, 180, 60),
        ('Outcome Engine', 260, 30, 180, 60),
        ('Outcome Category Layer', 480, 30, 180, 60),
        ('Applied Skills', 40, 130, 160, 50),
        ('Knowledge', 220, 130, 160, 50),
        ('Professional Practice', 400, 130, 160, 50),
        ('Critical Competency', 580, 130, 160, 50),
        ('Creative / Portfolio', 760, 130, 180, 50),
        ('decaying_average', 40, 220, 160, 50),
        ('average', 220, 220, 160, 50),
        ('weighted_average', 400, 220, 160, 50),
        ('n_number_of_times', 580, 220, 160, 50),
        ('highest_score', 760, 220, 180, 50),
        ('Mastery Score per Outcome', 260, 320, 220, 60),
        ('Threshold Evaluation', 260, 410, 220, 60),
        ('Student Intelligence Layer', 260, 500, 220, 60),
        ('Student Cockpit', 40, 590, 180, 50),
        ('Heatmap View', 260, 590, 180, 50),
        ('Student Intelligence Panel', 480, 590, 220, 50),
        ('Teacher Actions', 260, 660, 220, 50),
        ('Intervention / Support / Grading / Progress Tracking', 260, 730, 340, 50),
    ]
    inner = [svg_box(b[1], b[2], b[3], b[4], b[0], font_size=12) for b in boxes]
    lines = []
    lines.append(svg_line(*bottom_center(boxes[0]), *top_center(boxes[1])))
    lines.append(svg_line(*bottom_center(boxes[1]), *top_center(boxes[2])))
    for i in range(3, 8):
        lines.append(svg_line(*bottom_center(boxes[2]), *top_center(boxes[i])))
    for i in range(3, 8):
        lines.append(svg_line(*bottom_center(boxes[i]), *top_center(boxes[8 + i - 3])))
    for i in range(8, 13):
        lines.append(svg_line(*bottom_center(boxes[i]), *top_center(boxes[13])))
    lines.append(svg_line(*bottom_center(boxes[13]), *top_center(boxes[14])))
    lines.append(svg_line(*bottom_center(boxes[14]), *top_center(boxes[15])))
    lines.append(svg_line(*bottom_center(boxes[15]), *top_center(boxes[16])))
    lines.append(svg_line(*bottom_center(boxes[16]), *top_center(boxes[17])))
    lines.append(svg_line(*bottom_center(boxes[16]), *top_center(boxes[18])))
    lines.append(svg_line(*bottom_center(boxes[16]), *top_center(boxes[19])))
    lines.append(svg_line(*bottom_center(boxes[17]), *top_center(boxes[20])))
    lines.append(svg_line(*bottom_center(boxes[18]), *top_center(boxes[20])))
    lines.append(svg_line(*bottom_center(boxes[19]), *top_center(boxes[20])))
    inner.extend(lines)
    save_svg('architecture-overview.svg', svg_container(980, 820, '\n  '.join(inner)))


def generate_simplified():
    boxes = [
        ('Learning Evidence', 40, 40, 180, 50),
        ('Outcome Engine', 260, 40, 180, 50),
        ('Outcome Categories\n(logic layer)', 480, 40, 200, 50),
        ('Calculation Method\n(rule engine)', 720, 40, 200, 50),
        ('Mastery Score', 260, 140, 180, 50),
        ('Decision Layer\n(thresholds)', 480, 140, 180, 50),
        ('Student Intelligence System', 260, 240, 180, 50),
        ('Teacher Actions', 480, 240, 180, 50),
    ]
    inner = [svg_box(b[1], b[2], b[3], b[4], b[0], font_size=12) for b in boxes]
    lines = []
    lines.append(svg_line(*bottom_center(boxes[0]), *top_center(boxes[1])))
    lines.append(svg_line(*bottom_center(boxes[1]), *top_center(boxes[2])))
    lines.append(svg_line(*bottom_center(boxes[2]), *top_center(boxes[3])))
    lines.append(svg_line(*bottom_center(boxes[1]), *top_center(boxes[4])))
    lines.append(svg_line(*bottom_center(boxes[3]), *top_center(boxes[5])))
    lines.append(svg_line(*bottom_center(boxes[4]), *top_center(boxes[6])))
    lines.append(svg_line(*bottom_center(boxes[5]), *top_center(boxes[7])))
    inner.extend(lines)
    save_svg('simplified-mental-model.svg', svg_container(960, 320, '\n  '.join(inner)))


def generate_panel():
    boxes = [
        ('Learning Evidence', 40, 40, 180, 50),
        ('Outcome Engine', 240, 40, 180, 50),
        ('Outcome Category System', 440, 40, 180, 50),
        ('Applied Skills', 40, 130, 160, 50),
        ('Knowledge', 220, 130, 160, 50),
        ('Professional Practice', 400, 130, 160, 50),
        ('Critical Competency', 40, 200, 160, 50),
        ('Creative / Portfolio', 220, 200, 160, 50),
        ('Calculation Methods', 440, 190, 240, 50),
        ('Mastery Scores per Outcome', 440, 260, 240, 50),
        ('Threshold & Risk Evaluation', 440, 330, 240, 50),
        ('Student Risk Signals', 440, 400, 240, 50),
        ('Student Cockpit', 40, 500, 180, 50),
        ('Student Intelligence Panel', 260, 500, 240, 50),
        ('Outcome Breakdown', 40, 580, 140, 50),
        ('Trends per Outcome', 200, 580, 140, 50),
        ('Overdue / Pending Context', 360, 580, 140, 50),
        ('Recency of Assessment', 520, 580, 140, 50),
        ('Weakest Skills Analysis', 680, 580, 140, 50),
        ('Teacher Decision Layer', 260, 660, 240, 50),
        ('Intervention / Support / Feedback', 40, 740, 180, 50),
        ('Grading Actions', 260, 740, 180, 50),
        ('Monitoring', 520, 740, 180, 50),
    ]
    inner = [svg_box(b[1], b[2], b[3], b[4], b[0], font_size=12) for b in boxes]
    lines = [
        svg_line(*bottom_center(boxes[0]), *top_center(boxes[1])),
        svg_line(*bottom_center(boxes[1]), *top_center(boxes[2])),
        svg_line(*bottom_center(boxes[2]), *top_center(boxes[3])),
        svg_line(*bottom_center(boxes[2]), *top_center(boxes[4])),
        svg_line(*bottom_center(boxes[2]), *top_center(boxes[5])),
        svg_line(*bottom_center(boxes[2]), *top_center(boxes[6])),
        svg_line(*bottom_center(boxes[2]), *top_center(boxes[7])),
        svg_line(*bottom_center(boxes[3]), *top_center(boxes[8])),
        svg_line(*bottom_center(boxes[4]), *top_center(boxes[8])),
        svg_line(*bottom_center(boxes[5]), *top_center(boxes[8])),
        svg_line(*bottom_center(boxes[6]), *top_center(boxes[8])),
        svg_line(*bottom_center(boxes[7]), *top_center(boxes[8])),
        svg_line(*bottom_center(boxes[8]), *top_center(boxes[9])),
        svg_line(*bottom_center(boxes[9]), *top_center(boxes[10])),
        svg_line(*bottom_center(boxes[10]), *top_center(boxes[11])),
        svg_line(*bottom_center(boxes[11]), *top_center(boxes[13])),
        svg_line(*bottom_center(boxes[12]), *top_center(boxes[19])),
        svg_line(*bottom_center(boxes[13]), *top_center(boxes[19])),
        svg_line(*bottom_center(boxes[19]), *top_center(boxes[20])),
        svg_line(*bottom_center(boxes[19]), *top_center(boxes[21])),
        svg_line(*bottom_center(boxes[19]), *top_center(boxes[22])),
    ]
    inner.extend(lines)
    save_svg('student-intelligence-panel-architecture.svg', svg_container(940, 860, '\n  '.join(inner)))


def generate_ai_ready():
    boxes = [
        ('Raw Data', 40, 40, 180, 50),
        ('Structured Signals', 260, 40, 180, 50),
        ('Human Reasoning\n(Panel)', 480, 40, 220, 50),
        ('AI-ready Layer', 740, 40, 180, 50),
    ]
    inner = [svg_box(b[1], b[2], b[3], b[4], b[0], font_size=12) for b in boxes]
    lines = [svg_line(*bottom_center(boxes[i]), *top_center(boxes[i + 1])) for i in range(3)]
    inner.extend(lines)
    save_svg('ai-ready-reasoning-layer.svg', svg_container(960, 140, '\n  '.join(inner)))

if __name__ == '__main__':
    generate_architecture()
    generate_simplified()
    generate_panel()
    generate_ai_ready()
    print('SVG regeneration complete')
