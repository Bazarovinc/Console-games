#Эта программа по отгадыванию игроком загаданного числа
import random
guesssesTaken = 0
myName = input("Как тебя зовут?")
num_range = input("Загадай диапазон")
num_range = int(num_range)
chances = (num_range/4)+1
chances= int(chances)
number = random.randint(1, num_range)
print("Что ж, " + myName + ", я загадываю число от 1 до " + str(num_range) + "\nУ тебя есть " + str(chances)
      + " попыток.")
for guesssesTaken in range(num_range):
    guess = input()
    guess = int(guess)
    if guess == number:
        guesssesTaken += 1
        print("Отлично, " + myName + "! Ты отгадал число за " + str(guesssesTaken) + " попыток." )
        break
    elif guess > number:
        print("Твое число слишком большое.")
    elif guess < number:
        print("Твое число слишком маленькое.")
if guess != number:
    print("Увы, ты не отгадал число за" + str(chances) + "попыток. Это число: " + str(number))
