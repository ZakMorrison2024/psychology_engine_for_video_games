import random
# Word weights based on emotion, action, context, and polarity
word_weights = {
    "emotion": {
        "happy": 3, "sad": -2, "angry": -3, "excited": 4, "anxious": -1,
        "joyful": 3, "fearful": -2, "hopeful": 2, "content": 2, "bored": -1,
        "relieved": 2, "guilty": -2, "surprised": 1, "disappointed": -3,
        "frustrated": -2, "loving": 4, "grateful": 3, "lonely": -3, 
        "ashamed": -3, "proud": 3, "envious": -1, "jealous": -2, "calm": 2
    },
    "action": {
        "fight": -2, "explore": 2, "run": 1, "rest": 1, "argue": -2, 
        "help": 3, "ignore": -1, "listen": 2, "talk": 1, "shout": -2,
        "laugh": 3, "cry": -2, "smile": 3, "think": 2, "give": 3, "receive": 2,
        "work": 1, "rest": 1, "plan": 2, "wait": -1, "search": 2, 
        "celebrate": 3, "hide": -2, "discuss": 2, "fight": -2, "negotiate": 1,
        "create": 3, "destroy": -3, "travel": 2, "reflect": 2, "assist": 3
    },
    "context": {
        "forest": 2, "battlefield": -3, "city": 1, "home": 3, "office": 1,
        "park": 2, "beach": 3, "mountain": 2, "street": 1, "desert": -2,
        "village": 2, "school": 1, "market": 2, "library": 3, "restaurant": 3,
        "hospital": -2, "store": 1, "factory": -1, "jungle": 2, "meadow": 3,
        "countryside": 2, "airport": 1, "train station": 1, "stadium": 2,
        "workplace": 1, "courtroom": -1, "concert hall": 3, "theater": 3,
        "gym": 2, "hotel": 2, "bar": 1, "nightclub": 1, "museum": 3, 
        "forest clearing": 2, "desolate wasteland": -3, "highway": 1
    },
    "polarity": {
        "good": 3, "bad": -3, "positive": 2, "negative": -2, "neutral": 0,
        "right": 3, "wrong": -3, "fair": 2, "unfair": -2, "beneficial": 3,
        "harmful": -3, "just": 3, "unjust": -3, "kind": 3, "cruel": -3, 
        "loving": 4, "hateful": -4, "helpful": 3, "hurtful": -3, "strong": 2,
        "weak": -2, "bright": 2, "dark": -2, "valuable": 3, "worthless": -3,
        "successful": 3, "failure": -3, "truth": 3, "lie": -3, "honest": 3,
        "dishonest": -3, "pleasant": 2, "unpleasant": -2, "fortunate": 3, 
        "unlucky": -2, "lucky": 3, "unfortunate": -3, "loved": 4, "unloved": -3
    }
}
# Define placeholders for dynamic vocabulary and game contexts (This should be fed in by in-game data)
PLACEHOLDERS = {
    "contexts": [],  # Placeholder for environment contexts
    "subjects": [],  # Placeholder for NPCs, players, and other characters
    "actions": [],   # Placeholder for actions the subjects perform
    "objects": []    # Placeholder for objects or results of actions
}

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

    def adjust_bias_for_emotion(emotion_rating):
    """Adjust the bias dynamically based on the emotional rating (1-10 scale)."""
    # Emotional state determines the bias adjustment for different categories
    bias = {
        "emotion": 1.0 + 0.2 * (emotion_rating - 5),  # Neutral is 1.0, positive emotions increase, negative decrease
        "action": 1.0 + 0.1 * (emotion_rating - 5),   # Neutral is 1.0, positive actions are more likely with higher emotions
        "polarity": 1.0 + 0.1 * (emotion_rating - 5),  # Neutral is 1.0, more positive with higher emotions
        "context": 1.0 + 0.2 * (emotion_rating - 5)    # Neutral is 1.0, more positive context with higher emotions
    }
    
    return bias

    def adjust_ego(self, npc_ego):
        """Adjust weights based on ego level."""
        if npc_ego > 7:
            return "superior"  # Confident, self-important
        elif npc_ego < 3:
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

    def calculate_sentence_score(sentence, emotion_rating):
    """Calculate the total score of a sentence based on word weights and emotion-based bias."""
    # Adjust weights based on emotional state (1-10 scale)
    adjusted_weights = adjust_word_weights_based_on_emotion(emotion_rating)
    
    # Adjust bias for the sentence based on emotional state
    bias = adjust_bias_for_emotion(emotion_rating)
    
    score = 0
    # Tokenize sentence into words (simplified for demonstration)
    words = sentence.lower().split()
    
    # Apply word weights and biases to calculate score
    for word in words:
        for category in adjusted_weights:
            if word in adjusted_weights[category]:
                word_weight = adjusted_weights[category][word]
                adjusted_weight = word_weight * bias[category]  # Apply bias to weight
                score += adjusted_weight
                
    return score
        
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

    def generate_sentence(self, npc_ego, emotion_rating):
        """Combine dynamic vocabulary into a coherent sentence."""
        """Generate a sentence with adjusted weights based on NPC's emotional state."""
        adjusted_weights = self.apply_emotion_bias(emotion_rating)
        ego_modifier = self.adjust_ego(npc_ego)
        # Select words from each category based on the adjusted weights or fallback to random choice
        context = self.generate_weighted_word("context", adjusted_weights) if self.contexts else random.choice(self.contexts) if self.contexts else "In an undefined context"
        subject = self.generate_weighted_word("emotion", adjusted_weights) if self.subjects else random.choice(self.subjects) if self.subjects else "someone"
        action = self.generate_weighted_word("action", adjusted_weights) if self.actions else random.choice(self.actions) if self.actions else "does something"
        obj = self.generate_weighted_word("polarity", adjusted_weights) if self.objects else random.choice(self.objects) if self.objects else "somewhere"
        # Gen
        sentence = f"{context}, {subject} {action} {obj}."
        sentence = self.apply_ego_to_sentence(sentence, ego_modifier)
      
        return sentence


