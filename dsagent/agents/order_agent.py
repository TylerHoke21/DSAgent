from ..agent_manager import Agent

class OrderAgent(Agent):
    """Handles order fulfillment logic."""

    def __init__(self, supplier_api, *args, **kwargs):
        super().__init__(name="OrderAgent")
        self.supplier_api = supplier_api

    def run(self):
        # Placeholder: check for new orders and place with supplier
        print("Checking for new orders ...")
        print("Placing order with supplier (simulated)")
        return "orders processed"
