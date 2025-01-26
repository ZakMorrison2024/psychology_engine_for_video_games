class NPC:
    def __init__(self, name, ego, o, c, e, a, n):
        self.name = name
        self.personality = {
            "Openness": o,
            "Conscientiousness": c,
            "Extraversion": e,
            "Agreeableness": a,
            "Neuroticism": n,
            "Ego": ego
        }
        self.relationships = {}  # Tracks other NPCs/players
        self.item_preferences = {}  # Tracks item perceptions
        self.environment_responses = {}  # Tracks environment perceptions
        self.memory = []

    def meet(self, entity, interaction, context):
        """Handles first-time meetings and impressions."""
        impression_score = (
            (self.personality["Agreeableness"] * 0.5) +
            (self.personality["Extraversion"] * 0.3) +
            (self.personality["Openness"] * 0.2)
        )
        
        if impression_score > 0.7:
            self.relationships[entity] = "positive"
        elif impression_score < 0.4:
            self.relationships[entity] = "negative"
        else:
            self.relationships[entity] = "neutral"
        
        self.memory.append(f"Met {entity} in {context}, impression: {self.relationships[entity]}")
        return self.relationships[entity]

    def interact(self, entity, interaction, result):
        """Adjust NPC perception based on interaction outcomes."""
        impact = 0.1 if result == "neutral" else (0.2 if result == "positive" else -0.2)
        
        if entity in self.relationships:
            if self.relationships[entity] == "positive":
                impact *= self.personality["Agreeableness"]
            elif self.relationships[entity] == "negative":
                impact *= -self.personality["Neuroticism"]

        self.memory.append(f"Interacted with {entity}: {interaction}, result: {result}")
        return self.relationships[entity]

    def use_item(self, item, result):
        """Track NPC opinions on items based on past experiences."""
        self.item_preferences[item] = result
        self.memory.append(f"Used {item}, result: {result}")

    def enter(self, environment):
        """Adjust NPC response based on environmental factors."""
        response = "neutral"
        if environment in self.environment_responses:
            response = self.environment_responses[environment]
        else:
            if self.personality["Neuroticism"] > 0.6:
                response = "anxious"
            elif self.personality["Openness"] > 0.5:
                response = "curious"
            else:
                response = "neutral"

        self.environment_responses[environment] = response
        self.memory.append(f"Entered {environment}, reaction: {response}")
        return response

    def recall_memory(self):
        """Returns the NPC's stored memory."""
        return self.memory
