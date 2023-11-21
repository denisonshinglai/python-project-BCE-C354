import random

rand = random.randint(1, 100)
guesses = [0]

print("WELCOME TO 'GUESS THE NUMBER!'")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
    guess = int(input('Guess the number: '))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS')
        continue

    if guess == rand:
        print(f'Congratulations! You guessed the number in {len(guesses)} attempts.')
        break

    guesses.append(guess)

    if len(guesses) == 2:
        if abs(rand - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(rand - guess) < abs(rand - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

