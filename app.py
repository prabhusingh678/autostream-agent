from intent import detect_intent
from rag import load_knowledge, get_answer
from tools import mock_lead_capture

knowledge = load_knowledge()

# Memory
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

def chat():
    print("🤖 AutoStream Agent Started! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        intent = detect_intent(user_input)
        state["intent"] = intent

        # Greeting
        if intent == "greeting":
            print("Agent: Hello! How can I help you today?")

        # Inquiry (RAG)
        elif intent == "inquiry":
            answer = get_answer(user_input, knowledge)
            print("Agent:", answer)

        # High Intent
        elif intent == "high_intent":
            print("Agent: Great! Let's get you started 🚀")

            if not state["name"]:
                state["name"] = input("Agent: What's your name? ")

            if not state["email"]:
                state["email"] = input("Agent: Your email? ")

            if not state["platform"]:
                state["platform"] = input("Agent: Which platform do you use (YouTube/Instagram)? ")

            # Call tool ONLY after all data collected
            if state["name"] and state["email"] and state["platform"]:
                mock_lead_capture(state["name"], state["email"], state["platform"])

        else:
            print("Agent: Can you please clarify?")

if __name__ == "__main__":
    chat()