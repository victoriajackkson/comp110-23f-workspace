"""EX02- One-Shot Wordle-Loops!"""
__author__ = "730400711"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "python"
guess: str = str(input(f"What is your {len(secret)}-letter guess? "))


while len(guess) != len(secret):
    # Reassigning guess variable to ask for player input again
    guess = input(f"That was not {len(secret)} letters! Try again: ")
    # Checking to see if any guessed characters are present in the indices of the secret
index: int = 0
emoji: str = ""

while index < len(secret):
    # Checking to see if index of guess is equal to that of the secret
    if guess[index] == secret[index]:
        emoji = emoji + GREEN_BOX
    # Setting up boolean for characters in guess. Creating count for guessed characters in wrong place.
    else:
        guessed_chr: bool = False
        alt_index: int = 0
        while not guessed_chr and alt_index < len(secret):
            if secret[alt_index] == guess[index]:
                guessed_chr = True
            else:
                alt_index = alt_index + 1
# Checking guessed characters that are true but in wrong spot and those that are not true at all.
        if guessed_chr:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1
# Printing the resulting emojis of guessed characters found/not found in secret word
print(emoji)

if guess == secret:
    print("Woo! You got it! ")
else:
    print("Not quite. Play again soon! ")
    