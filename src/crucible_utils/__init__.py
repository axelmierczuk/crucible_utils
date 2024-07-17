from __future__ import annotations
from importlib.metadata import version

__version__ = version("crucible_utils")

__all__ = [
    "api",
    "Challenges",
    "ChallengeService"
]

import crucible_utils.api as api
from crucible_utils.challenges import Challenges, ChallengeService
