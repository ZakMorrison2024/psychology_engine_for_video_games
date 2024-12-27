import random

class DynamicVocabularyWithEgo:
    def __init__(self):
        self.contexts = []  # Game-defined contexts
        self.subjects = []  # Game-defined subjects
        self.actions = []  # Game-defined actions
        self.objects = []  # Game-defined objects
        self.ego_weights = {}  # For ego-related weights

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

    def set_ego_weights(self, ego_weights):
        """Set ego-related weights to influence NPC's language."""
        self.ego_weights = ego_weights

    def generate_sentence(self, npc_ego, context):
        """Generate a sentence using dynamic vocabulary and adjusted by ego."""
        context = random.choice(self.contexts) if self.contexts else "In an undefined context"
        subject = random.choice(self.subjects) if self.subjects else "someone"
        action = random.choice(self.actions) if self.actions else "does something"
        obj = random.choice(self.objects) if self.objects else "somewhere"
        
        # Adjust for ego-based behavior
        sentence = f"{context}, {subject} {action} {obj}."
        
        # Modify sentence based on NPC ego
        ego_modifier = self.adjust_ego(npc_ego)
        sentence = self.apply_ego_to_sentence(sentence, ego_modifier)
        
        return sentence

    def adjust_ego(self, npc_ego):
        """Adjust weights based on ego level."""
        if npc_ego > 7:
            return "superior"  # Confident, self-important
        elif npc_ego < 4:
            return "inferior"  # Self-doubt, less assertive
        else:
            return "neutral"  # Balanced ego, not extreme in any direction

    def apply_ego_to_sentence(self, sentence, ego_modifier):
        """Alter the sentence based on ego level."""
        if ego_modifier == "superior":
            return sentence.replace("someone", "I")
        elif ego_modifier == "inferior":
            return sentence.replace("someone", "I, though I’m not sure I can do it well")
        else:
            return sentence


class NPCWithEgo:
    def __init__(self, name, state, ego_level):
        self.name = name
        self.state = state  # A dictionary defining emotional and contextual state
        self.ego_level = ego_level  # Ego level from 1 to 10 (1 being the least self-important)
        self.interaction_history = []

    def add_interaction(self, interaction):
        """Update interaction history and modify state if necessary."""
        self.interaction_history.append(interaction)
        if len(self.interaction_history) > 5:
            self.interaction_history.pop(0)

    def update_emotion(self):
        """Update the NPC's emotion based on interaction history."""
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

class ThoughtProcessor:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def generate_thought(self, npc_state):
        """Generate a thought for the NPC based on their current state."""
        # The NPC's internal monologue focused on self-reflection and reasoning behind actions
        if not self.vocabulary.contexts or not self.vocabulary.subjects or not self.vocabulary.actions or not self.vocabulary.objects:
            return "I don't know what I should be doing right now."

        # Extract current emotional state and context
        emotion_rating = npc_state.get("emotion", 5)  # Default to neutral if undefined
        context = npc_state.get("context", "neutral")

        # Construct a self-reflective thought based on emotion and ego level
        if emotion_rating <= 3:
            thought = f"I'm feeling so helpless right now. Why am I even doing this? Is this action really worth it?"
        elif emotion_rating <= 6:
            thought = f"Alright, I guess this is the right thing to do, but it still feels like a waste of time. Why am I pushing myself?"
        elif emotion_rating > 6:
            thought = f"I’ve got this! There’s no one better than me to handle this situation. Everything I do is for a reason, and it’s going to work out."

        # Modify thought based on NPC ego
        ego_modifier = self.vocabulary.adjust_ego(npc_state.get("emotion", 5))
        thought = self.apply_ego_to_thought(thought, ego_modifier)
        
        return thought

    def apply_ego_to_thought(self, thought, ego_modifier):
        """Modify internal monologue based on ego level."""
        if ego_modifier == "superior":
            return thought.replace("I", "I, the master of this world,").replace("this", "everything I do")
        elif ego_modifier == "inferior":
            return thought.replace("I", "I, who have no chance,").replace("this", "what I must do, even if I fail")
        else:
            return thought

# Example Usage

vocabulary = DynamicVocabularyWithEgo()
vocabulary.set_vocabulary(
    contexts=["In the bustling town square", "On the battlefield", "While exploring the forest"],
    subjects=["the NPC", "the player", "a guard"],
    actions=["is gathering", "is fighting", "is exploring"],
    objects=["resources", "enemies", "treasures"]
)

# Ego weights example
vocabulary.set_ego_weights({
    "superior": {"gathering": 1.5, "fighting": 2, "exploring": 1.2},
    "inferior": {"gathering": 0.8, "fighting": 0.7, "exploring": 0.9},
    "neutral": {"gathering": 1.0, "fighting": 1.0, "exploring": 1.0}
})

npc = NPCWithEgo(name="Guard", state={"emotion": 5, "context": "neutral"}, ego_level=9)  # Highly self-important NPC
thought_processor = ThoughtProcessor(vocabulary)

# Generate a thought and sentence
npc_thought = npc.think(thought_processor)
sentence = vocabulary.generate_sentence(npc_ego=npc.ego_level, context="peaceful")

print(f"NPC Thought: {npc_thought}")
print(f"Generated Sentence: {sentence}")
