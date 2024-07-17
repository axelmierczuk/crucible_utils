import os.path
from typing import List, Optional

import requests
from .models import APISettings, Paths, FlagData
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

    def query(self, data: str) -> FlagData:
        url = self._settings.challenge_url + Paths.SCORE.value
        submission = self._settings.score_submission(data=data).model_dump()
        headers = self._settings.authorization_header

        response = requests.post(url, headers=headers, json=submission)
        if response.status_code != 200:
            raise ResponseError(response.text)
        return FlagData(**response.json())

    def pull_artifacts(self, artifacts: List[str], overwrite: bool = True, base_directory: Optional[str] = None):
        location = ""
        if base_directory is not None:
            os.makedirs(base_directory, exist_ok=True)
            location = base_directory

        base_url = self._settings.crucible_url + Paths.ARTIFACT.value
        for artifact in artifacts:
            url = base_url + f"/{self._settings.challenge.replace('-', '_')}/{artifact}"
            headers = self._settings.authorization_header
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                file_path = os.path.join(location, artifact)
                if not overwrite and os.path.exists(file_path):
                    print(f"Will not be overwriting artifact {artifact}")
                    
                with open(file_path, "wb") as file:
                    file.write(response.content)
            else:
                print(f"Failed to download {artifact}")