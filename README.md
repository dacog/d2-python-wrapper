# D2 Python Wrapper

A Python wrapper for the [D2](https://github.com/terrastruct/d2) diagram scripting language.

## Installation

```bash
pip install d2-python-wrapper
```

## Quick Start

```python
from d2_python import D2

d2 = D2()

# Simple diagram
with open("test.d2", "w") as f:
    f.write("x -> y")

# Default SVG output
d2.render("test.d2", "output.svg")

# PDF output with specific theme
d2.render("test.d2", "output.pdf", format="pdf", theme="dark")
```

## Tests

```shell
pip install pytest pytest-mock
pytest test_d2.py -v
```

## Features

- Automatic platform detection and binary management
- Support for multiple output formats (svg, png, pdf)
- Theme customization with dark mode support
- Layout engine options (dagre, elk)
- Hand-drawn sketch mode
- SVG enhancements:
  - Asset bundling
  - Center alignment
  - Custom scaling
  - Animation support

## Local Development Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

2. Get D2 locally:
```bash
curl -L "https://github.com/terrastruct/d2/releases/download/v0.6.8/d2-v0.6.8-linux-amd64.tar.gz" -o linux.tar.gz
tar xzf linux.tar.gz
mkdir -p d2_python/bin/linux
cp d2-v0.6.8/bin/d2 d2_python/bin/linux/d2-bin
chmod +x d2_python/bin/linux/d2-bin
```

3. Install in development mode:
```bash
pip install -e .
```

4. Render a diagram

```shell
echo "hello -> world" > test.d2
```

```python
from d2_python import D2
d2 = D2()
d2.render("test.d2", "output.svg") 
```

## API Reference

## API Reference

### D2 Class

#### render(input_source, output_file, **options)

- `input_source`: Path to D2 source file or string content
- `output_file`: Path for output file
- Options:
  - `format`: Output format ('svg', 'png', 'pdf'). Default: 'svg'
  - `theme`: Theme ID (0-11) or name. Default: system theme
  - `dark_theme`: Theme ID for dark mode. Default: None (uses same as light)
  - `layout`: Layout engine ('dagre', 'elk'). Default: 'dagre'
  - `pad`: Padding in pixels. Default: 100
  - `sketch`: Render in hand-drawn style. Default: False
  - `center`: Center SVG in viewbox. Default: False
  - `scale`: Output scaling (-1 for auto). Default: -1
  - `bundle`: Bundle SVG assets. Default: True
  - `force_appendix`: Force tooltip appendix. Default: False
  - `timeout`: Execution timeout in seconds. Default: 120
  - `animate_interval`: Animation interval in ms. Default: 0
  - `target`: Target board to render. Default: "*"
  - Font customization:
    - `font_regular`: Path to regular .ttf
    - `font_italic`: Path to italic .ttf
    - `font_bold`: Path to bold .ttf
    - `font_semibold`: Path to semibold .ttf

## License

Mozilla Public License Version 2.0 (same as https://github.com/terrastruct/d2)