class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        final = set(sentence)
        if len(final) == 26:
            return True
        else:
            return False

# Step 1: Converting  the string into a set. So that duplicate letters are removed.
# Step 2: If it's a Pangram, then the length of the string must be 26.