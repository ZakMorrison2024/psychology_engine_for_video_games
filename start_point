Step 1: Define Semantic Categories
contexts = [
"In the quiet of the night",
"Amidst the bustling crowd",
"Under the pale moonlight",
"As the rain poured down"
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

Step 2: Define Filters
undesirable_keywords = {"hate", "stupid", "meaningless", "die"}
incomprehensible_patterns = ["noun + abstract noun", "adjective + verb"]

def contains_undesirable(sentence):
"""Check for undesirable words."""
for word in undesirable_keywords:
if word in sentence:
return True
return False

def is_incomprehensible(sentence):
"""Check if the sentence lacks basic coherence."""
# Simplistic example: Ensure Subject and Object are distinct
subject, obj = sentence.split(",")[1:], sentence.split(",")[:1]
return subject == obj

Step 3: Generate Sentences
def generate_sentence():
"""Combine semantic categories into a sentence."""
context = random.choice(contexts)
subject = random.choice(subjects)
obj = random.choice(objects)
sentence = f"{context}, {subject} {obj}."
return sentence

Step 4: Speech Engine with Filtering
def speech_engine():
"""Generate and filter sentences."""
for _ in range(10): # Generate a batch of sentences
sentence = generate_sentence()
if not contains_undesirable(sentence) and not is_incomprehensible(sentence):
print(sentence)

Run the speech engine
speech_engine()
