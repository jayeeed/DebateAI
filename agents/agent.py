from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent
from agents.instructions import *

model_name = "gemini-2.5-flash"

pro_agent = LlmAgent(
    model=model_name,
    name="ProAgent",
    description="Argues in favor of the proposition",
    instruction=PRO_AGENT_INSTRUCTION,
    output_key="pro_argument",
)


con_agent = LlmAgent(
    model=model_name,
    name="ConAgent",
    description="Argues against the proposition",
    instruction=CON_AGENT_INSTRUCTION,
    output_key="con_argument",
)


debate_round = SequentialAgent(
    name="DebateRound",
    description="One round of debate with Pro and Con",
    sub_agents=[pro_agent, con_agent],
)


debate_loop = LoopAgent(
    name="DebateLoop",
    description="3 rounds of debate",
    max_iterations=3,
    sub_agents=[debate_round],
)


judge_agent = LlmAgent(
    model=model_name,
    name="JudgeAgent",
    description="Evaluates all debate rounds and declares a winner",
    instruction=JUDGE_AGENT_INSTRUCTION,
    output_key="verdict",
)


root_agent = SequentialAgent(
    name="DebateAI",
    description=DEBATE_AI_DESCRIPTION,
    sub_agents=[debate_loop, judge_agent],
)
