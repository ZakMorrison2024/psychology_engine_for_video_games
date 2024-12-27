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
    "While waiting for the bus"
]

subjects = [
    "the cat",
    "a stranger",
    "the young girl",
    "a single leaf",
    "the mechanic"
]

objects = [
    "whispered secrets to the shadows",
    "slipped silently into the alley",
    "watched the stars with longing",
    "tumbled across the cobblestone street"
]

# Step 2: Define Filters
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

# Step 3: Egoify Filter - Modify only the subject part
def egoify_subject(sentence):
    """Modify the subject to be self-centered."""
    if "I" not in sentence and "myself" not in sentence:
        # Egoify the subject part, changing it to "I"
        sentence = sentence.replace(random.choice(subjects), "I")
    return sentence

# Step 4: Generate Sentences
def generate_sentence():
    """Combine semantic categories into a sentence."""
    context = random.choice(contexts)
    subject = random.choice(subjects)
    obj = random.choice(objects)
    sentence = f"{context}, {subject} {obj}."
    return sentence

# Step 5: Speech Engine with Filtering and Random Egoification
def speech_engine():
    """Generate and filter sentences, then randomly egoify a percentage of them."""
    for _ in range(10):  # Generate a batch of sentences
        sentence = generate_sentence()
        if not contains_undesirable(sentence) and not is_incomprehensible(sentence):
            # Randomly decide whether to apply the ego transformation
            if random.random() < 0.25:  # 25% chance to egoify
                sentence = egoify_subject(sentence)
            print(sentence)

# Run the speech engine
speech_engine()
