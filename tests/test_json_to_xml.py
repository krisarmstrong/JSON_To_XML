#!/usr/bin/env python3
"""
Tests for JsonToXmlConverter.
"""
import json
import os
import pytest
from json_to_xml import __version__, convert_json_to_xml
from pathlib import Path

@pytest.fixture
def json_xml_files(tmp_path):
    """Create temporary JSON and XML files for testing."""
    input_path = tmp_path / "input.json"
    output_path = tmp_path / "output.xml"
    data = {"root": {"key": "value", "nested": {"a": 1, "b": 2}}}
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return input_path, output_path

def test_version() -> None:
    """Test version format."""
    assert __version__ == "1.0.1"

def test_convert_json_to_xml(json_xml_files) -> None:
    """Test converting a JSON file to XML."""
    input_path, output_path = json_xml_files
    convert_json_to_xml(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        xml_content = f.read()
    assert '<?xml version="1.0" encoding="utf-8"?>' in xml_content
    assert "<root>" in xml_content
    assert "<key>value</key>" in xml_content
    assert "<nested>" in xml_content
    assert "<a>1</a>" in xml_content
    assert "<b>2</b>" in xml_content

def test_convert_json_to_xml_invalid_json(tmp_path) -> None:
    """Test converting an invalid JSON file."""
    input_path = tmp_path / "invalid.json"
    output_path = tmp_path / "output.xml"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write("{invalid json}")
    with pytest.raises(json.JSONDecodeError):
        convert_json_to_xml(input_path, output_path)

def test_convert_json_to_xml_invalid_file() -> None:
    """Test converting a non-existent JSON file."""
    with pytest.raises(IOError):
        convert_json_to_xml(Path("nonexistent.json"), Path("output.xml"))