class ThoughtProcessor:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

  def generate_thought(self, npc_state):
    """Generate a thought for the NPC based on their current state."""
    # Apply emotion-based adjustments
    emotion_rating = npc_state.get("emotion", 5)
    adjusted_weights = self.vocabulary.apply_emotion_bias(emotion_rating)

    # Attempt to generate words based on emotional weights
    context = self.vocabulary.generate_weighted_word("context", adjusted_weights) if self.vocabulary.contexts else "In an undefined context"
    subject = self.vocabulary.generate_weighted_word("emotion", adjusted_weights) if self.vocabulary.subjects else "someone"
    action = self.vocabulary.generate_weighted_word("action", adjusted_weights) if self.vocabulary.actions else "does something"
    obj = self.vocabulary.generate_weighted_word("polarity", adjusted_weights) if self.vocabulary.objects else "somewhere"

    # If vocabulary is empty or weighted generation fails, fall back to random choices
    if not context or not subject or not action or not obj:
        thought_components = {
            "contexts": self.vocabulary.contexts,
            "subjects": self.vocabulary.subjects,
            "actions": self.vocabulary.actions,
            "objects": self.vocabulary.objects,
        }

        context = random.choice(thought_components["contexts"]) if self.vocabulary.contexts else "In an undefined context"
        subject = random.choice(thought_components["subjects"]) if self.vocabulary.subjects else "someone"
        action = random.choice(thought_components["actions"]) if self.vocabulary.actions else "does something"
        obj = random.choice(thought_components["objects"]) if self.vocabulary.objects else "somewhere"

    # Assemble a dynamic thought
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

    def action_chance(self, action, context, npc_state):
        """
        Determine if an action occurs based on a chance likelihood (0-100%),
        influenced by the game's context (positive or negative).
        :param action: The action to be performed (e.g., "shoot", "help").
        :param context: The context of the action (e.g., "positive" or "negative").
        :param npc_state: The NPC's current state (to factor in emotion).
        :return: True if the action occurs, False otherwise.
        """
        if not (0 <= context <= 100):
            raise ValueError("Context must be 'positive' or 'negative'.")

        # Base likelihood (from game logic, typically a percentage)
        base_likelihood = random.randint(1, 100)

        # Modify likelihood based on the NPC's emotional state
        emotion_rating = npc_state.get("emotion", 5)  # Default to neutral if undefined

        # Adjust likelihood based on the emotion rating
        if emotion_rating <= 4 and emotion_rating > 2:  # Miserable or Sad -> less likely to take action
            modifier = -10
        elif emotion_rating <= 2: 
            modifier = -25
        elif emotion_rating >= 6 and emotion_rating < 8:  # Happy or Ecstatic -> more likely to take action
            modifier = 10
        elif emotion_rating >= 8:  
            modifier = 25
        else:  # Neutral -> no change
            modifier = 0

        # Increase or decrease based on the context of the action
        if context == "negative":
            modifier -= 10  # Negative context (e.g., attacking) reduces likelihood
        elif context == "positive":
            modifier += 10  # Positive context (e.g., helping) increases likelihood

        # Calculate final likelihood (clamped between 0 and 100)
        final_likelihood = max(0, min(100, base_likelihood + modifier))

        # Decide whether the action occurs based on the final likelihood
        action_occurred = base_likelihood <= final_likelihood
        return action_occurred


