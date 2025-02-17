import os.path
from typing import List, Optional

import requests
from .models import APISettings, Paths, SubmissionType
from .exceptions import ResponseError


class APIService:
    def __init__(self, settings: APISettings):
        self._settings = settings

    def submit_flag(self, flag: str) -> bool:
        url = self._settings.crucible_url + Paths.SUBMIT.value
        submission = self._settings.challenge_submission(flag=flag).model_dump()
        headers = self._settings.authorization_header

        response = requests.post(url, headers=headers, json=submission)
        if response.status_code != 200:
            raise ResponseError(response.text)
        return response.json().get("correct")

    def query(self, data: SubmissionType):
        url = self._settings.challenge_url + Paths.SCORE.value
        headers = self._settings.authorization_header
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            raise ResponseError(response.text)
        return response.json()

    def pull_artifacts(self, artifacts: List[str], overwrite: bool = True, base_directory: Optional[str] = None):
        location = ""
        if base_directory is not None:
            os.makedirs(base_directory, exist_ok=True)
            location = base_directory

        base_url = self._settings.crucible_url + Paths.ARTIFACT.value
        for artifact in artifacts:
            file_path = os.path.join(location, artifact)
            if overwrite or not os.path.exists(file_path):
                url = base_url + f"/{self._settings.challenge.replace('-', '_')}/{artifact}"
                headers = self._settings.authorization_header
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    with open(file_path, "wb") as file:
                        file.write(response.content)
                else:
                    print(f"Failed to download {artifact}")
            else:
                print(f"Will not be overwriting artifact {artifact}")
