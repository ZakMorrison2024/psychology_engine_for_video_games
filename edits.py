import random

class DynamicVocabulary:
    def __init__(self):
        self.contexts = []  # Placeholder for game-defined contexts
        self.subjects = []  # Placeholder for game-defined subjects
        self.actions = []  # Placeholder for game-defined actions
        self.objects = []  # Placeholder for game-defined objects
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

      context.append(PLACEHOLDERS["contexts"]) 
      subjects.append(PLACEHOLDERS["subjects"])
      actions.append(PLACEHOLDERS["actions"]) 
      objects.append(PLACEHOLDERS["objects"])

    def set_ego_weights(self, ego_weights):
        """Set ego-related weights to influence NPC's language."""
        self.ego_weights = ego_weights

    def set_word_weights(emotion, action, context, polarity):
        """Set the word weights dynamically based on game-specific values."""
        word_weights["emotion"] = emotion
        word_weights["action"] = action
        word_weights["context"] = context
        word_weights["polarity"] = polarity

     def apply_emotion_bias(self, emotion_rating):
        """Adjust the word weights based on the NPC's emotional state (1-10)."""
        # Define basic scaling factors for each category
        emotion_scaling_factor = {
            1: 0.2,   # Extremely negative
            2: 0.4,   # Very negative
            3: 0.6,   # Negative
            4: 0.8,   # Slightly negative
            5: 1.0,   # Neutral
            6: 1.2,   # Slightly positive
            7: 1.4,   # Positive
            8: 1.6,   # Very positive
            9: 1.8,   # Extremely positive
            10: 2.0   # Ecstatic
        }
        
        scaling_factor = emotion_scaling_factor.get(emotion_rating, 1.0)
        
        # Adjust the word weights for each category based on the emotional scaling factor
        adjusted_weights = {
            "emotion": {word: weight * scaling_factor for word, weight in word_weights["emotion"].items()},
            "action": {word: weight * scaling_factor for word, weight in word_weights["action"].items()},
            "context": {word: weight * scaling_factor for word, weight in word_weights["context"].items()},
            "polarity": {word: weight * scaling_factor for word, weight in word_weights["polarity"].items()},
        }
        
        return adjusted_weights

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

    def generate_weighted_word(self, category, adjusted_weights):
        """Generate a word based on adjusted weights for a given category."""
        words = list(adjusted_weights[category].keys())
        weights = list(adjusted_weights[category].values())
        
        # Normalize the weights (to handle very large/small numbers)
        total_weight = sum(weights)
        normalized_weights = [weight / total_weight for weight in weights]
        
        # Select a word based on the normalized weights
        selected_word = random.choices(words, normalized_weights)[0]
        return selected_word

    def generate_sentence(self, ego_weights, emotion_rating):
        """Combine dynamic vocabulary into a coherent sentence."""
        """Generate a sentence with adjusted weights based on NPC's emotional state."""
        
      

        adjusted_weights = self.apply_emotion_bias(emotion_rating)
        
        # Select words from each category based on the adjusted weights
        context = self.generate_weighted_word("context", adjusted_weights)
        subject = self.generate_weighted_word("emotion", adjusted_weights)
        action = self.generate_weighted_word("action", adjusted_weights)
        obj = self.generate_weighted_word("polarity", adjusted_weights)
      
      ### FIX THIS
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


        ## to add
        emotion_rating = npc_state.get("emotion", 5)
        adjusted_weights = self.vocabulary.apply_emotion_bias(emotion_rating)
        
        # Generate words based on emotional weights
        context = self.vocabulary.generate_weighted_word("context", adjusted_weights)
        subject = self.vocabulary.generate_weighted_word("emotion", adjusted_weights)
        action = self.vocabulary.generate_weighted_word("action", adjusted_weights)
        obj = self.vocabulary.generate_weighted_word("polarity", adjusted_weights)
        
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
        emotion_rating = self.state["emotion"]

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

    def speech(self): ## edit to include vocabulary
    """Generate and filter sentences dynamically based on game state and NPC state."""
      for _ in range(10):  # Generate a batch of sentences
        sentence, score = generate_sentence(self.state["ego"], self.state["emotion"])
        if sentence and score > 0:  # Filter undesirable or incoherent sentences
            print(sentence)

# Example usage
vocabulary = DynamicVocabulary()
vocabulary.set_vocabulary(
    contexts=["In the forest", "On the battlefield", "At the marketplace"],
    subjects=["the merchant", "the adventurer", "a guard"],
    actions=["is pondering", "is trading", "is exploring"],
    objects=["a mysterious artifact", "a hidden cave", "a rare gem"]
)

# Ego weights example
vocabulary.set_ego_weights({
    "superior": {"gathering": 1.5, "fighting": 2, "exploring": 1.2},
    "inferior": {"gathering": 0.8, "fighting": 0.7, "exploring": 0.9},
    "neutral": {"gathering": 1.0, "fighting": 1.0, "exploring": 1.0}
})

##### Everything below this point should be given in game and processed through this script.
# Define placeholders for dynamic vocabulary and game contexts (This should be fed in by in-game data)
PLACEHOLDERS = {
    "contexts": [],  # Placeholder for environment contexts
    "subjects": [],  # Placeholder for NPCs, players, and other characters
    "actions": [],   # Placeholder for actions the subjects perform
    "objects": []    # Placeholder for objects or results of actions
}


npc = NPC(name="Guard", state={"emotion": 5, "ego": 5})
thought_processor = ThoughtProcessor(vocabulary)

# Generate a thought
npc_thought = npc.think(thought_processor)
print(f"NPC Thought: {npc_thought}")

# Generate a sentence based on dynamic vocabulary
sentence = vocabulary.generate_sentence()
print(f"Generated Sentence: {sentence}")
