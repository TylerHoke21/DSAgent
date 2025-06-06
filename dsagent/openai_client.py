"""Thin wrapper around OpenAI API calls."""
from typing import Any
import os

try:
    import openai
except ImportError:  # pragma: no cover
    openai = None  # type: ignore


class OpenAIClient:
    """Simple client to interact with the OpenAI chat completion API."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model

        # The OpenAI Python library changed its interface starting in v1.0.
        # Newer versions expose an ``OpenAI`` class for creating clients while
        # older versions rely on global configuration.  Support both so that the
        # rest of the code works regardless of the installed package version.
        self._client = None
        if openai:
            if hasattr(openai, "OpenAI"):
                # Newer 1.x style client. Only instantiate when an API key is
                # available; otherwise calls will fail.  The client will remain
                # ``None`` and calls will fall back to returning a placeholder.
                if self.api_key:
                    self._client = openai.OpenAI(api_key=self.api_key)
            else:  # pragma: no cover - old API path
                openai.api_key = self.api_key

    def chat_completion(self, prompt: str) -> Any:
        """Return the assistant response for ``prompt`` using the chat API."""

        if not openai:
            # Library missing; return a placeholder so the rest of the program
            # can continue running.
            return "(OpenAI library not installed)"

        messages = [{"role": "user", "content": prompt}]

        if self._client is not None:
            # 1.x API
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return response.choices[0].message.content

        if hasattr(openai, "OpenAI"):
            # openai>=1.0.0 but no API key configured
            return "(OpenAI API key not configured)"

        # 0.x API (deprecated but still supported for compatibility)
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        return response.choices[0].message["content"]
