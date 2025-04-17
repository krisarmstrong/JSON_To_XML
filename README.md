# JsonToXmlConverter

Converts JSON files to XML using the xmltodict library.

## Installation

```bash
git clone https://github.com/krisarmstrong/json-to-xml-converter
cd json-to-xml-converter
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python json_to_xml.py --input_file discovery.json --output_file discovery.xml --verbose
```

- `--input_file`: Input JSON file (default: discovery.json).
- `--output_file`: Output XML file (default: discovery.xml).
- `--verbose`: Enable verbose logging.
- `--logfile`: Log file path (default: json_to_xml.log).

## Files

- `json_to_xml.py`: Main script.
- `version_bumper.py`: Version management tool.
- `tests/test_json_to_xml.py`: Pytest suite.
- `requirements.txt`: Dependencies.
- `CHANGELOG.md`: Version history.
- `LICENSE`: MIT License.
- `CONTRIBUTING.md`: Contribution guidelines.
- `CODE_OF_CONDUCT.md`: Contributor Covenant.

## GitHub Setup

```bash
gh repo create json-to-xml-converter --public --source=. --remote=origin
git init
git add .
git commit -m "Initial commit: JsonToXmlConverter v1.0.1"
git tag v1.0.1
git push origin main --tags
```

## Contributing

See CONTRIBUTING.md for details.

## License

MIT License. See LICENSE for details.