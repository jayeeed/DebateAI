# Debate-AI System Diagrams

This document contains all the Mermaid diagrams used in the Debate-AI system documentation.

## 1. System Overview (Mind Map)

```mermaid
mindmap
  root((Debate-AI))
    Agents
      ProAgent
      ConAgent
      JudgeAgent
    Structure
      LoopAgent 3x
      SequentialAgent
      Shared State
    Features
      3-Round Debate
      Clean Output
      UUID Sessions
      Cross-Platform
    Customization
      Topics
      Models
      Word Limits
      Iterations
```

**Purpose:** High-level overview of system components and features

---

## 2. Architecture Diagram (Graph)

```mermaid
graph TD
    A[User Submits Debate Topic] --> B[DebateAI System]
    B --> C[DebateLoop - LoopAgent]
    C --> D{Iteration Counter}
    
    D -->|Round 1| E1[DebateRound]
    D -->|Round 2| E2[DebateRound]
    D -->|Round 3| E3[DebateRound]
    
    E1 --> F1[ProAgent]
    F1 --> G1[ConAgent]
    
    E2 --> F2[ProAgent]
    F2 --> G2[ConAgent]
    
    E3 --> F3[ProAgent]
    F3 --> G3[ConAgent]
    
    G1 --> H[Session State]
    G2 --> H
    G3 --> H
    
    H --> I[JudgeAgent]
    I --> J[Winner Declared]
```

**Purpose:** Shows how the LoopAgent executes 3 iterations and feeds into the Judge

---

## 3. Sequence Diagram (Workflow)

```mermaid
sequenceDiagram
    participant User
    participant System as DebateAI System
    participant Looper as LoopAgent (3x)
    participant Pro as ProAgent
    participant Con as ConAgent
    participant State as Session State
    participant Judge as JudgeAgent
    
    User->>System: Submit debate topic
    System->>Looper: Start 3-round debate
    
    Note over Looper,Con: Round 1
    Looper->>Pro: Argue FOR
    Pro->>State: Save argument
    Looper->>Con: Argue AGAINST
    Con->>State: Save argument
    
    Note over Looper,Con: Round 2
    Looper->>Pro: Build on previous + Counter
    Pro->>State: Update argument
    Looper->>Con: Build on previous + Counter
    Con->>State: Update argument
    
    Note over Looper,Con: Round 3
    Looper->>Pro: Closing statement
    Pro->>State: Final argument
    Looper->>Con: Closing statement
    Con->>State: Final argument
    
    Looper->>Judge: Evaluate all rounds
    Judge->>State: Read all arguments
    Judge->>System: Declare winner
    System->>User: Return verdict
```

**Purpose:** Shows the temporal sequence of agent interactions across 3 rounds

---

## 4. Component Structure (Graph)

```mermaid
graph LR
    A[debate_system<br/>SequentialAgent] --> B[debate_loop<br/>LoopAgent<br/>max_iterations=3]
    A --> C[judge_agent<br/>LlmAgent]
    
    B --> D[debate_round<br/>SequentialAgent]
    
    D --> E[pro_agent<br/>LlmAgent]
    D --> F[con_agent<br/>LlmAgent]
    
    E -.->|output_key| G[(Session State)]
    F -.->|output_key| G
    C -.->|reads from| G
```

**Purpose:** Shows the hierarchical structure of agents and their relationships

---

## 5. Data Flow Diagram

```mermaid
flowchart LR
    A[Debate Topic] --> B{DebateAI}
    B --> C[Round 1]
    B --> D[Round 2]
    B --> E[Round 3]
    
    C --> C1[Pro: Opening]
    C --> C2[Con: Opening]
    
    D --> D1[Pro: Rebuttal]
    D --> D2[Con: Rebuttal]
    
    E --> E1[Pro: Closing]
    E --> E2[Con: Closing]
    
    C1 & C2 & D1 & D2 & E1 & E2 --> F[Judge]
    F --> G{Winner}
    
    G -->|Pro Wins| H[✅ Pro]
    G -->|Con Wins| I[✅ Con]
```

**Purpose:** Shows how data flows from input through rounds to final verdict

---

## 6. State Management Diagram

```mermaid
stateDiagram-v2
    [*] --> Initialized: User submits topic
    
    Initialized --> Round1: Start Loop
    
    Round1 --> ProArgues1: ProAgent executes
    ProArgues1 --> ConArgues1: ConAgent executes
    ConArgues1 --> Round2: Iteration 1 complete
    
    Round2 --> ProArgues2: ProAgent executes
    ProArgues2 --> ConArgues2: ConAgent executes
    ConArgues2 --> Round3: Iteration 2 complete
    
    Round3 --> ProArgues3: ProAgent executes
    ProArgues3 --> ConArgues3: ConAgent executes
    ConArgues3 --> Judging: Loop complete
    
    Judging --> ProWins: Judge declares Pro
    Judging --> ConWins: Judge declares Con
    
    ProWins --> [*]
    ConWins --> [*]
    
    note right of Round1
        Opening statements
    end note
    
    note right of Round2
        Rebuttals
    end note
    
    note right of Round3
        Closing statements
    end note
```

**Purpose:** Shows the state transitions throughout the debate lifecycle

---

## 7. Agent Interaction Pattern

```mermaid
graph TB
    subgraph "Iteration 1"
        A1[ProAgent] -->|Argument| B1[Session State]
        B1 -->|Context| C1[ConAgent]
        C1 -->|Counter-Argument| B1
    end
    
    subgraph "Iteration 2"
        A2[ProAgent] -->|Reads previous| B2[Session State]
        B2 -->|Enhanced Argument| A2
        A2 -->|Rebuttal| B2
        B2 -->|Context| C2[ConAgent]
        C2 -->|Counter-Rebuttal| B2
    end
    
    subgraph "Iteration 3"
        A3[ProAgent] -->|Reads all previous| B3[Session State]
        B3 -->|Closing Statement| A3
        A3 -->|Final Argument| B3
        B3 -->|Context| C3[ConAgent]
        C3 -->|Final Counter| B3
    end
    
    B1 --> B2
    B2 --> B3
    B3 --> D[JudgeAgent]
    D --> E[Verdict]
```

**Purpose:** Shows how agents interact with shared state across iterations

---

## 8. Simplified Flow (For Presentations)

```mermaid
graph LR
    A[📝 Topic] --> B[🔁 Loop 3x]
    B --> C[🔵 Pro]
    B --> D[🔴 Con]
    C & D --> E[⚖️ Judge]
    E --> F[🏆 Winner]
```

**Purpose:** Simple, high-level flow for quick understanding
