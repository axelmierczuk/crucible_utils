# Crucible Utils

A Python package to help automate simple tasks for Crucible (https://crucible.dreadnode.io/).

## Installation 

```bash
pip install git+https://github.com/axelmierczuk/crucible_utils.git@main
```

## Usage

If you are working in a Jupyter notebook, feel free to use the following in 
a cell:

```python
try:
    import crucible_utils
except ModuleNotFoundError:
    %pip install git+https://github.com/axelmierczuk/crucible_utils.git@main
    raise Exception("Restart your kernel!")

KEY = "<EXAMPLE>"
CHALLENGE = crucible_utils.Challenges.BEAR_1

service = crucible_utils.ChallengeService(key=KEY, challenge=CHALLENGE)
```

Each field in the `crucible_utils.Challenges` enum has the following structure:

```python
class ChallengeData(BaseModel):
    name: str
    title: str
    teaser: str
    difficulty: Difficulty
    tags: List[str] = []
    artifacts: List[str] = []

    @property
    def formatted_name(self) -> str:
        return self.name.replace("_", "-")

    @property
    def url(self) -> str:
        return f"https://crucible.dreadnode.io/challenges/{self.formated_name}"
```

which makes access accessing metadata straightforward. For exmaple:

```python
import crucible_utils

challenge = crucible_utils.Challenges.BEAR_1

print("Challenge Artifacts:", challenge.value.artifacts)
```

### Example - Query and Submit Flag

```python
import crucible_utils
KEY = "<EXAMPLE>"
CHALLENGE = crucible_utils.Challenges.BEAR_1

service = crucible_utils.ChallengeService(key=KEY, challenge=CHALLENGE)

response = service.query({"data": "help?"})
service.submit_flag(flag=response.flag)
```

### Example - Pull Artifacts

```python
import crucible_utils
KEY = "<EXAMPLE>"
CHALLENGE = crucible_utils.Challenges.BEAR_1

service = crucible_utils.ChallengeService(key=KEY, challenge=CHALLENGE)
service.pull_artifacts(base_directory=f"data/{CHALLENGE.value.formatted_name}", overwrite=False)
```

The `ChallengeService` has the following functions available:

| Function         | Description                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `submit_flag`    | Takes a `flag` as input and returns a boolean based on the response from the server. May raise a `ResponseError` exception for invalid responses from the server.                                                                                                                                       |
| `query`          | Takes some `data` as input and returns `FlagData` based on the response from the server. May raise a `ResponseError` exception for invalid responses from the server.                                                                                                                                   |
| `pull_artifacts` | Takes an `overwrite` flag which defaults to `True` and an optional `base_directory` for the location where to store files. Downloads and saves files to the current directory unless `base_directory` is defined, and will only write files if `overwrite` is `True` or if the file does not exist yet. |

### Example - Print all Challenges


```python
import crucible_utils

crucible_utils.Challenges.show_challenges()
```


## Available Challenges

| Challenge                                                                                       | Teaser                                                |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [Bear 1 - Data Exploration](https://crucible.dreadnode.io/challenges/bear1)                     | What is the bear data trying to tell us?              |
| [Bear 2 - Model Extraction](https://crucible.dreadnode.io/challenges/bear2)                     | What does it take to reverse a basic model?           |
| [Bear 3 - Model Fingerprinting](https://crucible.dreadnode.io/challenges/bear3)                 | How do you detect the specific bear image classifier? |
| [Bear 4 - Prompt Injection](https://crucible.dreadnode.io/challenges/bear4)                     | Can you get the LLM to reveal the true bear name?     |
| [Brig 1 - Escape the Classifier](https://crucible.dreadnode.io/challenges/brig1)                | Maybe giving LLMs access to bash was a bad idea?      |
| [Brig 2 - Escape the Summarizer](https://crucible.dreadnode.io/challenges/brig2)                | What happens when LLMs make web requests?             |
| [Cluster 1 - Misclassification](https://crucible.dreadnode.io/challenges/cluster1)              | Can you find the misclasification?                    |
| [Cluster 2 - Clustering](https://crucible.dreadnode.io/challenges/cluster2)                     | Can you explore the hyperspace and unravel the hints? |
| [Cluster 3 - Hyperspace](https://crucible.dreadnode.io/challenges/cluster3)                     | Can you go to the end of hyperspace?                  |
| [Count - MNIST](https://crucible.dreadnode.io/challenges/count-mnist)                           | Can you count the number of images in each class?     |
| [Granny - Adversarial Images](https://crucible.dreadnode.io/challenges/granny)                  | Can you hide your true identity?                      |
| [Granny 2 - Adversarial JPGs](https://crucible.dreadnode.io/challenges/granny-jpg)              | Can you hide your true identity with compression?     |
| [Guess Who's Back - Data Analysis](https://crucible.dreadnode.io/challenges/guess-whos-back)    | Can you guess who's back?                             |
| [Hush - Audio Generation](https://crucible.dreadnode.io/challenges/hush)                        | Can you discover the hidden audio passphrase?         |
| [Inversion - Invert the Model](https://crucible.dreadnode.io/challenges/inversion)              | Can you invert the image?                             |
| [Passphrase - Adversarial Semantics](https://crucible.dreadnode.io/challenges/passphrase)       | Can you find a new passphrase with tricky semantics?  |
| [Pickle - Malicious Blobs](https://crucible.dreadnode.io/challenges/pickle)                     | Can you pop a shell bro?                              |
| [Pirate Flag - RAG Escape](https://crucible.dreadnode.io/challenges/pirate-flag)                | Can you break free from the context?                  |
| [Pixelated - Adversarial OCR](https://crucible.dreadnode.io/challenges/pixelated)               | Can you break some OCR for admin?                     |
| [Puppeteer 1 - Basic Prompting](https://crucible.dreadnode.io/challenges/puppeteer1)            | How good are you at following instructions?           |
| [Puppeteer 2 - Restricted Prompting](https://crucible.dreadnode.io/challenges/puppeteer2)       | How good are you at telling instructions?             |
| [Puppeteer 3 - Limited Prompting](https://crucible.dreadnode.io/challenges/puppeteer3)          | How good are you at condensing instructions?          |
| [Puppeteer 4 - Tricky Prompting](https://crucible.dreadnode.io/challenges/puppeteer4)           | How good are you at cheating instructions?            |
| [Semantle - One Word](https://crucible.dreadnode.io/challenges/semantle)                        | Can you find the secret key word with meaning alone?  |
| [Semantle 2 - Phrase](https://crucible.dreadnode.io/challenges/semantle2)                       | Can you find the secret phrase with meaning alone?    |
| [Spanglish - Escape the Translator](https://crucible.dreadnode.io/challenges/spanglish)         | Que es la bandera?                                    |
| [Test - Confirm API Access](https://crucible.dreadnode.io/challenges/test)                      | Can you make an API request?                          |
| [What is the Flag 1 - Basic](https://crucible.dreadnode.io/challenges/whatistheflag)            | Can you steal the flag from an LLM?                   |
| [What is the Flag 2 - Blocked Words](https://crucible.dreadnode.io/challenges/whatistheflag2)   | Can you steal the flag from an LLM?                   |
| [What is the Flag 3 - Identity Crisis](https://crucible.dreadnode.io/challenges/whatistheflag3) | Can you steal the flag from an LLM?                   |
| [What is the Flag 4 - Guarded](https://crucible.dreadnode.io/challenges/whatistheflag4)         | Can you steal the flag from an LLM?                   |
| [What is the Flag 5 - Safety First](https://crucible.dreadnode.io/challenges/whatistheflag5)    | Can you steal the flag from an LLM?                   |
| [What is the Flag 6 - Safety Second](https://crucible.dreadnode.io/challenges/whatistheflag6)   | Can you steal the flag from an LLM?                   |
| [What's my IP - RAG Escape](https://crucible.dreadnode.io/challenges/whats-my-ip)               | Can you trick some new AI DNS?                        |
| [What's my IP 2 - No Bruno](https://crucible.dreadnode.io/challenges/whats-my-ip2)              | Can you trick some even newer AI DNS?                 |
