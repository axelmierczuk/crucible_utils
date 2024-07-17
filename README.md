# Crucible Utils

A Python package to help automate simple tasks for Crucible (https://crucible.dreadnode.io/).

## Installation 

```bash
pip install git+https://github.com/axelmierczuk/crucible_utils.git
```

## Usage

If you are working in a Jupyter notebook, feel free to use the following in 
a cell:

```python
try:
    import crucible_utils
except Exception as e:
    %pip install git+https://github.com/axelmierczuk/crucible_utils.git
    raise Exception("Restart your kernel!")

CRUCIBLE_API_KEY = "<EXAMPLE>"
CHALLENGE = "test"

settings = crucible_utils.api.APISettings(key=CRUCIBLE_API_KEY, challenge=CHALLENGE)
service = crucible_utils.api.APIService(settings=settings)
```

As seen in the example above, there's two main components, settings and service.

Settings takes the following parameters:

| Field         | Type   | Required | Default                 |
|---------------|--------|----------|-------------------------|
| `key`         | string | Yes      | N/a                     |
| `challenge`   | string | Yes      | N/a                     |
| `base_domain` | string | No       | "crucible.dreadnode.io" |

The service has the following functions available:

| Function         | Description                                                                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `submit_flag`    | Takes a `flag` as input and returns a boolean based on the response from the server. May raise a `ResponseError` exception for invalid responses from the server.                                                                                                                                                                          |
| `query`          | Takes some `data` as input and returns `FlagData` based on the response from the server. May raise a `ResponseError` exception for invalid responses from the server.                                                                                                                                                                      |
| `pull_artifacts` | Takes a list of file name (`artifacts`), an `overwrite` flag which defaults to `True` and an optional `base_directory` for the location where to store files. Downloads and saves files to the current directory unless `base_directory` is defined, and will only write files if `overwrite` is `True` or if the file does not exist yet. |

## Examples

### Query and Submit Flag

```python
import crucible_utils

CRUCIBLE_API_KEY = "<EXAMPLE>"
CHALLENGE = "example"

settings = crucible_utils.api.APISettings(key=CRUCIBLE_API_KEY, challenge=CHALLENGE)
service = crucible_utils.api.APIService(settings=settings)

response = service.query("help?")
service.submit_flag(flag=response.flag)
```

### Pull Artifacts

```python
import crucible_utils

CRUCIBLE_API_KEY = "<EXAMPLE>"
CHALLENGE = "example"
ARTIFACT_FILES = ["example.csv"]

settings = crucible_utils.api.APISettings(key=CRUCIBLE_API_KEY, challenge=CHALLENGE)
service = crucible_utils.api.APIService(settings=settings)

service.pull_artifacts(artifacts=ARTIFACT_FILES, base_directory=f"data/{CHALLENGE}", overwrite=False)
```
