# Debate-AI Multi-Agent Orchestration

A multi-agent debate system built with Google ADK where two AI agents argue opposite sides of a topic and a judge declares the winner.

## ✨ Features

<img width="800" height="400" alt="mindmap" src="https://github.com/user-attachments/assets/6f44d9c6-3552-43c4-b284-910c573b54c7" />


- 🤖 **Three Core Agents:** Pro, Con, and Judge with loop-based repetition
- 🔁 **LoopAgent Pattern:** Elegant 3-round structure using iteration
- 🥊 **3-Round Debate:** Agents build arguments progressively across rounds
- 🔄 **Sequential Workflow:** Structured debate flow with automatic orchestration
- 💾 **Shared State:** Agents access previous arguments to build stronger cases
- 🆔 **UUID Generation:** Automatic unique IDs for isolated test runs
- 🎯 **Clean Output:** No meta-commentary, just debate content
- 📏 **Word Limits:** Concise responses (100 words per round, 150 for judge)
- 🔧 **Customizable:** Easy to modify topics, instructions, and models
- 🌐 **Cross-Platform:** Test scripts for Windows, Linux, and macOS

## 🎭 System Architecture

### Agents
The system uses **3 core agents** with a loop structure for efficient 3-round debate:

1. **ProAgent** - Argues FOR the proposition (runs 3 times)
2. **ConAgent** - Argues AGAINST the proposition (runs 3 times)
3. **JudgeAgent** - Evaluates all 3 rounds and declares winner

## 🚀 Quick Start

### Start ADK server (Built-in FastAPI)

```bash
adk api_server
```

### Running the Debate

**Python:**
```bash
python test_debate_api.py
```

## 📊 Example Output

