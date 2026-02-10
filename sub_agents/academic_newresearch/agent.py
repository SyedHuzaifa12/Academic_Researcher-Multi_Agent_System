"""Academic_newresearch_agent for finding new research lines."""

from google.adk.agents import Agent
from . import prompt

MODEL = "gemma-3-12b-it"

academic_newresearch_agent = Agent(
    model=MODEL,
    name="academic_newresearch_agent",
    description="Suggests future research directions based on seminal and recent papers",
    instruction=prompt.ACADEMIC_NEWRESEARCH_PROMPT,
)