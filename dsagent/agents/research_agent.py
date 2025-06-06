from ..agent_manager import Agent


class ResearchAgent(Agent):
    """Performs product research using GPT."""

    def __init__(self, openai_client, *args, **kwargs):
        super().__init__(name="ResearchAgent")
        self.openai_client = openai_client

    def run(self):
        prompt = (
            "Suggest trending products for dropshipping on eBay. "
            "List top 5 ideas with brief justification."
        )
        response = self.openai_client.chat_completion(prompt)
        print("Research results:\n", response)
        return response
