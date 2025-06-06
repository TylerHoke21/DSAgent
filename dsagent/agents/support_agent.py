from ..agent_manager import Agent


class SupportAgent(Agent):
    """Handles customer support inquiries."""

    def __init__(self, openai_client, *args, **kwargs):
        super().__init__(name="SupportAgent")
        self.openai_client = openai_client

    def run(self):
        # Placeholder: respond to a sample customer inquiry
        inquiry = "Where is my order?"
        prompt = (
            f"You are a helpful eBay seller. Answer the customer question:\n{inquiry}"
        )
        response = self.openai_client.chat_completion(prompt)
        print("Customer response:\n", response)
        return response