vocabulary = DynamicVocabulary()
vocabulary.set_vocabulary(
contexts = [
    "In a public space", "On a commute", "While exercising", "At a gathering", 
    "In a quiet area", "On a street", "In a store", "At home", "In a park", 
    "At work", "In a restaurant", "At a station", "On a road", "In a busy area", 
    "At a public event", "At a meeting", "In a waiting room", "At a school", 
    "In a social setting", "In a place of business", "At a recreational spot", 
    "On a trip", "In a café", "At a health club", "In a shopping center", 
    "At an activity", "At a service center", "In an open space", "In a building", 
    "In a relaxed environment", "At a function", "On a journey", "In a crowd", 
    "At a performance", "On an outing", "At an entertainment venue", "At a public place", 
    "In a community space", "At an event", "At a celebration", "In a shop", 
    "At a local spot", "In a shared space", "At a landmark", "In a neighborhood", 
    "At a gathering", "In a busy district", "On a walk", "In a peaceful spot", 
    "At a casual event", "In a familiar place", "At a routine stop"
]

subjects = [
    "a person", "an individual", "someone", "a commuter", "a traveler", 
    "a worker", "a shopper", "a visitor", "a pedestrian", "a driver", 
    "a participant", "a student", "a customer", "a guest", "a client", 
    "a member", "a visitor", "a runner", "a hiker", "a jogger", 
    "a cyclist", "a patron", "a volunteer", "a guest", "a diner", 
    "a friend", "a neighbor", "a family member", "a teammate", "a student", 
    "a colleague", "an athlete", "a performer", "a teacher", "a participant", 
    "a shopper", "a passerby", "a stranger", "a colleague", "a coach", 
    "a guide", "a resident", "a competitor", "a teammate", "a local", 
    "a mentor", "a helper", "a caregiver", "a runner", "an explorer"
]

actions = [
    "is walking", "is shopping", "is waiting", "is traveling", "is working", 
    "is studying", "is running", "is biking", "is resting", "is exercising", 
    "is dining", "is driving", "is attending", "is participating", "is reading", 
    "is socializing", "is relaxing", "is listening", "is talking", "is exploring", 
    "is volunteering", "is working out", "is resting", "is enjoying", "is helping", 
    "is cooking", "is cleaning", "is learning", "is meeting", "is playing", 
    "is observing", "is browsing", "is moving", "is relaxing", "is conversing", 
    "is traveling", "is gathering", "is sitting", "is laughing", "is shopping", 
    "is practicing", "is commuting", "is waiting", "is enjoying", "is engaging", 
    "is assisting", "is attending", "is exercising", "is participating", 
    "is enjoying", "is mentoring"
]

objects = [
    "food", "items", "supplies", "documents", "tools", "gear", "belongings", 
    "books", "bags", "equipment", "furniture", "clothing", "footwear", 
    "devices", "personal items", "materials", "accessories", "drinks", 
    "snacks", "electronics", "goods", "papers", "belongings", "bills", 
    "materials", "plans", "goods", "gadgets", "objects", "resources", 
    "products", "goods", "devices", "instruments", "toys", "records", 
    "reports", "supplies", "pieces", "vehicles", "tools", "objects", 
    "materials", "medications", "gadgets", "phones", "documents", "papers", 
    "treasures", "memorabilia", "gifts", "notes", "files"
]
)

