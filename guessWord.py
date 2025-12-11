import random as r


print (f'Hello Buddy!! How are You. Lets Start the Game')


words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = r.choice(words)

guesses = set()
turns = len(word)

while turns>0 :
    display = ""
    missed = 0

    for char in word:
        
        if char in guesses:
            display += char + " "

        else:
            display += "_ "
            missed += 1

    print(display.strip())

    if missed == 0:
        print(f"Hurray! You won it!! The word is '{word}'.")
        break

    guess = input("guess a character: ").lower()

    if not guess or len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter a single alphabet.")
        continue

    if guess in guesses:
        print("You already guessed that. Try something else.")
        continue

    guesses.add(guess)

    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print(f"You have {turns} turns left.")

if turns == 0:
    print(f"You Lost it Buddy. The Word was {word}")