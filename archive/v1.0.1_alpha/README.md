# JsonToXmlConverter

A Python tool to convert JSON files to XML using the xmltodict library.

Designed for users needing to transform JSON data into XML for interoperability or data exchange.

## Installation

```bash
pip install -r requirements.txt
chmod +x json_to_xml.py
```

## Usage

### json_to_xml.py

```bash
./json_to_xml.py [--input_file discovery.json] [--output_file discovery.xml] [--verbose] [--logfile path]
```

### version_bumper.py

```bash
python version_bumper.py --project /path/to/project [--type minor] [--commit] [--git_tag] [--dry_run]
```

## Generated Files (via git_setup.py)

- **.gitignore**: Ignores Python, IDE, OS, and project-specific files (e.g., `__pycache__`, `.venv`, `tests/output/`).
- **README.md**: Project template with customizable title, installation, and usage.
- **CHANGELOG.md**: Initial changelog with a 0.1.0 entry, customizable author.
- **requirements.txt**: Placeholder for dependencies.
- **LICENSE**: MIT license with customizable author.
- **CONTRIBUTING.md**: Fork-branch-PR guidelines.
- **CODE_OF_CONDUCT.md**: Contributor Covenant with contact info.
- **tests/**: Directory with a placeholder test file.
- **version_bumper.py** (optional): Tool for bumping semantic versions.