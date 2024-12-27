import random

class NPC:
    def __init__(self, name, personality_type):
        self.name = name
        self.personality_type = personality_type
        self.memory = []  # Will store past events
        self.emotional_state = "neutral"
        self.current_location = None
        self.relationships = {}
    
    def remember(self, event):
        """Stores important events in the NPC's memory."""
        self.memory.append(event)
    
    def set_location(self, location):
        """Updates the NPC's location."""
        self.current_location = location
    
    def update_emotion(self, emotion):
        """Updates the NPC's emotional state."""
        self.emotional_state = emotion
    
    def update_relationship(self, npc_name, relationship):
        """Updates relationship with another NPC or the player."""
        self.relationships[npc_name] = relationship

    def generate_thoughts(self):
        """Generate thoughts based on memory, emotion, and surroundings."""
        thought = ""

        if self.emotional_state == "happy":
            thought += f"I'm feeling great today. I remember when I helped the player. Good times.\n"
        elif self.emotional_state == "angry":
            thought += f"I'm still furious about what happened earlier... The player betrayed me.\n"

        if self.memory:
            recent_event = random.choice(self.memory)
            thought += f"That was a crazy event, when {recent_event}. I wonder if it will happen again.\n"

        if self.current_location:
            thought += f"Right now, I’m in {self.current_location}. It's so quiet here... too quiet.\n"

        return thought

    def generate_speech(self):
        """Generate a dynamic sentence based on thoughts and context."""
        thought = self.generate_thoughts()
        
        # Randomized response generation based on NPC's relationships
        if "player" in self.relationships:
            relationship = self.relationships["player"]
            if relationship == "friendly":
                return f"{thought}Oh, the player is a true friend. I should help them more."
            elif relationship == "hostile":
                return f"{thought}I don’t trust the player. I’ll watch my back around them."

        # Default generic response
        return f"{thought}What was I even thinking about again? Oh well, life goes on."

# Example usage
npc = NPC("Grim", "brooding")
npc.set_location("a dark alley")
npc.remember("the player gave me gold")
npc.update_emotion("angry")
npc.update_relationship("player", "hostile")

print(npc.generate_speech())


class WorldEvent:
    def __init__(self, event_type, description):
        self.event_type = event_type
        self.description = description
        self.timestamp = random.randint(0, 100)  # Time-based event trigger

    def trigger(self):
        """Randomize the event impact on NPCs."""
        if self.event_type == "riot":
            return "A riot broke out in the town square!"
        elif self.event_type == "weather_change":
            return "It’s suddenly started raining. Should I head back inside?"
        return "An unknown event has happened."

# World event and NPC reaction example
world_event = WorldEvent("riot", "A riot broke out in the town square!")
npc.remember(world_event.trigger())  # Add the world event to the NPC’s memory
npc.update_emotion("anxious")

print(npc.generate_speech())

