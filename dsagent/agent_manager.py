import logging
from typing import List


class Agent:
    """Base class for all agents."""

    def __init__(self, name: str):
        self.name = name

    def run(self, *args, **kwargs):
        raise NotImplementedError


class AgentManager:
    """Coordinates multiple agents."""

    def __init__(self, agents: List[Agent], auto_mode: bool = False):
        self.agents = agents
        self.auto_mode = auto_mode

    def run_all(self):
        """Run all configured agents sequentially.

        Returns a list containing the result of each ``agent.run()`` call.  If
        execution is interrupted (for example when not running in ``auto`` mode
        and the user chooses to stop), only the results up to that point are
        returned.
        """

        results = []
        for agent in self.agents:
            logging.info("Running %s", agent.name)
            result = agent.run()
            results.append(result)
            if not self.auto_mode:
                cont = input(f"Continue after {agent.name}? (y/n) ").lower()
                if cont != "y":
                    print("Stopping execution per user request.")
                    break
        print("All agents complete.")
        return results
