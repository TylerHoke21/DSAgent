"""Simple orchestration script for DSAgent."""
import logging
from .openai_client import OpenAIClient
from .ebay_api import EbayAPI
from .supplier_api import SupplierAPI
from .agent_manager import AgentManager
from .agents.research_agent import ResearchAgent
from .agents.listing_agent import ListingAgent
from .agents.order_agent import OrderAgent
from .agents.support_agent import SupportAgent


def main(auto: bool = False):
    logging.basicConfig(level=logging.INFO)
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
