import json

def load_knowledge():
    with open("knowledge.json", "r") as f:
        return json.load(f)

def get_answer(query, knowledge):
    query = query.lower()

    if "basic" in query:
        return f"Basic Plan: {knowledge['pricing']['basic']['price']} with {', '.join(knowledge['pricing']['basic']['features'])}"

    elif "pro" in query:
        return f"Pro Plan: {knowledge['pricing']['pro']['price']} with {', '.join(knowledge['pricing']['pro']['features'])}"

    elif "refund" in query:
        return knowledge["policies"]["refund"]

    elif "support" in query:
        return knowledge["policies"]["support"]

    else:
        return "Sorry, I couldn't find that information."