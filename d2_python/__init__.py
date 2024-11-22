import os
import platform
import subprocess
from pathlib import Path
from typing import Optional, Union
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

import tempfile


class D2:
    """
    Python wrapper for the D2 diagram scripting language.
    Supports multiple output formats, themes, and layout options.
    """

    def __init__(self):
        system = platform.system().lower()
        if system == "linux":
            platform_name = "linux"
        elif system == "windows":
            platform_name = "win32"
        elif system == "darwin":
            platform_name = "darwin"
        else:
            raise RuntimeError(f"Unsupported platform: {system}")

        package_dir = Path(__file__).parent
        binary_path = package_dir / "bin" / platform_name / "d2-bin"
        if platform_name == "win32":
            binary_path = binary_path.with_suffix(".exe")

        if not binary_path.exists():
            raise RuntimeError(f"D2 binary not found at {binary_path}")

        self.binary_path = str(binary_path)

    def render(self,
               input_source: str,
               output_file: str,
               format: Literal["svg", "png", "pdf"] = "svg",
               theme: Optional[Union[int, str]] = None,
               layout: Literal["dagre", "elk"] = "dagre",
               pad: int = 100,
               dark_theme: Optional[int] = None,
               sketch: bool = False,
               center: bool = False,
               scale: float = -1,
               bundle: bool = True,
               force_appendix: bool = False,
               timeout: int = 120,
               animate_interval: int = 0,
               target: str = "*",
               font_regular: Optional[str] = None,
               font_italic: Optional[str] = None,
               font_bold: Optional[str] = None,
               font_semibold: Optional[str] = None) -> None:
        """
        Render D2 diagram to specified format.

        Args:
            input_source: Input D2 file path or string content
            output_file: Output file path
            format: Output format (svg, png, pdf)
            theme: Theme ID (0-11) or name. See https://github.com/terrastruct/d2/tree/master/d2themes
            dark_theme: Theme ID to use when in dark mode. -1 uses the same theme as light mode
            layout: Layout engine (dagre, elk)
            pad: Padding in pixels
            sketch: Render the diagram to look like it was sketched by hand
            center: Center the SVG in the containing viewbox
            scale: Scale the output. -1 means SVGs fit to screen, others use default size
            bundle: When outputting SVG, bundle all assets and layers into the output file
            force_appendix: Force addition of appendix for tooltips and links in SVG exports
            timeout: Maximum number of seconds D2 runs before timing out
            animate_interval: Milliseconds between transitions when using multiple boards (SVG only)
            target: Target board to render. Use '*' for all scenarios, '' for root only
            font_regular: Path to .ttf file for regular font
            font_italic: Path to .ttf file for italic font
            font_bold: Path to .ttf file for bold font
            font_semibold: Path to .ttf file for semibold font
        """
        cmd = [self.binary_path]

        if theme is not None:
            cmd.extend(["--theme", str(theme)])

        if dark_theme is not None:
            cmd.extend(["--dark-theme", str(dark_theme)])

        cmd.extend(["--layout", layout])
        cmd.extend(["--pad", str(pad)])

        if sketch:
            cmd.append("--sketch")

        if center:
            cmd.append("--center")

        if scale != -1:
            cmd.extend(["--scale", str(scale)])

        if not bundle:
            cmd.extend(["--bundle", "false"])

        if force_appendix:
            cmd.append("--force-appendix")

        if timeout != 120:
            cmd.extend(["--timeout", str(timeout)])

        if animate_interval > 0:
            cmd.extend(["--animate-interval", str(animate_interval)])

        if target != "*":
            cmd.extend(["--target", target])

        for font_type, font_path in [
            ("regular", font_regular),
            ("italic", font_italic),
            ("bold", font_bold),
            ("semibold", font_semibold)
        ]:
            if font_path:
                cmd.extend([f"--font-{font_type}", str(font_path)])

        if format != "svg":
            cmd.extend(["--format", format])

        # Handle string input
        if not os.path.isfile(input_source):
            with tempfile.NamedTemporaryFile(mode='w', suffix='.d2', delete=False) as tmp:
                tmp.write(input_source)
                input_path = tmp.name
        else:
            input_path = input_source

        cmd.extend([input_path, output_file])

        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        finally:
            # Clean up temp file if created
            if input_path != input_source:
                try:
                    os.unlink(input_path)
                except OSError:
                    pass  # Ignore cleanup errors