from collections import defaultdict
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure you have downloaded NLTK dependencies
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Big Five personality traits dictionary
big_five_traits = {
    "Openness": 5,
    "Conscientiousness": 5,
    "Extraversion": 5,
    "Agreeableness": 5,
    "Neuroticism": 5
}

class NPC:
    def __init__(self, name, state, traits=None):
        self.name = name
        self.state = state  # A dictionary defining emotional and contextual state
        self.traits = traits or big_five_traits.copy()
        self.interaction_history = []

    def add_interaction(self, interaction):
        """Update interaction history and modify state if necessary."""
        self.interaction_history.append(interaction)
        if len(self.interaction_history) > 5:
            self.interaction_history.pop(0)

    def update_emotion(self):
        """Update the NPC's emotion based on interaction history and buzzwords."""
        positive_buzzwords = {"helped", "saved", "kind", "loved", "praised", "gifted"}
        negative_buzzwords = {"hurt", "ignored", "mocked", "stolen", "attacked", "lied"}
        emotion_rating = self.state["emotion"]

        for word in self.interaction_history:
            if word in positive_buzzwords:
                emotion_rating += 1
            elif word in negative_buzzwords:
                emotion_rating -= 1

        self.state["emotion"] = max(1, min(10, emotion_rating))

    def think(self, thought_processor):
        """Generate and return an internal thought."""
        return thought_processor.generate_thought(self.state)

    def update_traits(self, player_input):
        """Update Big Five traits based on player input sentiment."""
        sentiment = sia.polarity_scores(player_input)
        if sentiment['pos'] > 0.5:
            self.traits["Agreeableness"] += 0.1
        elif sentiment['neg'] > 0.5:
            self.traits["Neuroticism"] += 0.1

        # Clamp traits to a scale of 1-10
        for trait in self.traits:
            self.traits[trait] = max(1, min(10, self.traits[trait]))

    def listen_and_respond(self, player_input, thought_processor):
        """Analyze player input, update state, and respond."""
        sentiment = sia.polarity_scores(player_input)
        self.update_traits(player_input)

        if sentiment["compound"] > 0.5:
            response = "Thank you for your kind words."
        elif sentiment["compound"] < -0.5:
            response = "That was uncalled for."
        else:
            response = "I see. Let's continue."

        # Update emotion state
        self.add_interaction(player_input)
        self.update_emotion()

        # Generate a thought or dynamic response
        thought = self.think(thought_processor)
        return f"{response} {thought}"


class ThoughtProcessor:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def generate_thought(self, npc_state):
        """Generate a thought for the NPC based on their current state."""
        emotion_rating = npc_state.get("emotion", 5)
        adjusted_weights = self.vocabulary.apply_emotion_bias(emotion_rating)

        context = self.vocabulary.generate_weighted_word("context", adjusted_weights)
        subject = self.vocabulary.generate_weighted_word("emotion", adjusted_weights)
        action = self.vocabulary.generate_weighted_word("action", adjusted_weights)
        obj = self.vocabulary.generate_weighted_word("polarity", adjusted_weights)

        thought = f"{context}, {subject} {action} {obj}."
        return thought


# Example usage
npc_state = {"emotion": 5, "ego": 5}
npc = NPC(name="Guard", state=npc_state)
vocabulary = DynamicVocabulary()
thought_processor = ThoughtProcessor(vocabulary)

# Simulate player input and NPC response
player_input = "You're doing a great job!"
npc_response = npc.listen_and_respond(player_input, thought_processor)
print(npc_response)
