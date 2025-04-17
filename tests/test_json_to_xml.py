#!/usr/bin/env python3
"""
Project Title: JsonToXmlConverterTests

Pytest smoke tests for json_to_xml.py functionality.

Author: Kris Armstrong
"""
__version__ = "1.0.0"

import pytest
import subprocess
from pathlib import Path
import json_to_xml

@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for testing.

    Args:
        tmp_path: Pytest-provided temporary path.

    Returns:
        Path to temporary directory.
    """
    return tmp_path

def test_convert_json_to_xml(temp_dir: Path) -> None:
    """Test JSON to XML conversion."""
    input_file = temp_dir / "test.json"
    output_file = temp_dir / "test.xml"
    input_file.write_text('{"key": "value"}')
    result = json_to_xml.convert_json_to_xml(input_file, output_file)
    assert result is True
    assert output_file.exists()

def test_keyboard_interrupt(temp_dir: Path, caplog: pytest.LogCaptureFixture) -> None:
    """Test KeyboardInterrupt handling.

    Args:
        temp_dir: Temporary directory for testing.
        caplog: Pytest fixture to capture log output.
    """
    with pytest.raises(SystemExit) as exc:
        json_to_xml.setup_logging(False)
        raise KeyboardInterrupt
    assert exc.value.code == 0
    assert "Cancelled by user" in caplog.text

def test_version_bumper_generation(temp_dir: Path) -> None:
    """Test version_bumper.py generation."""
    from git_setup import VERSION_BUMPER_TEMPLATE, create_file
    create_file(temp_dir / 'version_bumper.py', VERSION_BUMPER_TEMPLATE)
    assert (temp_dir / 'version_bumper.py').exists()
    result = subprocess.run(['python', 'version_bumper.py', '--help'], cwd=temp_dir, capture_output=True, text=True)
    assert result.returncode == 0