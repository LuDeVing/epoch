"""`python -m harness.think ...`: forward to the driver in harness/think.py (see __init__.py)."""
import sys

from . import load_driver

sys.exit(load_driver().main())
