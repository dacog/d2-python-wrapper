import os
import platform
import subprocess
from pathlib import Path
from typing import Optional
import tempfile


class D2:
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
               format: str = "svg",
               theme: Optional[str] = None,
               layout: str = "dagre",
               pad: int = 100) -> None:
        """
        Render D2 diagram to specified format.

        Args:
            input_source: Input D2 file path or string content
            output_file: Output file path
            format: Output format (svg, png, pdf)
            theme: Theme name (dark, light)
            layout: Layout engine (dagre, elk)
            pad: Padding in pixels
        """
        cmd = [self.binary_path]

        if theme:
            cmd.extend(["--theme", theme])

        cmd.extend(["--layout", layout])
        cmd.extend(["--pad", str(pad)])

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