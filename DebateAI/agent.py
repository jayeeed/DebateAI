from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent


# Pro Agent - Argues FOR the proposition
pro_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="ProAgent",
    description="Argues in favor of the proposition",
    instruction="""You are a skilled debater arguing FOR the proposition.
    Present strong, concise arguments supporting your position.
    Build on your previous arguments and counter the opposition's points.
    Be persuasive, use evidence and logic.
    Keep your response under 100 words.
    Do NOT include any meta-commentary about state or output.""",
    output_key="pro_argument",
)


# Con Agent - Argues AGAINST the proposition
con_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="ConAgent",
    description="Argues against the proposition",
    instruction="""You are a skilled debater arguing AGAINST the proposition.
    Present strong, concise arguments opposing the position.
    Build on your previous arguments and counter the opposition's points.
    Be persuasive, use evidence and logic.
    Keep your response under 100 words.
    Do NOT include any meta-commentary about state or output.""",
    output_key="con_argument",
)


# Debate Round - Pro then Con
debate_round = SequentialAgent(
    name="DebateRound",
    description="One round of debate with Pro and Con",
    sub_agents=[pro_agent, con_agent],
)


# Loop 3 rounds
debate_loop = LoopAgent(
    name="DebateLoop",
    description="3 rounds of debate",
    max_iterations=3,
    sub_agents=[debate_round],
)


# Judge Agent - Evaluates all 3 rounds and picks a winner
judge_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="JudgeAgent",
    description="Evaluates all debate rounds and declares a winner",
    instruction="""You are an impartial judge evaluating a 3-round debate.
    
    Review all rounds of arguments from both Pro and Con sides.
    
    Evaluate based on:
    1. Strength of logic and reasoning across all rounds
    2. Quality of evidence presented
    3. Effectiveness of rebuttals
    4. Persuasiveness of arguments
    
    Declare a clear winner (Pro or Con) and explain your reasoning in under 150 words.
    Format your response as:
    WINNER: [Pro/Con]
    REASONING: [Your detailed explanation]
    
    Do NOT include any meta-commentary about state or output.""",
    output_key="verdict",
)


# Debate Workflow - 3 rounds of debate then judge
debate_system = SequentialAgent(
    name="DebateAI",
    description="A 3-round debate system where two AI agents argue opposite sides and a judge picks the winner",
    sub_agents=[debate_loop, judge_agent],
)


# Root agent for easy access
root_agent = debate_system
