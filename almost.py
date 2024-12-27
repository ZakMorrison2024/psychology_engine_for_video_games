import random

class NPC:
    def __init__(self, name, dynamic_vocabulary):
        self.name = name
        self.dynamic_vocabulary = dynamic_vocabulary
        self.state = {
            "emotion": 5,  # Emotion scale from 0 (miserable) to 10 (ecstatic)
            "context": "neutral",
            "interaction_history": []
        }

    def generate_dynamic_sentence(self):
        """Generate a dynamic sentence using the vocabulary."""
        context = random.choice(self.dynamic_vocabulary['contexts'])
        subject = random.choice(self.dynamic_vocabulary['subjects'])
        action = random.choice(self.dynamic_vocabulary['actions'])
        obj = random.choice(self.dynamic_vocabulary['objects'])

        sentence = f"{context}, {subject} {action} {obj}."
        return sentence

    def update_emotion(self):
        """Update emotion on a scale of 0 (miserable) to 10 (ecstatic) based on interaction history."""
        positive_interactions = sum(1 for action in self.interaction_history if action == "helped")
        negative_interactions = sum(1 for action in self.interaction_history if action == "hurt")
        
        # Adjust emotion scale
        self.state["emotion"] = max(0, min(10, 5 + positive_interactions - negative_interactions))

    def add_interaction(self, interaction):
        """Add an interaction to the history and update the NPC's emotional state."""
        self.state['interaction_history'].append(interaction)
        if len(self.state['interaction_history']) > 10:  # Limit history length
            self.state['interaction_history'].pop(0)
        self.update_emotion()

    def generate_internal_thought(self):
        """Generate an internal thought dynamically using the vocabulary."""
        thought_context = random.choice(self.dynamic_vocabulary['contexts'])
        thought_action = random.choice(self.dynamic_vocabulary['actions'])
        thought_subject = "I"  # Internal thoughts are ego-centric
        thought_obj = random.choice(self.dynamic_vocabulary['objects'])

        thought = f"{thought_context}, {thought_subject} {thought_action} {thought_obj}."
        return thought

# Example dynamic vocabulary
dynamic_vocabulary = {
    "contexts": [
        "On a quiet afternoon",
        "In the bustling marketplace",
        "While exploring the forest",
        "At the guild hall"
    ],
    "subjects": [
        "the NPC",
        "the player",
        "a guard",
        "an adventurer"
    ],
    "actions": [
        "is pondering",
        "is crafting",
        "is exploring",
        "is assisting"
    ],
    "objects": [
        "a new item",
        "the surrounding area",
        "a mysterious artifact",
        "their fellow adventurers"
    ]
}

# Example usage
npc = NPC("Guard", dynamic_vocabulary)
npc.add_interaction("helped")
npc.add_interaction("hurt")

print("Generated Sentence:", npc.generate_dynamic_sentence())
print("NPC Emotion:", npc.state["emotion"])
print("NPC Thought:", npc.generate_internal_thought())
