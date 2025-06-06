"""Simple orchestration script for DSAgent."""

from .agent_manager import AgentManager
from .agents.listing_agent import ListingAgent
from .agents.order_agent import OrderAgent
from .agents.research_agent import ResearchAgent
from .agents.support_agent import SupportAgent
from .ebay_api import EbayAPI
from .openai_client import OpenAIClient
from .supplier_api import SupplierAPI


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
    manager.run_all()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run DSAgent")
    parser.add_argument("--auto", action="store_true", help="Run without prompts")
    args = parser.parse_args()
    main(auto=args.auto)
