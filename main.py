import random

class DynamicVocabulary:
    def __init__(self):
        self.contexts = []  # Placeholder for game-defined contexts
        self.subjects = []  # Placeholder for game-defined subjects
        self.actions = []  # Placeholder for game-defined actions
        self.objects = []  # Placeholder for game-defined objects

    def set_vocabulary(self, contexts=None, subjects=None, actions=None, objects=None):
        """Set or update the dynamic vocabulary."""
        if contexts is not None:
            self.contexts = contexts
        if subjects is not None:
            self.subjects = subjects
        if actions is not None:
            self.actions = actions
        if objects is not None:
            self.objects = objects

    def generate_sentence(self):
        """Combine dynamic vocabulary into a coherent sentence."""
        context = random.choice(self.contexts) if self.contexts else "In an undefined context"
        subject = random.choice(self.subjects) if self.subjects else "someone"
        action = random.choice(self.actions) if self.actions else "does something"
        obj = random.choice(self.objects) if self.objects else "somewhere"
        return f"{context}, {subject} {action} {obj}."

class ThoughtProcessor:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def generate_thought(self, npc_state):
        """Generate a thought for the NPC based on their current state."""
        if not self.vocabulary.contexts or not self.vocabulary.subjects or not self.vocabulary.actions or not self.vocabulary.objects:
            return "The NPC seems lost in undefined thoughts."

        thought_components = {
            "contexts": self.vocabulary.contexts,
            "subjects": self.vocabulary.subjects,
            "actions": self.vocabulary.actions,
            "objects": self.vocabulary.objects,
        }

        # Select a random context, subject, action, and object based on state
        context = random.choice(thought_components["contexts"])
        subject = random.choice(thought_components["subjects"])
        action = random.choice(thought_components["actions"])
        obj = random.choice(thought_components["objects"])

        # Assemble a dynamic thought
        thought = f"{context}, {subject} {action} {obj}."
        return thought

class NPC:
    def __init__(self, name, state):
        self.name = name
        self.state = state  # A dictionary defining emotional and contextual state
        self.interaction_history = []

    def add_interaction(self, interaction):
        """Update interaction history and modify state if necessary."""
        self.interaction_history.append(interaction)
        if len(self.interaction_history) > 5:
            self.interaction_history.pop(0)

    def update_emotion(self):
        """Update the NPC's emotion based on interaction history and buzzwords."""
        # Define buzzwords for adjusting emotion
        positive_buzzwords = {"helped", "saved", "kind", "loved", "praised", "gifted"}
        negative_buzzwords = {"hurt", "ignored", "mocked", "stolen", "attacked", "lied"}

        # Base emotion starts at neutral (5 on a 1-10 scale)
        emotion_rating = 5

        # Adjust emotion based on buzzwords in interaction history
        for word in self.interaction_history:
            if word in positive_buzzwords:
                emotion_rating += 1
            elif word in negative_buzzwords:
                emotion_rating -= 1

        # Clamp emotion rating between 1 and 10
        self.state["emotion"] = max(1, min(10, emotion_rating))

    def think(self, thought_processor):
        """Generate and return an internal thought."""
        return thought_processor.generate_thought(self.state)

# Example usage
vocabulary = DynamicVocabulary()
vocabulary.set_vocabulary(
    contexts=["In the forest", "On the battlefield", "At the marketplace"],
    subjects=["the merchant", "the adventurer", "a guard"],
    actions=["is pondering", "is trading", "is exploring"],
    objects=["a mysterious artifact", "a hidden cave", "a rare gem"]
)

npc = NPC(name="Guard", state={"emotion": "neutral", "context": "peaceful"})
thought_processor = ThoughtProcessor(vocabulary)

# Generate a thought
npc_thought = npc.think(thought_processor)
print(f"NPC Thought: {npc_thought}")

# Generate a sentence based on dynamic vocabulary
sentence = vocabulary.generate_sentence()
print(f"Generated Sentence: {sentence}")
