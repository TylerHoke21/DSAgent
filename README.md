# DSAgent

DSAgent is a proof-of-concept framework for automating an eBay dropshipping
operation. It orchestrates multiple AI-powered agents to handle the
lifecycle of a storefront:

- **Product Research** – uses GPT to find trending products.
- **Listing Management** – generates listings for eBay.
- **Order Fulfillment** – places orders with a supplier (simulated).
- **Customer Support** – drafts responses to buyers.

Each agent can run autonomously or pause for human confirmation depending on
command line options. The `main.py` entry point wires together all agents.

This repo only provides skeleton code with placeholder API integrations. You
must supply real API keys and business logic for production use.

## Quick Start

```bash
pip install -r requirements.txt
python -m dsagent.main --auto  # run in autonomous mode
```
