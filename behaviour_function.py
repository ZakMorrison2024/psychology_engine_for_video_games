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
        if emotion_rating <= 2:  # Miserable or Sad -> less likely to take action
            modifier = -10
        elif emotion_rating >= 8:  # Happy or Ecstatic -> more likely to take action
            modifier = 10
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