```
🎭 Debate-AI System - API Test
=============================

👤 User ID: 84e67725-80cc-4d2d-9b28-ae78b6372210
🔑 Session ID: 9ca6a68f-5b5b-45b4-b207-862a9cd811c1

📝 Step 1: Creating session...
✅ Session created

🎤 Step 2: Starting debate...
Topic: Global warming is a real threat

==================================================

📊 Received 7 events from the debate system

==================================================
ROUND 1: OPENING STATEMENTS
==================================================

 🔵 PRO (Opening):
--------------------------------------------------
Global warming is unequivocally a real threat. The overwhelming scientific consensus, evidenced by NASA and the IPCC, confirms a rapidly warming planet driven by human activity. We are already witnessing devastating consequences: unprecedented extreme weather events, rising sea levels threatening coastal communities, and accelerating biodiversity loss. Ignoring these clear indicators jeopardizes future generations, demanding urgent action to mitigate catastrophic impacts.

 🔴 CON (Opening):
--------------------------------------------------
The proposition that global warming is an *existential* threat ignores crucial context. Earth's climate exhibits natural variability, with warming and cooling trends predating industrialization. Attributing all current climate phenomena solely to human activity overlooks significant solar, oceanic, and volcanic influences. While some warming is evident, historical data shows similar fluctuations, and the predicted catastrophic outcomes often rely on worst-case models. Prioritizing economically damaging policies over adaptation and acknowledging natural cycles is misguided, exaggerating a complex, multi-faceted environmental phenomenon into an unparalleled crisis.

==================================================
ROUND 2: REBUTTALS
==================================================

 🔵 PRO (Rebuttal):
--------------------------------------------------
While natural climate variability is real, it *cannot* explain the unprecedented *rate* and *magnitude* of current warming. Scientific models, accounting for all natural factors like solar and volcanic activity, conclusively demonstrate that anthropogenic greenhouse gas emissions are the dominant driver. Dismissing this overwhelming evidence and relying on historical natural fluctuations is a dangerous false equivalence. The real threat isn't the models, but the accelerating impacts we're already experiencing, demanding urgent mitigation alongside adaptation.

 🔴 CON (Rebuttal):
--------------------------------------------------
The assertion of an "unprecedented rate" often overlooks the limited temporal scope of precise instrumental records, while paleoclimate data reveals significant, rapid shifts pre-dating human industrialization. Scientific models, despite their utility, contain inherent uncertainties and are sensitive to parameters like climate sensitivity, which remains a subject of active debate. Attributing warming solely to human activity as the "dominant driver" oversimplifies Earth's complex, multifactorial climate system. Dismissing natural variability as a "false equivalence" risks ignoring fundamental climatic dynamics, promoting alarmism and potentially misguided, economically detrimental policies based on an incomplete picture rather than comprehensive scientific consensus.

==================================================
ROUND 3: CLOSING STATEMENTS
==================================================

 🔵 PRO (Closing):
--------------------------------------------------
Paleoclimate data reveals past changes, but the *current* warming trend, especially over the last century, is unequivocally *unprecedented in its speed and global synchronicity*, directly correlating with anthropogenic greenhouse gas emissions. While models have uncertainties, their robust, converging results across diverse scientific institutions confirm human activity as the **dominant driver**. Focusing on model "minutiae" or past natural cycles to dismiss this overwhelming evidence is a dangerous distraction from the very real and escalating threat demanding urgent, informed action, not further debate on settled science.

 🔴 CON (Closing):
--------------------------------------------------
The claim of "unprecedented speed and global synchronicity" oversimplifies paleoclimate data, whose resolution often masks past rapid, localized shifts. To declare science "settled" on such a complex system like Earth's climate disregards the continuous evolution of scientific understanding and inherent model limitations, particularly concerning long-term predictions and climate sensitivity. Labeling legitimate scientific inquiry into these uncertainties as "distractions" stifles critical analysis. Focusing solely on anthropogenic drivers as the undisputed cause, while dismissing other natural influences, risks promoting a narrow, alarmist agenda that could lead to economically damaging, ineffective policies based on an incomplete and potentially exaggerated threat assessment.

==================================================
FINAL VERDICT
==================================================

 ⚖️  JUDGE:
--------------------------------------------------
WINNER: Pro
REASONING: Pro consistently presented a strong case, emphasizing the unprecedented *rate* and *magnitude* of current warming directly attributable to human activity, supported by overwhelming scientific consensus from diverse institutions. While Con effectively introduced the complexities of natural variability and model uncertainties, it struggled to provide compelling counter-evidence demonstrating that these factors *dominate* the current warming or that it is *not* unprecedented in its speed and global synchronicity. Pro effectively rebutted by clarifying that models *do* account for natural influences, reinforcing human activity as the dominant driver, making its argument more persuasive and logically consistent.


🏁 Debate Complete!
==================
```

## 🎯 Customizing Debate Topics

Edit the debate topic in any script:

**Python:**
```python
"text": "Debate topic: YOUR TOPIC HERE"
```

**Batch/Shell:**
```bash
"text": "Debate topic: YOUR TOPIC HERE"
```

### Example Topics
- "Remote work is better than office work"
- "Social media harms society more than it helps"
- "Nuclear energy is the best climate solution"
- "Universal basic income should be implemented"
- "Space exploration is worth the cost"

## 📁 Project Structure

```
.
├── DebateAI/
│   ├── agent.py               # Multi-agent system definition
│   └── __init__.py            # Package initialization
├── .env                       # Environment variables (API keys)
├── .gitignore                 # Git ignore file
├── test_debate_api.py         # Python test script
└── README.md                  # This file
```

## 🔧 API Endpoints Used

### 1. Create Session
```http
POST /apps/{appName}/users/{userId}/sessions/{sessionId}
```
---

### 2. Run Debate
```http
POST /run
Content-Type: application/json

{
  "appName": "agents",
  "userId": "{uuid}",
  "sessionId": "{uuid}",
  "newMessage": {
    "role": "user",
    "parts": [
      {"text": "Debate topic: {your topic here}"}
    ]
  }
}
```
