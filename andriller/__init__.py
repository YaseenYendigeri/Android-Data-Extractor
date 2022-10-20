__version__ = "1.1.0"
__app_name__ = "Android Data Extractor"
__package_name__ = "andriller"
__website__ = "https://github.com/YaseenYendigeri/Android-Data-Extractor"
__license__ = "None"
__all__ = ["gui"]

import os
import logging

logger = logging.getLogger(__name__)


def run():
    import argparse

    parser = argparse.ArgumentParser(
        description="ADE execution with CLI options."
    )
    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        help="Run with log level set to debug.",
    )
    parser.add_argument(
        "-f", "--file", help="Save log to a file, use with --debug flag."
    )
    parser.add_argument(
        "--nothread",
        dest="nothread",
        action="store_true",
        help="Disable threading on GUI.",
    )
    parser.add_argument(
        "-v", "--version", dest="version", action="store_true", help="Show the version."
    )
    parser.set_defaults(debug=False, file=None, version=None)
    args = parser.parse_args()
    # Set logging level
    level = logging.DEBUG if args.debug else logging.INFO

    # Print version
    if args.version:
        import sys

        print(__version__)
        sys.exit(0)

    # Log to file
    if args.file:
        logging.basicConfig(filename=args.file, filemode="a", level=level)

    # No thread
    if args.nothread:
        os.environ["NOTHREAD"] = "1"

    # Run main App
    from .gui import windows

    try:
        root = windows.MainWindow(log_level=level)
        root.mainloop()
    except Exception:
        logger.exception("Failed to execute a gui window.")
