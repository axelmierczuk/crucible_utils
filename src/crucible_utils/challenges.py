from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
import crucible_utils.api as api
from crucible_utils.api.models import FlagData


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class ChallengeData(BaseModel):
    name: str
    title: str
    teaser: str
    difficulty: Difficulty
    tags: List[str] = []
    artifacts: List[str] = []

    def info(self):
        print("Title:", self.title)
        print("Teaser:", self.teaser)
        print("Difficulty:", self.difficulty.value)
        print("Tags:", ", ".join(self.tags))
        if len(self.artifacts) != 0:
            print("Artifacts:", ", ".join(self.artifacts))

    @property
    def formatted_name(self) -> str:
        return self.name.replace("_", "-")

    @property
    def url(self) -> str:
        return f"https://crucible.dreadnode.io/challenges/{self.formated_name}"


class Challenges(Enum):
    BEAR_1 = ChallengeData(name="bear1", title="Bear 1 - Data Exploration", teaser="What is the bear data trying to tell us?", difficulty=Difficulty.EASY, tags=["data"], artifacts=["bear.csv"])
    BEAR_2 = ChallengeData(name="bear2", title="Bear 2 - Model Extraction", teaser="What does it take to reverse a basic model?", difficulty=Difficulty.EASY, tags=["data"], artifacts=[])
    BEAR_3 = ChallengeData(name="bear3", title="Bear 3 - Model Fingerprinting", teaser="How do you detect the specific bear image classifier?", difficulty=Difficulty.EASY, tags=["model fingerprinting"], artifacts=["brown_bear.png"])
    BEAR_4 = ChallengeData(name="bear4", title="Bear 4 - Prompt Injection", teaser="Can you get the LLM to reveal the true bear name?", difficulty=Difficulty.EASY, tags=["intro", "llm", "prompt", "engineering"], artifacts=[])
    
    BRIG_1 = ChallengeData(name="brig1", title="Brig 1 - Escape the Classifier", teaser="Maybe giving LLMs access to bash was a bad idea?", difficulty=Difficulty.MEDIUM, tags=["llm", "escape"], artifacts=[])
    BRIG_2 = ChallengeData(name="brig2", title="Brig 2 - Escape the Summarizer", teaser="What happens when LLMs make web requests?", difficulty=Difficulty.MEDIUM, tags=["llm", "escape"], artifacts=[])
    
    CLUSTER_1 = ChallengeData(name="cluster1", title="Cluster 1 - Misclassification", teaser="Can you find the misclasification?", difficulty=Difficulty.MEDIUM, tags=["DEFCON-31"], artifacts=["census_full_data.csv", "census_model.skops"])
    CLUSTER_2 = ChallengeData(name="cluster2", title="Cluster 2 - Clustering", teaser="Can you explore the hyperspace and unravel the hints?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=["data.npz"])
    CLUSTER_3 = ChallengeData(name="cluster3", title="Cluster 3 - Hyperspace", teaser="Can you go to the end of hyperspace?", difficulty=Difficulty.HARD, tags=["DEFCON-31"], artifacts=["data.npz"])
    
    COUNT = ChallengeData(name="count_mnist", title="Count - MNIST", teaser="Can you count the number of images in each class?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    
    GRANNY = ChallengeData(name="granny", title="Granny - Adversarial Images", teaser="Can you hide your true identity?", difficulty=Difficulty.MEDIUM, tags=["DEFCON-31"], artifacts=["reference.png"])
    GRANNY_2 = ChallengeData(name="granny_jpg", title="Granny 2 - Adversarial JPGs", teaser="Can you hide your true identity with compression?", difficulty=Difficulty.HARD, tags=["DEFCON-31"], artifacts=["reference.png"])
    
    GUESS_WHOS_BACK = ChallengeData(name="guess_whos_back", title="Guess Who's Back - Data Analysis", teaser="Can you guess who's back?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=["terrence.npz"])
    
    HUSH = ChallengeData(name="hush", title="Hush - Audio Generation", teaser="Can you discover the hidden audio passphrase?", difficulty=Difficulty.MEDIUM, tags=["DEFCON-31"], artifacts=["test_noise.wav"])
    
    INVERSION = ChallengeData(name="inversion", title="Inversion - Invert the Model", teaser="Can you invert the image?", difficulty=Difficulty.HARD, tags=["DEFCON-31"], artifacts=[])
    
    PASSPHRASE = ChallengeData(name="passphrase", title="Passphrase - Adversarial Semantics", teaser="Can you find a new passphrase with tricky semantics?", difficulty=Difficulty.HARD, tags=["DEFCON-31"], artifacts=[])
    
    PICKLE = ChallengeData(name="pickle", title="Pickle - Malicious Blobs", teaser="Can you pop a shell bro?", difficulty=Difficulty.HARD, tags=["DEFCON-31"], artifacts=[])
    
    PIRATE_FLAG = ChallengeData(name="pirate_flag", title="Pirate Flag - RAG Escape", teaser="Can you break free from the context?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    
    PIXELATED = ChallengeData(name="pixelated", title="Pixelated - Adversarial OCR", teaser="Can you break some OCR for admin?", difficulty=Difficulty.HARD, tags=["DEFCON-31"], artifacts=["reference.png"])
    
    PUPPETEER_1 = ChallengeData(name="puppeteer1", title="Puppeteer 1 - Basic Prompting", teaser="How good are you at following instructions?", difficulty=Difficulty.EASY, tags=["llm"], artifacts=[])
    PUPPETEER_2 = ChallengeData(name="puppeteer2", title="Puppeteer 2 - Restricted Prompting", teaser="How good are you at telling instructions?", difficulty=Difficulty.EASY, tags=["llm"], artifacts=[])
    PUPPETEER_3 = ChallengeData(name="puppeteer3", title="Puppeteer 3 - Limited Prompting", teaser="How good are you at condensing instructions?", difficulty=Difficulty.MEDIUM, tags=["llm"], artifacts=[])
    PUPPETEER_4 = ChallengeData(name="puppeteer4", title="Puppeteer 4 - Tricky Prompting", teaser="How good are you at cheating instructions?", difficulty=Difficulty.MEDIUM, tags=["llm"], artifacts=[])
    
    SEMANTLE = ChallengeData(name="semantle", title="Semantle - One Word", teaser="Can you find the secret key word with meaning alone?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    SEMANTLE_2 = ChallengeData(name="semantle2", title="Semantle 2 - Phrase", teaser="Can you find the secret phrase with meaning alone?", difficulty=Difficulty.MEDIUM, tags=["DEFCON-31"], artifacts=[])
    
    SPANGLISH = ChallengeData(name="spanglish", title="Spanglish - Escape the Translator", teaser="Que es la bandera?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    TEST = ChallengeData(name="test", title="Test - Confirm API Access", teaser="Can you make an API request?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    
    WHAT_IS_THE_FLAG_1 = ChallengeData(name="whatistheflag", title="What is the Flag 1 - Basic", teaser="Can you steal the flag from an LLM?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    WHAT_IS_THE_FLAG_2 = ChallengeData(name="whatistheflag2", title="What is the Flag 2 - Blocked Words", teaser="Can you steal the flag from an LLM?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    WHAT_IS_THE_FLAG_3 = ChallengeData(name="whatistheflag3", title="What is the Flag 3 - Identity Crisis", teaser="Can you steal the flag from an LLM?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    WHAT_IS_THE_FLAG_4 = ChallengeData(name="whatistheflag4", title="What is the Flag 4 - Guarded", teaser="Can you steal the flag from an LLM?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    WHAT_IS_THE_FLAG_5 = ChallengeData(name="whatistheflag5", title="What is the Flag 5 - Safety First", teaser="Can you steal the flag from an LLM?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    WHAT_IS_THE_FLAG_6 = ChallengeData(name="whatistheflag6", title="What is the Flag 6 - Safety Second", teaser="Can you steal the flag from an LLM?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    
    WHATS_MY_IP = ChallengeData(name="whats_my_ip", title="What's my IP - RAG Escape", teaser="Can you trick some new AI DNS?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])
    WHATS_MY_IP_2 = ChallengeData(name="whats_my_ip2", title="What's my IP 2 - No Bruno", teaser="Can you trick some even newer AI DNS?", difficulty=Difficulty.EASY, tags=["DEFCON-31"], artifacts=[])

    @classmethod
    def show_challenges(cls):
        for challenge in list(cls):
            challenge.value.info()
            print()


class ChallengeService:
    def __init__(self, key: str, challenge: Challenges):
        self._challenge = challenge
        self._settings = api.APISettings(key=key, challenge=challenge.value.formatted_name)
        self._service = api.APIService(settings=self._settings)

    def submit_flag(self, flag: str) -> bool:
        return self._service.submit_flag(flag=flag)

    def query(self, data: str) -> FlagData:
        return self._service.query(data=data)

    def pull_artifacts(self, overwrite: bool = True, base_directory: Optional[str] = None):
        return self._service.pull_artifacts(self._challenge.value.artifacts, overwrite=overwrite, base_directory=base_directory)


