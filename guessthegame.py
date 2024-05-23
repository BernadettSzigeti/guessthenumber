import random

def generate_number():
    return random.randint(1, 100)

def check_guess(guess, number):
    if guess < number:
        return "Too low"
    elif guess > number:
        return "Too high"
    else:
        return "Congratulations! You guessed it!"

def main():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    number = generate_number()
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            result = check_guess(guess, number)
            print(result)
            
            if result == "Congratulations! You guessed it!":
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
