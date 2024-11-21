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

## Features

- Automatic platform detection and binary management
- Support for multiple output formats (svg, png, pdf)
- Theme customization
- Layout engine options

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

## API Reference

### D2 Class

#### render(input_file, output_file, **options)
- `input_file`: Path to D2 source file
- `output_file`: Path for output file
- Options:
  - `format`: Output format ('svg', 'png', 'pdf'). Default: 'svg'
  - `theme`: Theme name ('dark', 'light', etc.). Default: system theme
  - `layout`: Layout engine ('dagre', 'elk'). Default: 'dagre'
  - `pad`: Padding in pixels. Default: 100

## License

Mozilla Public License Version 2.0 (same as https://github.com/terrastruct/d2)