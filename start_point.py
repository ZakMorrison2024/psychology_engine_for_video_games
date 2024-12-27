import random

# Step 1: Define Semantic Categories (Casual Contexts)
contexts = [
    "On a quiet afternoon",
    "In the middle of the city",
    "At the park",
    "While sitting at the coffee shop",
    "During a peaceful walk",
    "At the grocery store",
    "In the living room",
    "While waiting for the bus",
    "In the bustling town square",
    "In the marketplace",
    "On the outskirts of the city",
    "In the player’s home",
    "While exploring the forest",
    "At the guild hall",
    "On the battlefield",
    "In the town library"
]

subjects = [
    "the cat",
    "a stranger",
    "the young girl",
    "a single leaf",
    "the mechanic",
    "the merchant",
    "the adventurer",
    "a guard",
    "the engineer"
]

objects = [
    "whispered secrets to the shadows",
    "slipped silently into the alley",
    "watched the stars with longing",
    "tumbled across the cobblestone street",
    "traded goods with a passing traveler",
    "crafted a new item in the workshop",
    "explored the dark cave",
    "gathered resources from the forest",
    "watched the stars while resting",
    "built a new building in the town"
]

# Step 2: Define Filters and Game Input Check
undesirable_keywords = {"hate", "stupid", "meaningless", "die"}

def contains_undesirable(sentence):
    """Check for undesirable words."""
    for word in undesirable_keywords:
        if word in sentence:
            return True
    return False

def is_incomprehensible(sentence):
    """Check if the sentence lacks basic coherence."""
    # Simple check for coherence: make sure there's a subject and an object
    if sentence.count(",", 0) != 1:
        return False
    subject, obj = sentence.split(",", 1)
    return subject.strip() == obj.strip()

# Step 3: Dynamic Game Inputs (Context, Subject, and Action Variables)
def check_game_inputs(context, subject, action, game_variables):
    """Ensure the inputs are valid and related to the simulation game, adjusting based on variables."""
    # Dynamically adjust the subject, context, or action based on game variables (e.g., player position, quest status)
    if game_variables.get("location") == "battlefield" and subject == "the player":
        context = "On the battlefield"
        action = "fought bravely against the enemies"
    
    if game_variables.get("quest_status") == "completed" and subject == "the merchant":
        action = "celebrated the completion of the quest"
    
    if game_variables.get("player_health") < 20 and subject == "the player":
        context = "In the player’s home"
        action = "rested to regain strength"

    # Ensure the subject is a valid character
    valid_subjects = ["the merchant", "the adventurer", "a guard", "the engineer"]
    if subject not in valid_subjects:
        raise ValueError(f"Invalid subject: {subject}")

    # Ensure the context is valid for a simulation game
    valid_contexts = [
        "In the bustling town square", "In the marketplace", "On the outskirts of the city", "In the player’s home",
        "While exploring the forest", "At the guild hall", "On the battlefield", "In the town library"
    ]
    if context not in valid_contexts:
        raise ValueError(f"Invalid context: {context}")

    # Ensure the action is valid for a simulation game
    valid_actions = [
        "traded goods with a passing traveler", "crafted a new item in the workshop", "explored the dark cave",
        "gathered resources from the forest", "watched the stars while resting", "built a new building in the town",
        "fought bravely against the enemies", "celebrated the completion of the quest", "rested to regain strength"
    ]
    if action not in valid_actions:
        raise ValueError(f"Invalid action: {action}")
    
    return context, subject, action

# Step 4: Egoify Filter - Modify only the subject part
def egoify_subject(sentence):
    """Modify the subject to be self-centered."""
    if "I" not in sentence and "myself" not in sentence:
        # Egoify the subject part, changing it to "I"
        sentence = sentence.replace(random.choice(subjects), "I")
    return sentence

# Step 5: Generate Sentences with Game Input Variables
def generate_sentence(game_variables):
    """Combine semantic categories into a sentence based on dynamic game variables."""
    context = random.choice(contexts)
    subject = random.choice(subjects)
    action = random.choice(objects)

    # Adjust based on the game state and input variables
    try:
        context, subject, action = check_game_inputs(context, subject, action, game_variables)
    except ValueError as e:
        print(e)
        return None
    
    sentence = f"{context}, {subject} {action}."
    return sentence

# Step 6: Speech Engine with Filtering and Random Egoification
def speech_engine(game_variables):
    """Generate and filter sentences, then randomly egoify a percentage of them."""
    for _ in range(10):  # Generate a batch of sentences
        sentence = generate_sentence(game_variables)
        if sentence and not contains_undesirable(sentence) and not is_incomprehensible(sentence):
            # Randomly decide whether to apply the ego transformation
            if random.random() < 0.25:  # 25% chance to egoify
                sentence = egoify_subject(sentence)
            print(sentence)

# Game variables that can dynamically change based on the game state
game_variables = {
    "location": "battlefield",  # Example: The player is on the battlefield
    "quest_status": "completed",  # Example: A quest has been completed
    "player_health": 50  # Example: The player's health is at 50%
}

# Run the speech engine with th
