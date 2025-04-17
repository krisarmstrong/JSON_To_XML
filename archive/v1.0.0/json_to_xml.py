#!/usr/bin/env python

"""
JSON to XML Converter
=====================

This script converts a JSON file to an XML file using the xmltodict library.
It is designed for users who need to transform JSON data into XML format for
interoperability or data exchange.

Author: Kris Armstrong
Version: 1.0.0
Date: April 18, 2025
"""

__title__ = "JSON to XML Converter"
__author__ = "Kris Armstrong"
__version__ = "1.0.1"

# Standard Library Imports
import argparse
import logging
import sys
from pathlib import Path

# Third-Party Imports
import xmltodict
import json

# Global Configuration
class Config:
    """Global configuration constants for the JSON to XML Converter."""
    log_file = "json_to_xml.log"  # Log file for debugging and info
    encoding = "utf-8"  # Default file encoding
    default_input = "discovery.json"  # Default input file
    default_output = "discovery.xml"  # Default output file


def setup_logging(verbose=False):
    """Configure logging to write to a file with a standardized format.

    Args:
        verbose (bool): If True, also log to console.
    """
    logging.basicConfig(
        filename=Config.log_file,
        filemode="w",
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        )
        logging.getLogger().addHandler(console_handler)


def parse_arguments():
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.

    Raises:
        SystemExit: If arguments are invalid.
    """
    parser = argparse.ArgumentParser(
        description="Convert a JSON file to an XML file."
    )
    parser.add_argument(
        "--input",
        default=Config.default_input,
        help=f"Path to the input JSON file (default: {Config.default_input})",
    )
    parser.add_argument(
        "--output",
        default=Config.default_output,
        help=f"Path to the output XML file (default: {Config.default_output})",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose console output",
    )

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.is_file():
        parser.error(f"Input file does not exist: {args.input}")
    if input_path.suffix.lower() != ".json":
        parser.error(f"Input file must be a JSON file: {args.input}")

    return args


def convert_json_to_xml(input_path, output_path):
    """Convert a JSON file to an XML file.

    Args:
        input_path (Path): Path to the input JSON file.
        output_path (Path): Path to the output XML file.

    Returns:
        bool: True if conversion is successful, False otherwise.

    Raises:
        json.JSONDecodeError: If the input file is not valid JSON.
        IOError: If file read/write operations fail.
    """
    try:
        # Read JSON file
        logging.debug("Reading JSON file: %s", input_path)
        with input_path.open("r", encoding=Config.encoding) as json_file:
            json_data = json.load(json_file)
        logging.info("Successfully read JSON file: %s", input_path)

        # Convert to XML
        logging.debug("Converting JSON to XML")
        xml_data = xmltodict.unparse(json_data, pretty=True)
        logging.info("Successfully converted JSON to XML")

        # Write XML file
        logging.debug("Writing XML file: %s", output_path)
        with output_path.open("w", encoding=Config.encoding) as xml_file:
            xml_file.write(xml_data)
        logging.info("Successfully wrote XML file: %s", output_path)

        return True

    except json.JSONDecodeError as err:
        logging.error("Invalid JSON in file %s: %s", input_path, err)
        raise
    except IOError as err:
        logging.error("File operation failed: %s", err)
        raise


def main():
    """Main function to convert JSON to XML."""
    args = parse_arguments()
    setup_logging(args.verbose)

    input_path = Path(args.input)
    output_path = Path(args.output)

    try:
        logging.info("Starting JSON to XML conversion: %s -> %s", input_path, output_path)
        if convert_json_to_xml(input_path, output_path):
            print(f"{input_path} has been converted to {output_path}")
            logging.info("Conversion completed successfully")
        sys.exit(0)

    except json.JSONDecodeError as err:
        print(f"Error: Invalid JSON in {input_path}: {err}")
        logging.error("Conversion failed: %s", err)
        sys.exit(1)
    except IOError as err:
        print(f"Error: File operation failed: {err}")
        logging.error("Conversion failed: %s", err)
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error: {err}")
        logging.error("Unexpected error: %s", err)
        sys.exit(1)


if __name__ == "__main__":
    main()