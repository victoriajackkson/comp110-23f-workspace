"""EX01- Chardle- A cute step toward Wordle"""
__author__= "730400711"

# Generating input for word guess
# Checking length of word and character input

word: str = input("Enter a 5-character word: ")
if len(word)!= 5:
    print("Error: Word must contain 5 characters")
    exit()
chr: str = input("Enter a single character: ")
if len(chr)!= 1:
        print("Error: Character must be a single character.")
        exit()
print("Searching for ",  chr , "in",  word)

# Initializing the string I want to count the instances of
# Initializing counter for number of instances of the character inputed for a word
inst_of_chr: int = 0

if (word[0]) == chr:
    print(chr,  "found at index 0")
    inst_of_chr = inst_of_chr +1

if (word[1]) == chr:
    print(chr,  "found at index 1")
    inst_of_chr = inst_of_chr +1

if str(word[2]) == chr:
    print(chr,  "found at index 2")
    inst_of_chr = inst_of_chr +1

if str(word[3]) == chr:
    print(chr,  "found at index 3")
    inst_of_chr = inst_of_chr +1

if str(word[4]) == chr:
    print(chr,  "found at index 4")
    inst_of_chr = inst_of_chr +1

if inst_of_chr == 1: 
    print (inst_of_chr,  "instance of",  chr, "found in",  word)
else:
    print(inst_of_chr, "instances of", chr , "found in",  word)
if inst_of_chr == 0:
    print ("No instances of",  chr , "found in", word)

