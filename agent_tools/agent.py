
"""
Day 2a: Agent Tools/Custom Function Tools.
A simple cat agent with two function tools.


"""

from google.adk.agents import Agent


def get_cat_age() -> int:
    """Return the cat's age."""
    return 4


def get_cat_name() -> str:
    """Return the cat's name."""
    return "Luna"


root_agent = Agent(
    name="CatAgent",
    model="gemini-3.5-flash-lite",
    instruction=(
        "You are a helpful cat assistant. "
        "Use the available tools to answer questions "
        "about the cat's name and age."
    ),
    tools=[get_cat_age, get_cat_name],
)
