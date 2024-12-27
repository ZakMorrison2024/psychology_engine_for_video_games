import random

# Word weights based on categories
word_weights = {
    "emotion": {
        "happy": 3,
        "joyful": 3,
        "sad": -2,
        "angry": -3,
        "excited": 2,
        "neutral": 0,
    },
    "action": {
        "help": 3,
        "fight": -2,
        "talk": 1,
        "run": 1,
        "think": 2,
        "avoid": -1,
    },
    "context": {
        "quiet": 2,
        "noisy": -1,
        "dark": -1,
        "bright": 2,
        "crowded": -2,
        "peaceful": 3,
    },
    "polarity": {
        "good": 3,
        "bad": -3,
        "neutral": 0,
        "great": 4,
        "terrible": -4,
    },
}

def adjust_bias_for_context(context):
    """Adjust word weights based on context."""
    bias = {
        "peaceful": {
            "emotion": 1.2,
            "action": 1.1,
            "polarity": 1.5,
            "context": 1.3
        },
        "tense": {
            "emotion": 0.8,
            "action": 1.3,
            "polarity": 1.8,
            "context": 0.9
        },
        "neutral": {
            "emotion": 1.0,
            "action": 1.0,
            "polarity": 1.0,
            "context": 1.0
        }
    }
    
    return bias.get(context, bias["neutral"])

def calculate_sentence_score(sentence, context):
    """Calculate the total score of a sentence based on word weights and context bias."""
    bias = adjust_bias_for_context(context)
    score = 0
    
    # Tokenize sentence into words (simplified for demonstration)
    words = sentence.lower().split()
    
    for word in words:
        for category in word_weights:
            if word in word_weights[category]:
                word_weight = word_weights[category][word]
                adjusted_weight = word_weight * bias[category]  # Apply bias to weight
                score += adjusted_weight
                
    return score

def generate_dynamic_sentence(context, npc_emotion="neutral", npc_action="thinking"):
    """Generate a sentence based on context, emotion, and action."""
    # Possible components for sentence generation
    possible_subjects = ["the NPC", "the player", "a guard", "the merchant", "an adventurer"]
    possible_actions = {
        "thinking": ["is considering the situation", "is pondering the consequences", "is lost in thought"],
        "talking": ["speaks to you cautiously", "whispers to a nearby NPC", "shouts across the street"],
        "fighting": ["bravely faces the enemy", "launches into battle", "defends their position"],
        "helping": ["offers their assistance", "gives you a hand", "lends you support"]
    }
    
    # Randomly choose components
    subject = random.choice(possible_subjects)
    action = random.choice(possible_actions.get(npc_action, ["is unsure what to do"]))
    
    # Generate sentence based on the chosen subject, action, and context
    sentence = f"{subject} {action}."
    
    # Calculate its score (and possibly modify based on score)
    score = calculate_sentence_score(sentence, context)
    
    return sentence, score

# Word-based speech generator
def generate_sentence(game_variables):
    """Combine semantic categories into a sentence based on dynamic game variables."""
    contexts = [
        "On a quiet afternoon", "In the middle of the city", "At the park", "While sitting at the coffee shop",
        "During a peaceful walk", "At the grocery store", "In the living room", "While waiting for the bus",
        "In the bustling town square", "In the marketplace", "On the outskirts of the city", "In the player’s home",
        "While exploring the forest", "At the guild hall", "On the battlefield", "In the town library"
    ]

    subjects = [
        "the cat", "a stranger", "the young girl", "a single leaf", "the mechanic", "the merchant",
        "the adventurer", "a guard", "the engineer"
    ]

    objects = [
        "whispered secrets to the shadows", "slipped silently into the alley", "watched the stars with longing",
        "tumbled across the cobblestone street", "traded goods with a passing traveler", "crafted a new item in the workshop",
        "explored the dark cave", "gathered resources from the forest", "watched the stars while resting",
        "built a new building in the town"
    ]

    context = random.choice(contexts)
    subject = random.choice(subjects)
    action = random.choice(objects)

    # Adjust based on the game state and input variables
    if game_variables.get("location") == "battlefield" and subject == "the player":
        context = "On the battlefield"
        action = "fought bravely against the enemies"

    if game_variables.get("quest_status") == "completed" and subject == "the merchant":
        action = "celebrated the completion of the quest"

    if game_variables.get("player_health") < 20 and subject == "the player":
        context = "In the player’s home"
        action = "rested to regain strength"

    sentence = f"{context}, {subject} {action}."
    return sentence

def speech_engine(game_variables):
    """Generate and filter sentences, then randomly egoify a percentage of them."""
    undesirable_keywords = {"hate", "stupid", "meaningless", "die"}

    def contains_undesirable(sentence):
        for word in undesirable_keywords:
            if word in sentence:
                return True
        return False

    def is_incomprehensible(sentence):
        if sentence.count(",", 0) != 1:
            return False
        subject, obj = sentence.split(",", 1)
        return subject.strip() == obj.strip()

    def egoify_subject(sentence):
        if "I" not in sentence and "myself" not in sentence:
            sentence = sentence.replace(random.choice(subjects), "I")
        return sentence

    for _ in range(10):
        sentence = generate_sentence(game_variables)
        if sentence and not contains_undesirable(sentence) and not is_incomprehensible(sentence):
            if random.random() < 0.25:  # 25% chance to egoify
                sentence = egoify_subject(sentence)
            print(sentence)

# Example usage
game_variables = {
    "location": "battlefield",
    "quest_status": "completed",
    "player_health": 50
}

speech_engine(game_variables)

npc_state = {
    "emotion": "neutral",
    "action": "thinking",
    "interaction_history": [],
}

def npc_thought_process():
    """Generate an internal thought for the NPC based on their state and context."""
    if npc_state["emotion"] == "happy":
        thought = "The day feels good, maybe I should offer help."
    elif npc_state["emotion"] == "sad":
        thought = "Everything seems off today, I should stay quiet."
    elif npc_state["action"] == "thinking":
        thought = "I need to assess the situation before taking action."
    else:
        thought = "I don't know what to do, but I’ll just keep going."
    return thought

def update_npc_interaction_history(player_action):
    """Update NPC's interaction history."""
    npc_state["interaction_history"].append(player_action)
    if len(npc_state["interaction_history"]) > 5:
        npc_state["interaction_history"].pop(0)

    if "helped" in npc_state["interaction_history"]:
        npc_state["emotion"] = "happy"
    elif "hurt" in npc_state["interaction_history"]:
        npc_state["emotion"] = "angry"
    else:
        npc_state["emotion"] = "neutral"

def main():
    context = "peaceful"
    npc_emotion = "happy"
    npc_action = "helping"

    thought = npc_thought_process()
    print(f"NPC Thought: {thought}")

    sentence, score = generate_dynamic_sentence(context, npc_emotion, npc_action)
    print(f"Generated Sentence: {sentence}")
    print(f"Sentence Score: {score}")

main()
