print(" think of a number between 1 to 100, i will guess it ")
low = 1
high = 100
guesses = 0
while True:
    guess = (low + high) // 2
    guesses += 1
    print(f"My guess is: {guess}")
    feedback = input("Is it too low (L), too high (H), or correct (C)? ").upper()
    if feedback == 'C':
        print(f"Yay! I guessed your number {guess} in {guesses} attempts.")
        break
    elif feedback == 'L':
        low = guess + 1
    elif feedback == 'H':
        high = guess - 1
    else:
        print("Invalid input. Please enter L, H, or C.")
        