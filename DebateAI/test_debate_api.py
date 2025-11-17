#!/usr/bin/env python3
"""
Debate-AI API Testing Script
Usage: python test_debate_api.py
"""

import requests
import json
import sys
import uuid

BASE_URL = "http://localhost:8000"
APP_NAME = "agents"
USER_ID = str(uuid.uuid4())
SESSION_ID = str(uuid.uuid4())


def print_header(text):
    """Print a formatted header"""
    print(f"\n{text}")
    print("=" * len(text))
    print()


def print_agent_response(title, text, emoji):
    """Print an agent's response with formatting"""
    print(f"{emoji} {title}")
    print("-" * 50)
    print(text)
    print()


def main():
    print_header("🎭 Debate-AI System - API Test")

    print(f"👤 User ID: {USER_ID}")
    print(f"🔑 Session ID: {SESSION_ID}")
    print()

    # Step 1: Create Session
    print("📝 Step 1: Creating session...")
    try:
        response = requests.post(
            f"{BASE_URL}/apps/{APP_NAME}/users/{USER_ID}/sessions/{SESSION_ID}",
            headers={"Content-Type": "application/json"},
            json={},
        )
        response.raise_for_status()
        print("✅ Session created\n")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error creating session: {e}")
        sys.exit(1)

    # Step 2: Start Debate
    print("🎤 Step 2: Starting debate...")
    print("Topic: Global warming is a real threat\n")
    print("=" * 50)
    print()

    try:
        response = requests.post(
            f"{BASE_URL}/run",
            headers={"Content-Type": "application/json"},
            json={
                "appName": APP_NAME,
                "userId": USER_ID,
                "sessionId": SESSION_ID,
                "newMessage": {
                    "role": "user",
                    "parts": [
                        {"text": "Debate topic: Global warming is a real threat"}
                    ],
                },
            },
        )
        response.raise_for_status()
        events = response.json()

        print(f"📊 Received {len(events)} events from the debate system\n")

        # Helper function to extract text from event
        def get_text(event):
            try:
                content = event.get("content", {})
                parts = content.get("parts", [])
                if parts and len(parts) > 0:
                    return parts[0].get("text", "No response")
                return "No response"
            except (AttributeError, TypeError, IndexError):
                return "No response"

        # Parse and display each agent's response
        if len(events) >= 7:
            # Round 1
            print("=" * 50)
            print("ROUND 1: OPENING STATEMENTS")
            print("=" * 50)
            print()

            print_agent_response("🔵 PRO (Opening):", get_text(events[0]), "")
            print_agent_response("🔴 CON (Opening):", get_text(events[1]), "")

            # Round 2
            print("=" * 50)
            print("ROUND 2: REBUTTALS")
            print("=" * 50)
            print()

            print_agent_response("🔵 PRO (Rebuttal):", get_text(events[2]), "")
            print_agent_response("🔴 CON (Rebuttal):", get_text(events[3]), "")

            # Round 3
            print("=" * 50)
            print("ROUND 3: CLOSING STATEMENTS")
            print("=" * 50)
            print()

            print_agent_response("🔵 PRO (Closing):", get_text(events[4]), "")
            print_agent_response("🔴 CON (Closing):", get_text(events[5]), "")

            # Judge
            print("=" * 50)
            print("FINAL VERDICT")
            print("=" * 50)
            print()

            print_agent_response("⚖️  JUDGE:", get_text(events[6]), "")
        else:
            print(
                f"⚠️  Unexpected response format - got {len(events)} events, expected 7"
            )
            print("\nShowing available events:")
            for i, event in enumerate(events):
                print(f"\n--- Event {i+1} ---")
                text = get_text(event)
                author = event.get("author", "Unknown")
                print(f"Author: {author}")
                print(f"Text: {text[:100]}..." if len(text) > 100 else f"Text: {text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error running debate: {e}")
        sys.exit(1)
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"❌ Error parsing response: {e}")
        sys.exit(1)

    print_header("🏁 Debate Complete!")


if __name__ == "__main__":
    main()
