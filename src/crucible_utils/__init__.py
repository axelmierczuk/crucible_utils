from __future__ import annotations
from importlib.metadata import version

__version__ = version("ctf_utils")

__all__ = [
    "api",
]

import crucible_utils.api as api
