#!/usr/bin/env python3
"""
Project Title: JsonToXmlConverter

Converts a JSON file to an XML file using the xmltodict library.

Designed for users needing to transform JSON data into XML for interoperability or data exchange.

Author: Kris Armstrong
"""
__version__ = "1.0.1"

import argparse
import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path
from typing import Optional
import xmltodict
import json

class Config:
    """Global configuration constants for JsonToXmlConverter."""
    LOG_FILE: str = "json_to_xml.log"
    ENCODING: str = "utf-8"
    DEFAULT_INPUT: str = "discovery.json"
    DEFAULT_OUTPUT: str = "discovery.xml"

def setup_logging(verbose: bool, logfile: Optional[str] = None) -> None:
    """Configure logging with console and rotating file handler.

    Args:
        verbose: Enable DEBUG level logging to console if True.
        logfile: Path to log file, defaults to Config.LOG_FILE if unspecified.

    Returns:
        None
    """
    logger = logging.getLogger()
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(console_handler)
    logfile = logfile or Config.LOG_FILE
    file_handler = RotatingFileHandler(logfile, maxBytes=10_000_000, backupCount=5)
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
    logger.addHandler(file_handler)

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed command-line arguments.

    Raises:
        SystemExit: If arguments are invalid.
    """
    parser = argparse.ArgumentParser(
        description="Convert a JSON file to an XML file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--input_file",
        default=Config.DEFAULT_INPUT,
        help=f"Path to input JSON file (default: {Config.DEFAULT_INPUT})"
    )
    parser.add_argument(
        "--output_file",
        default=Config.DEFAULT_OUTPUT,
        help=f"Path to output XML file (default: {Config.DEFAULT_OUTPUT})"
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose console output"
    )
    parser.add_argument(
        "--logfile",
        help="Path to log file"
    )

    args = parser.parse_args()
    input_path = Path(args.input_file)
    if not input_path.is_file():
        parser.error(f"Input file does not exist: {args.input_file}")
    if input_path.suffix.lower() != ".json":
        parser.error(f"Input file must be a JSON file: {args.input_file}")

    return args

def convert_json_to_xml(input_path: Path, output_path: Path) -> bool:
    """Convert a JSON file to an XML file.

    Args:
        input_path: Path to the input JSON file.
        output_path: Path to the output XML file.

    Returns:
        True if conversion is successful.

    Raises:
        json.JSONDecodeError: If the input file is not valid JSON.
        IOError: If file read/write operations fail.
    """
    try:
        logging.debug("Reading JSON file: %s", input_path)
        with input_path.open("r", encoding=Config.ENCODING) as json_file:
            json_data = json.load(json_file)
        logging.info("Successfully read JSON file: %s", input_path)

        logging.debug("Converting JSON to XML")
        xml_data = xmltodict.unparse(json_data, pretty=True)
        logging.info("Successfully converted JSON to XML")

        logging.debug("Writing XML file: %s", output_path)
        with output_path.open("w", encoding=Config.ENCODING) as xml_file:
            xml_file.write(xml_data)
        logging.info("Successfully wrote XML file: %s", output_path)

        return True
    except json.JSONDecodeError as err:
        logging.error("Invalid JSON in file %s: %s", input_path, err)
        raise
    except IOError as err:
        logging.error("File operation failed: %s", err)
        raise

def main() -> None:
    """Convert JSON to XML and handle errors."""
    try:
        args = parse_arguments()
        setup_logging(args.verbose, args.logfile)
        input_path = Path(args.input_file)
        output_path = Path(args.output_file)
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
    except KeyboardInterrupt:
        logging.info("Cancelled by user")
        sys.exit(0)
    except Exception as err:
        print(f"Unexpected error: {err}")
        logging.error("Unexpected error: %s", err)
        sys.exit(1)

if __name__ == "__main__":
    main()