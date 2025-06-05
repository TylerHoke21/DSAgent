"""Thin wrapper around OpenAI API calls."""
from typing import Any
import os

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None

class OpenAIClient:
    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if openai:
            openai.api_key = self.api_key
        self.model = model

    def chat_completion(self, prompt: str) -> Any:
        if not openai:
            return "(OpenAI library not installed)"  # placeholder
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"]
