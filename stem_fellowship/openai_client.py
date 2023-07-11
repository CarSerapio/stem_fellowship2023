import os
import json
import openai

class OpenAIClient:
    def __init__(self, config_path: str = "config.json"):
        self.api_key = self.load_api_key(config_path)
        openai.api_key = self.api_key

    @staticmethod
    def load_api_key(config_path: str):
        with open(config_path) as f:
            config = json.load(f)
        api_key = config.get('openai_api_key')
        env_api_key = os.getenv("OPENAI_API_KEY")
        if env_api_key is not None:
            api_key = env_api_key
        return api_key