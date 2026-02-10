"""Academic_Research: Research advice, related literature finding, research area proposals."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
from .sub_agents.academic_newresearch.agent import academic_newresearch_agent
from .sub_agents.academic_websearch.agent import academic_websearch_agent

MODEL = "gemma-3-12b-it"

academic_coordinator = Agent(
    name="academic_coordinator",
    model=MODEL,
    description=( "Analyzing seminal papers provided by users, "
        "providing research advice, locating current papers "
        "relevant to the seminal paper, generating suggestions "
        "for new research directions, and accessing web resources "
        "to acquire knowledge"
    ),
    instruction=prompt.ACADEMIC_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=academic_websearch_agent),
        AgentTool(agent=academic_newresearch_agent),
    ],
)

root_agent = academic_coordinator