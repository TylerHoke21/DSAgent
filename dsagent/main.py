"""Simple orchestration script for DSAgent."""
from .openai_client import OpenAIClient
from .ebay_api import EbayAPI
from .supplier_api import SupplierAPI
from .agent_manager import AgentManager
from .agents.research_agent import ResearchAgent
from .agents.listing_agent import ListingAgent
from .agents.order_agent import OrderAgent
from .agents.support_agent import SupportAgent


def main(auto: bool = False):
    openai_client = OpenAIClient()
    ebay_api = EbayAPI()
    supplier_api = SupplierAPI()

    agents = [
        ResearchAgent(openai_client),
        ListingAgent(openai_client, ebay_api),
        OrderAgent(supplier_api),
        SupportAgent(openai_client),
    ]
    manager = AgentManager(agents, auto_mode=auto)
    results = manager.run_all()

    # Display results when not running in fully autonomous mode so the user can
    # review what each agent produced.  In auto mode the agents themselves may
    # print output, so showing the collected list is optional.
    if not auto:
        print("Run results:")
        for res in results:
            print(res)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run DSAgent")
    parser.add_argument("--auto", action="store_true", help="Run without prompts")
    args = parser.parse_args()
    main(auto=args.auto)
