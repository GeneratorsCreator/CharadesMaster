import random

# Define lists of characters for different age groups
characters_3_4 = ['Elmo', 'Minnie Mouse', 'Daniel Tiger', 'Peppa Pig']
characters_5_6 = ['Buzz Lightyear', 'Lightning McQueen', 'Doc McStuffins', 'Elena of Avalor']
characters_7_8 = ['Rapunzel', 'Spider-Man', 'Captain America', 'Mickey Mouse', 'Dora the Explorer']
characters_9_10 = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Elsa', 'Anna', 'Olaf', 'Pikachu', 'Iron Man']
characters_11_12 = ['Katniss Everdeen', 'Sherlock Holmes', 'Captain Marvel', 'Black Panther', 'Spider-Man']
characters_13_14 = ['Buffy Summers', 'Tony Stark', 'Wonder Woman', 'Hawkeye', 'Loki', 'Harley Quinn']

# Define function to generate a character based on age group
def generate_character(age):
    if age >= 3 and age <= 4:
        return random.choice(characters_3_4)
    elif age >= 5 and age <= 6:
        return random.choice(characters_5_6)
    elif age >= 7 and age <= 8:
        return random.choice(characters_7_8)
    elif age >= 9 and age <= 10:
        return random.choice(characters_9_10)
    elif age >= 11 and age <= 12:
        return random.choice(characters_11_12)
    elif age >= 13 and age <= 14:
        return random.choice(characters_13_14)
    else:
        return "Sorry, we don't have any characters suitable for your age group."

# Define function to prompt user for age and generate a character
def main():
    print("Welcome to CharadesMaster V1!")
    while True:
        age = input("Enter your age (or q to quit): ")
        if age == 'q':
            break
        age = int(age)
        character = generate_character(age)
        print("Your charades character is:", character)
        play_again = input("Generate another character? (y/n): ")
        if play_again == 'n':
            break

# Call main function to run the program
main()
