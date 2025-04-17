# JSON to XML Converter

## Overview

The JSON to XML Converter is a Python 3 script that transforms a JSON file into an XML file using the `xmltodict` library. It is designed for users who need to convert JSON data into XML format for interoperability, data exchange, or legacy system compatibility. The script supports command-line arguments for specifying input and output files, logs operations for debugging, and validates inputs to ensure robust operation.

## Features

- Converts JSON files to XML with human-readable formatting (indented).
- Accepts custom input and output file paths via command-line arguments.
- Defaults to `discovery.json` and `discovery.xml` for compatibility with original scripts.
- Validates input file existence and JSON format.
- Logs operations and errors to `json_to_xml.log`.
- Provides verbose console output option for real-time feedback.
- Uses cross-platform file handling with `pathlib`.
- Requires minimal dependencies (only `xmltodict`).

## Requirements

- Python 3.6 or later.
- Third-party library: `xmltodict` (listed in `requirements.txt`).
- Read permissions for the input JSON file.
- Write permissions for the output XML file and log file.

## Installation

1. Install Python 3.6 or later on your system.

2. Clone or download the project repository.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the script has executable permissions:

   ```bash
   chmod +x json_to_xml.py
   ```

## Usage

Run the script with optional input and output file paths:

```bash
./json_to_xml.py --input discovery.json --output discovery.xml
```

If no arguments are provided, it defaults to `discovery.json` and `discovery.xml`:

```bash
./json_to_xml.py
```

### Command-Line Options

- `--input INPUT`: Path to the input JSON file (default: `discovery.json`).
- `--output OUTPUT`: Path to the output XML file (default: `discovery.xml`).
- `-v, --version`: Display the script version (1.0.0).
- `--verbose`: Enable verbose console output.

### Example Commands

Convert `data.json` to `data.xml`:

```bash
./json_to_xml.py --input data.json --output data.xml
```

Use defaults with verbose output:

```bash
./json_to_xml.py --verbose
```

### Example Output

```
discovery.json has been converted to discovery.xml
```

If the input file is invalid:

```
Error: Invalid JSON in data.json: Expecting value: line 1 column 1 (char 0)
```

## Project Structure

```
json-to-xml/
├── archive/
│   └── v1.0.0/
│       ├── main.py          # Original script using json2xml
│       └── json2xml.py      # Original script using xmltodict
├── json_to_xml.py           # Current script (version 1.0.0)
├── requirements.txt         # Lists xmltodict
├── README.md                # Project documentation
├── changelog.txt            # Version history
├── bump_version.py          # Version increment script
└── .gitignore               # Git ignore rules
```

- The `archive/v1.0.0/` folder contains the original scripts for reference.
- The root folder holds the active development files.

## Development

### Installation for Development

```bash
git clone <repository-url>
cd json-to-xml
pip install -r requirements.txt
```

### Versioning

To increment the version number and update the changelog, use the `bump_version.py` script:

```bash
python3 bump_version.py "Added new feature X"
```

This increments the patch version (e.g., 1.0.0 to 1.0.1), updates `json_to_xml.py`, and appends a changelog entry.

### Git Workflow

- **Branches**:
  - `main`: Stable, production-ready code.
  - `develop`: Integration branch for new features and fixes.
  - Feature/bugfix branches: Named `feature/<name>` or `bugfix/<name>`.
- **Commit Messages**:
  - Format: `<type>(<scope>): <description>`
  - Types: `feat`, `fix`, `docs`, `refactor`, `chore`.
  - Example: `feat(conversion): Add support for custom XML root tags`

## Notes

- **Dependency**: The script uses `xmltodict` for JSON-to-XML conversion, chosen for its active maintenance and simplicity.
- **Original Scripts**: The original `main.py` (using `json2xml`) and `json2xml.py` (using `xmltodict`) are archived in `archive/v1.0.0/` for reference.
- **Log File**: The log file is overwritten on each run to manage storage.
- **Interrupt Handling**: Use `Ctrl+C` to stop the script gracefully.
- **Encoding**: Files are read/written using UTF-8 encoding.
- **XML Formatting**: The output XML is pretty-printed with indentation for readability.

## Known Limitations

- Assumes UTF-8 encoding for input and output files.
- Does not support advanced XML customization (e.g., custom root tags or attributes) without modifying the script.
- Validation is limited to JSON syntax and file existence; it does not check JSON schema or content.

## Contributing

This script is maintained by Kris Armstrong. For bug reports or feature requests, please contact the maintainer.

## License

This software is open-source under the MIT License. See LICENSE file for details (if applicable).

## Version

1.0.0 (April 18, 2025)