# Debate-AI Multi-Agent Orchestration

A multi-agent debate system built with Google ADK where two AI agents argue opposite sides of a topic and a judge declares the winner.

## ✨ Features

<img width="800" height="400" alt="mindmap" src="https://github.com/user-attachments/assets/6f44d9c6-3552-43c4-b284-910c573b54c7" />


- 🤖 **Three Core Agents:** Pro, Con, and Judge with loop-based repetition
- 🔁 **LoopAgent Pattern:** Elegant 3-round structure using iteration
- 🥊 **3-Round Debate:** Agents build arguments progressively across rounds
- 💾 **Shared State:** Agents access previous arguments to build stronger cases
- 🔧 **Customizable:** Easy to modify topics, instructions, and models

## 🎭 System Architecture

### Agents
The system uses **3 core agents** with a loop structure for efficient 3-round debate:

1. **ProAgent** - Argues FOR the proposition (runs 3 times)
2. **ConAgent** - Argues AGAINST the proposition (runs 3 times)
3. **JudgeAgent** - Evaluates all 3 rounds and declares winner

## 🚀 Quick Start

### Install Dependencies

```bash
python -m venv .venv
.venv\Scripts\activate # for linux: `source .venv/bin/activate`
pip install -r requirements.txt
```

### Start ADK Web UI (Default: http://127.0.0.1:8000)

```bash
adk web
```

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

👤 User ID: 738e4e4a-185a-4707-8200-14e330d161e1
🔑 Session ID: 43c4e9b5-8884-4762-be2b-9f38a9dc6547

📝 Step 1: Creating session...
✅ Session created

🎤 Step 2: Starting debate...
Topic: Global warming is a hoax

==================================================

📊 Received 7 events from the debate system

==================================================
ROUND 1: OPENING STATEMENTS
==================================================

 🔵 PRO (Opening):
--------------------------------------------------
The "global warming" narrative misrepresents natural climate fluctuations. Earth's climate has always changed; current warming is part of these cyclical patterns, not unprecedented. Crucially, raw temperature data often undergoes significant "adjustments" by agencies, frequently increasing past warming to fit an alarming narrative. This manipulation, combined with failed predictions and obvious political opportunism, exposes the fabricated crisis for what it truly is: a well-orchestrated hoax.

 🔴 CON (Opening):
--------------------------------------------------
The argument for "natural climate fluctuations" ignores the unprecedented speed and scale of current warming, demonstrably linked to human activity. "Data adjustments" are standard scientific procedures for accuracy, not manipulation; *multiple independent agencies* using various methods confirm the alarming trend. The overwhelming scientific consensus, built on decades of empirical evidence from glaciers to ocean acidification, unequivocally establishes anthropogenic global warming as a stark reality, not a fabricated crisis or hoax.

==================================================
ROUND 2: REBUTTALS
==================================================

 🔵 PRO (Rebuttal):
--------------------------------------------------
The "unprecedented speed" claim crumbles when examining geological timescales. Earth's climate has experienced far more rapid and dramatic shifts naturally. The alleged "consensus" is often manufactured, stifling dissenting scientists whose research contradicts the narrative, especially given how funding prioritizes alarmism. These systematic "adjustments" to historical data consistently amplify warming trends, generating a crisis from raw, unadjusted records. This ongoing data manipulation, coupled with politically aligned "consensus," underscores the hoax.

 🔴 CON (Rebuttal):
--------------------------------------------------
Geological timescales obscure the *unprecedented rate* of warming now, drastically impacting human civilization. The overwhelming scientific consensus is rigorously peer-reviewed, not manufactured; valid dissent strengthens science, not undermines it. Data adjustments standardize diverse inputs for accuracy, and *multiple independent datasets*, including satellite observations, consistently corroborate accelerating global warming. Denying this convergent evidence is denying reality.

==================================================
ROUND 3: CLOSING STATEMENTS
==================================================

 🔵 PRO (Closing):
--------------------------------------------------
Geological history is replete with *rapid*, dramatic climate shifts predating human influence, making the "unprecedented rate" argument short-sighted. The "peer-reviewed consensus" often functions as an echo chamber, actively marginalizing legitimate scientific dissent and prioritizing alarmist narratives. Even satellite data, initially showing less warming, undergoes *constant adjustments* that invariably align it with the surface record, consistently amplifying the warming trend. This systemic data manipulation, from surface to space, is a hallmark of the hoax.

 🔴 CON (Closing):
--------------------------------------------------
Past climate shifts, while significant, occurred over vastly different timescales and without human industrial drivers; the *current rate* is unprecedentedly fast and profoundly impactful on civilization. The scientific consensus is a rigorous framework, not an echo chamber, continually tested by new evidence; true scientific dissent requires robust data, not mere contrarianism. Satellite data adjustments, like for orbital drift or sensor degradation, are standard procedures to ensure accuracy, and *all major independent satellite datasets* now definitively show a clear, accelerating warming trend, consistent with surface and ocean data, decisively refuting claims of manipulation.

==================================================
FINAL VERDICT
==================================================

 ⚖️  JUDGE:
--------------------------------------------------
SCORES:
ROUND 1: [Pro 6/Con 8]
ROUND 2: [Pro 6/Con 8.5]
ROUND 3: [Pro 5.5/Con 9]

TOTAL SCORE: [Pro 17.5/Con 25.5]

WINNER: [Con]
REASONING: Con consistently presented stronger arguments, grounding its claims in scientific consensus, empirical evidence, and logical defenses of scientific methodologies like data adjustments. It effectively countered Pro's claims of "hoax" by highlighting the unprecedented *rate* of current warming and the human industrial drivers, distinguishing it from natural historical fluctuations. Con's rebuttals were robust, directly addressing Pro's points with clarity and scientific rigor.

LOSER: [Pro]
REASONING: Pro's arguments, while attempting to sow doubt about data and consensus, consistently struggled to present compelling evidence for a "hoax" beyond generalized claims of manipulation and natural cycles. It failed to effectively counter Con's emphasis on the *rate* and *human cause* of current warming, often resorting to reiteration of its initial points without offering new or more specific evidence to support its claims of widespread fabrication.

🏁 Debate Complete!
==================
```

## 🎯 Customizing Debate Topics

Edit the debate topic in `test_debate_api.py`:

**Python:**
```python
    # ===========This is the topic of the debate===========
    text = "Debate topic: Global warming is a hoax"
    # =====================================================
```

## 📁 Project Structure

```
.
├── agents/
│   ├── __init__.py            # Package initialization
│   └── agent.py               # Multi-agent system definition
├── .env                       # Environment variables (Gemini API key)
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
  "userId": "user1",
  "sessionId": "session1",
  "newMessage": {
    "role": "user",
    "parts": [
      {"text": "Debate topic: {your topic here}"}
    ]
  }
}
```
