#!/usr/bin/env python3
"""
Lightweight Multi-Agent Chat Interface
Works with existing dependencies while Open WebUI installs
"""

import os
import json
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

try:
    from openai import OpenAI
    HAS_OPENAI = True
except:
    HAS_OPENAI = False

# Initialize OpenAI client
if HAS_OPENAI and os.getenv('OPENAI_API_KEY'):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
else:
    print("⚠️  OpenAI not available. Install with: pip install openai")
    client = None

# Load personas
PERSONAS_DIR = Path(__file__).parent / "data" / "personas"

def load_personas():
    """Load all persona definitions"""
    personas = {}
    for file in PERSONAS_DIR.glob("*.json"):
        with open(file) as f:
            persona = json.load(f)
            personas[persona['role']] = persona
    return personas

def chat_with_persona(persona, message):
    """Chat with a specific persona"""
    if not client:
        return "Error: OpenAI client not initialized. Check your API key."

    try:
        response = client.chat.completions.create(
            model=persona.get('model', 'gpt-4'),
            messages=[
                {"role": "system", "content": persona['system_prompt']},
                {"role": "user", "content": message}
            ],
            temperature=persona.get('temperature', 0.7)
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main chat interface"""
    print("\n" + "="*60)
    print("🤖 Multi-Agent Workspace - Lite Version")
    print("="*60)
    print()

    personas = load_personas()

    if not personas:
        print("❌ No personas found. Run setup.py first.")
        return

    print("Available Personas:")
    for i, (role, persona) in enumerate(personas.items(), 1):
        print(f"  {i}. {persona['avatar']} {persona['name']} - {persona['description']}")

    print()
    print("Commands:")
    print("  'switch' - Change persona")
    print("  'list' - Show available personas")
    print("  'quit' - Exit")
    print()
    print("="*60)
    print()

    # Select initial persona
    roles = list(personas.keys())
    current_persona = personas[roles[0]]

    print(f"\n🤖 Chatting with: {current_persona['name']}\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == 'quit':
                print("\n👋 Goodbye!\n")
                break

            if user_input.lower() == 'list':
                print("\nAvailable Personas:")
                for i, (role, persona) in enumerate(personas.items(), 1):
                    print(f"  {i}. {persona['avatar']} {persona['name']}")
                print()
                continue

            if user_input.lower() == 'switch':
                print("\nSelect persona:")
                for i, (role, persona) in enumerate(personas.items(), 1):
                    print(f"  {i}. {persona['avatar']} {persona['name']}")

                try:
                    choice = int(input("\nEnter number: ")) - 1
                    if 0 <= choice < len(roles):
                        current_persona = personas[roles[choice]]
                        print(f"\n🤖 Now chatting with: {current_persona['name']}\n")
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Invalid input")
                continue

            # Chat with persona
            print()
            response = chat_with_persona(current_persona, user_input)
            print(f"{current_persona['avatar']} {current_persona['name']}: {response}")
            print()

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\nError: {e}\n")

if __name__ == "__main__":
    main()
