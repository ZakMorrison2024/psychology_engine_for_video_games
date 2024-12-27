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
    
    # Tokenize sentence into words (basic space split for simplicity)
    words = sentence.lower().split()
    
    for word in words:
        for category in word_weights:
            if word in word_weights[category]:
                word_weight = word_weights[category][word]
                adjusted_weight = word_weight * bias[category]  # Apply bias to weight
                score += adjusted_weight
                
    return score

def generate_dynamic_sentence(context):
    """Generate a sentence and adjust its components based on context."""
    # Choose a base sentence (simplified for demonstration)
    sentences = [
        "I feel happy today",
        "The surroundings are noisy",
        "I think we should run",
        "The air is peaceful and quiet",
        "That was a bad idea",
        "It feels like a great opportunity"
    ]
    
    # Randomly select a sentence
    sentence = random.choice(sentences)
    
    # Calculate its score
    score = calculate_sentence_score(sentence, context)
    
    # Return the sentence with its score (and perhaps modify sentence based on score)
    return sentence, score

# Example usage:
context = "peaceful"  # Can be "peaceful", "tense", or "neutral"
sentence, score = generate_dynamic_sentence(context)
print(f"Generated Sentence: {sentence}")
print(f"Sentence Score: {score}")


