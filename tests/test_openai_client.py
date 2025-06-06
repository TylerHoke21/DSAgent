import types
from unittest import mock
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dsagent.openai_client import OpenAIClient


def test_chat_completion_without_openai():
    with mock.patch('dsagent.openai_client.openai', None):
        client = OpenAIClient()
        assert client.chat_completion('hello') == '(OpenAI library not installed)'


def test_chat_completion_api_key_not_configured():
    # Create a fake openai module exposing an OpenAI attribute
    dummy_openai = types.SimpleNamespace(OpenAI=object)
    with mock.patch('dsagent.openai_client.openai', dummy_openai):
        with mock.patch.dict('os.environ', {}, clear=True):
            client = OpenAIClient(api_key=None)
            assert client.chat_completion('hi') == '(OpenAI API key not configured)'
