from enum import Enum
from pydantic import BaseModel

_BASE_DOMAIN = "crucible.dreadnode.io"


class ChallengeSubmission(BaseModel):
    challenge: str
    flag: str


class ScoreSubmission(BaseModel):
    data: str


class FlagData(BaseModel):
    flag: str


class APISettings(BaseModel):
    key: str
    base_domain: str = _BASE_DOMAIN
    challenge: str

    @property
    def challenge_url(self) -> str:
        return f"https://{self.challenge}.{self.base_domain}"

    @property
    def crucible_url(self) -> str:
        return f"https://{self.base_domain}"

    @property
    def authorization_header(self) -> dict:
        return {"Authorization": self.key}

    def challenge_submission(self, flag: str) -> ChallengeSubmission:
        return ChallengeSubmission(challenge=self.challenge.replace("-", "_"), flag=flag)

    def score_submission(self, data: str) -> ScoreSubmission:
        return ScoreSubmission(data=data)


class Paths(Enum):
    SCORE = "/score"
    SUBMIT = "/api/submit-flag"
    ARTIFACT = "/api/artifacts"
