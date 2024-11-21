import os
import platform
import subprocess
from pathlib import Path


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

    def render(self, input_file: str, output_file: str):
        subprocess.run([self.binary_path, input_file, output_file], check=True)