# Ego weights example
vocabulary.set_ego_weights({
"superior": {
        "gathering": 1.5, "fighting": 2, "exploring": 1.2, 
        "shopping": 1.5, "waiting": 1.3, "running": 1.4, 
        "working": 1.7, "listening": 1.6, "relaxing": 1.4, 
        "resting": 1.3, "helping": 1.8, "socializing": 1.6, 
        "traveling": 1.5, "meeting": 1.4, "celebrating": 1.9, 
        "attending": 1.6, "playing": 1.7, "learning": 1.8, 
        "exploring": 1.5, "baking": 1.4, "creating": 2, 
        "cooking": 1.6, "performing": 1.9, "studying": 1.7, 
        "training": 1.8, "competing": 2, "exercising": 1.5, 
        "communicating": 1.5, "planning": 1.6, "observing": 1.2
    },
    "inferior": {
        "gathering": 0.8, "fighting": 0.7, "exploring": 0.9, 
        "shopping": 0.6, "waiting": 0.7, "running": 0.9, 
        "working": 0.8, "listening": 0.7, "relaxing": 0.6, 
        "resting": 0.7, "helping": 0.9, "socializing": 0.8, 
        "traveling": 0.7, "meeting": 0.8, "celebrating": 0.9, 
        "attending": 0.8, "playing": 0.9, "learning": 0.7, 
        "exploring": 0.8, "baking": 0.7, "creating": 0.6, 
        "cooking": 0.8, "performing": 0.7, "studying": 0.6, 
        "training": 0.7, "competing": 0.6, "exercising": 0.8, 
        "communicating": 0.9, "planning": 0.7, "observing": 0.8
    },
    "neutral": {
        "gathering": 1.0, "fighting": 1.0, "exploring": 1.0, 
        "shopping": 1.0, "waiting": 1.0, "running": 1.0, 
        "working": 1.0, "listening": 1.0, "relaxing": 1.0, 
        "resting": 1.0, "helping": 1.0, "socializing": 1.0, 
        "traveling": 1.0, "meeting": 1.0, "celebrating": 1.0, 
        "attending": 1.0, "playing": 1.0, "learning": 1.0, 
        "exploring": 1.0, "baking": 1.0, "creating": 1.0, 
        "cooking": 1.0, "performing": 1.0, "studying": 1.0, 
        "training": 1.0, "competing": 1.0, "exercising": 1.0, 
        "communicating": 1.0, "planning": 1.0, "observing": 1.0
    }
})


### Thins for game enviroment


#PLACEHOLDERS = {
# #   "contexts": [],  # Placeholder for environment contexts
 #   "subjects": [],  # Placeholder for NPCs, players, and other characters
#    "actions": [],   # Placeholder for actions the subjects perform
 #   "objects": []    # Placeholder for objects or results of actions
#}

#npc = NPC(name="Guard", state={"emotion": 5, "ego": 5})
#thought_processor = ThoughtProcessor(vocabulary)

# Generate a thought
#npc_thought = npc.think(thought_processor)
#print(f"NPC Thought: {npc_thought}")

# Generate a sentence based on dynamic vocabulary
#sentence = vocabulary.generate_sentence()
#print(f"Generated Sentence: {sentence}")
