#Эта программа по отгадыванию игроком загаданного числа
import random


def ending(n):
    if n == 1:
        return 'кa'
    elif n >= 2 and n <= 4:
        return 'ки'
    elif n >= 5:
        return 'ок'


guesssesTaken = 0
myName = input("Как тебя зовут?\n")
num_range = input("Загадай диапазон:\n")
num_range = int(num_range)
chances = (num_range/4)+1
chances = int(chances)
number = random.randint(1, num_range)
print("Что ж, " + myName + ", я загадываю число от 1 до " + str(num_range) + "\nУ тебя есть " + str(chances)
      + " попыт" + ending(chances) + '.')
for guesssesTaken in range(num_range):
    guess = input()
    guess = int(guess)
    if guess == number:
        guesssesTaken += 1
        print("Отлично, " + myName + "! Ты отгадал число за " + str(guesssesTaken) + " попыт" + ending(guesssesTaken)
              + '.')
        break
    elif guess > number:
        print("Твое число слишком большое.")
    elif guess < number:
        print("Твое число слишком маленькое.")
if guess != number:
    print("Увы, ты не отгадал число за" + str(chances) + " попыт" + ending(num_range) + '.' + "Это число: "
          + str(number))
