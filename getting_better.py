import random

# Define placeholders for dynamic vocabulary and game contexts
PLACEHOLDERS = {
    "contexts": [],  # Placeholder for environment contexts
    "subjects": [],  # Placeholder for NPCs, players, and other characters
    "actions": [],   # Placeholder for actions the subjects perform
    "objects": []    # Placeholder for objects or results of actions
}

# Word weights for dynamic scoring based on categories
word_weights = {
    "emotion": {},  # Placeholder for emotion-based words
    "action": {},   # Placeholder for action-based words
    "context": {},  # Placeholder for context-based words
    "polarity": {}  # Placeholder for polarity-based words
}

def set_placeholders(contexts, subjects, actions, objects):
    """Set the placeholder values based on game-specific contexts."""
    PLACEHOLDERS["contexts"] = contexts
    PLACEHOLDERS["subjects"] = subjects
    PLACEHOLDERS["actions"] = actions
    PLACEHOLDERS["objects"] = objects

def set_word_weights(emotion, action, context, polarity):
    """Set the word weights dynamically based on game-specific values."""
    word_weights["emotion"] = emotion
    word_weights["action"] = action
    word_weights["context"] = context
    word_weights["polarity"] = polarity

def adjust_bias_for_context(context):
    """Adjust word weights based on dynamic game context."""
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

def generate_dynamic_sentence(game_state):
    """Generate a sentence based on the game's current state and placeholders."""
    # Fetch components dynamically from placeholders
    context = random.choice(PLACEHOLDERS["contexts"])
    subject = random.choice(PLACEHOLDERS["subjects"])
    action = random.choice(PLACEHOLDERS["actions"])
    obj = random.choice(PLACEHOLDERS["objects"])

    # Generate sentence
    sentence = f"{context}, {subject} {action} {obj}."

    # Calculate its score
    score = calculate_sentence_score(sentence, game_state.get("context", "neutral"))

    return sentence, score

def npc_thought_process(npc_state):
    """Generate an internal thought for the NPC based on its state and context."""
    emotion = npc_state.get("emotion", "neutral")
    if emotion == "happy":
        thought = "The day feels good, maybe I should offer help."
    elif emotion == "sad":
        thought = "Everything seems off today, I should stay quiet."
    elif npc_state.get("action") == "thinking":
        thought = "I need to assess the situation before taking action."
    else:
        thought = "I don't know what to do, but I’ll just keep going."
    
    return thought

def speech_engine(game_state, npc_state):
    """Generate and filter sentences dynamically based on game state and NPC state."""
    for _ in range(10):  # Generate a batch of sentences
        sentence, score = generate_dynamic_sentence(game_state)
        if sentence and score > 0:  # Filter undesirable or incoherent sentences
            print(sentence)

# Example setup for game-specific placeholders and weights
set_placeholders(
    contexts=["In the bustling town square", "On the battlefield", "While exploring the forest"],
    subjects=["the NPC", "the player", "a guard"],
    actions=["is gathering", "is fighting", "is exploring"],
    objects=["resources", "enemies", "treasures"]
)

set_word_weights(
    emotion={"happy": 3, "sad": -2},
    action={"fight": -2, "explore": 2},
    context={"forest": 2, "battlefield": -3},
    polarity={"good": 3, "bad": -3}
)

# Example game state and NPC state
example_game_state = {"context": "peaceful"}
example_npc_state = {"emotion": "happy", "action": "exploring"}

# Run the speech engine
speech_engine(example_game_state, example_npc_state)
