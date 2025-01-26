import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from random import choice

nltk.download('vader_lexicon')  # Download sentiment analysis tool

class NPC:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality  # Dict with O, C, E, A, N, ego
        self.memory = []  # Stores past conversation topics
        self.sia = SentimentIntensityAnalyzer()  # Sentiment analyzer

    def listen(self, player_input):
        """Process player input and categorize sentiment."""
        sentiment = self.sia.polarity_scores(player_input)
        keywords = nltk.word_tokenize(player_input.lower())
        
        # Categorize player intent based on keywords
        if "help" in keywords or "assist" in keywords:
            intent = "help_request"
        elif "fight" in keywords or "attack" in keywords:
            intent = "hostile"
        else:
            intent = "neutral"

        # Store memory of interaction
        self.memory.append({"input": player_input, "intent": intent, "sentiment": sentiment['compound']})
        
        return intent, sentiment['compound']

    def respond(self, intent, sentiment):
        """Generate a response based on personality and sentiment."""
        responses = {
            "help_request": ["Sure, I'm always happy to assist!", "Why should I help you?", "I’ll think about it..."],
            "hostile": ["I'm not looking for trouble.", "Bring it on!", "Violence isn't the answer."],
            "neutral": ["Interesting.", "Tell me more.", "Hmmm..."]
        }

        # NPC's personality affects response choice
        if sentiment > 0.5:
            personality_factor = "positive"
        elif sentiment < -0.5:
            personality_factor = "negative"
        else:
            personality_factor = "neutral"

        chosen_response = choice(responses[intent])
        
        if self.personality["Agreeableness"] > 0.7 and personality_factor == "positive":
            return f"{chosen_response} You're really nice!"
        elif self.personality["Neuroticism"] > 0.6 and personality_factor == "negative":
            return f"{chosen_response} I don't trust you..."
        else:
            return chosen_response

# Example usage
npc = NPC("Zak", {"Openness": 0.8, "Conscientiousness": 0.5, "Extraversion": 0.6, "Agreeableness": 0.9, "Neuroticism": 0.2, "Ego": 0.7})

player_input = input("You: ")
intent, sentiment = npc.listen(player_input)
response = npc.respond(intent, sentiment)
print(f"{npc.name}: {response}")
