"""Academic_websearch_agent for finding research papers using search tools."""

from google.adk.agents import Agent
from . import prompt

MODEL = "gemma-3-12b-it"

academic_websearch_agent = Agent(
    model=MODEL,
    name="academic_websearch_agent",
    description="Searches for recent academic papers citing a given seminal paper",
    instruction=prompt.ACADEMIC_WEBSEARCH_PROMPT,
)