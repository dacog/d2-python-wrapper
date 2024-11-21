import pytest
from d2_python import D2
import os
from pathlib import Path
import tempfile
from unittest import mock
import subprocess


@pytest.fixture
def d2():
    return D2()


def test_binary_detection(d2):
    """Test if the D2 binary exists and is executable in the expected location"""
    assert os.path.exists(d2.binary_path)
    assert os.access(d2.binary_path, os.X_OK)


def test_wrapper_vs_binary_output(d2, tmp_path):
    """
    Verify that the wrapper produces identical output to direct binary usage.
    This ensures our wrapper doesn't modify the D2 output in any way.
    """
    diagram = "x -> y"
    wrapper_output = tmp_path / "wrapper.svg"
    binary_output = tmp_path / "binary.svg"
    input_file = tmp_path / "test.d2"

    # Generate output using wrapper with string input
    d2.render(diagram, str(wrapper_output))

    # Generate output using binary directly with file input
    input_file.write_text(diagram)
    subprocess.run([d2.binary_path, str(input_file), str(binary_output)], check=True)

    # Compare binary outputs to ensure they're identical
    assert wrapper_output.read_bytes() == binary_output.read_bytes()


def test_temp_file_cleanup(d2, tmp_path):
    """
    Verify that temporary files are properly cleaned up after rendering.
    Checks that no .d2 files are left in the temp directory.
    """
    temp_files_before = list(Path(tempfile.gettempdir()).glob("*.d2"))

    with mock.patch('subprocess.run') as mock_run:
        mock_run.return_value = mock.Mock(returncode=0)
        d2.render("x -> y", str(tmp_path / "output.svg"))

    temp_files_after = list(Path(tempfile.gettempdir()).glob("*.d2"))
    assert temp_files_before == temp_files_after


def test_command_construction(d2, tmp_path):
    """
    Test that the wrapper correctly constructs D2 command with all options.
    Verifies that each option (theme, layout, pad, format) is properly included
    in the command passed to the binary.
    """
    with mock.patch('subprocess.run') as mock_run:
        mock_run.return_value = mock.Mock(returncode=0)

        d2.render(
            "x -> y",
            str(tmp_path / "output.svg"),
            theme='dark',
            layout='elk',
            pad=200,
            format='png'
        )

        cmd = mock_run.call_args[0][0]
        assert all(x in cmd for x in ['--theme', 'dark'])
        assert all(x in cmd for x in ['--layout', 'elk'])
        assert all(x in cmd for x in ['--pad', '200'])
        assert all(x in cmd for x in ['--format', 'png'])