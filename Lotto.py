import random

winningNumbers = []

i = 1

# wybieranie wygrywających numerów / chosing winning numbers
while i <= 6:

    a = random.randint(1, 49)

    winningNumbers.append(a)

    i += 1

age = int(input("Hello to play Lotto please enter your age: "))


if age >= 18:
    print("---You are old enough to play Lotto---")
else:
    print("---You are to young to play Lotto---")

while age >=18:
    userNumbers = []

    for y in range(6):
        try: 
            z = int(input("Enter a number between 1 and 49: (Chosing invalid numer will result in a loss) \n"))
            if 1 <= z <=49:
               userNumbers.append(z)
            else:
                print("You can only pick numbers between 1 and 49.")
                userNumbers.clear()
                break
        except ValueError:
            print("Invalid input.")
            userNumbers.clear()
            break
    
    if userNumbers == winningNumbers:

        print("---You have won!!!---")

        print("---Your numbers: ", userNumbers)

        print("Winning numbers: ", winningNumbers)

    else:

        print("---You have lost---")

        print("Your numbers: ", userNumbers)

        print("Winning numbers: ", winningNumbers)
    
    if len(userNumbers) == 6:
        break