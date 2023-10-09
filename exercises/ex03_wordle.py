"""EX03- Structured Wordle."""
__author__ = "730400711"


# Creating function that will see if character from guess is found in secret word
def contains_char(guess: str, char: str) -> bool:
    """Returns T/F character found in string."""
    assert len(char) == 1
    index: int = 0
    while index < len(guess):
        if char == guess[index]:
            return True
        index = index + 1
    else:
        return False


# Creating function for emojifying guessed characters found (or not) in secret word
def emojified(guess: str, secret: str) -> str:
    """Returns string of emojis whose color codifies correct/incorrect letters found in secret word."""
    assert len(guess) == len(secret)
    index: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    box: str = ""
    
    while index < len(guess):
        if guess[index] == secret[index]:
            box = box + GREEN_BOX
        else: 
            if contains_char(secret, guess[index]):
                box = box + YELLOW_BOX
            else:
                box = box + WHITE_BOX
        index = index + 1
    return box


# Creating function for user input for guess word. Checking if guess is correct length.
def input_guess(expected: int) -> str:
    """Returns prompt for user to input guess of expected length, correct length isn't given, prompt again."""
    player_guess = input(f"Enter a {expected} character word: ")
    while len(player_guess) != expected:
        player_guess = input(f"That wasn't {expected} chars! Try again: ")
    return player_guess


# Declaring main function
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    win: str = "codes"
    result: str = ""
    while turns <= 6 and result != win:
        print(f"=== Turn {turns}/6 ===")
        result = input_guess(len(win))
        print(emojified(result, win))
        turns = turns + 1

    # Printing result if user is out of turns and incorrect, or if they've guessed correctly at or under 6 turns.
    if turns >= 6 and result != win:
        print("X/6 - Sorry, try again tomorrow!")
    if result == win:
        print(f"You won in {turns-1}/6 turns!")


if __name__ == "__main__":
    main()