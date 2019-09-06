import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
      |
      |
     ===
''', '''
  +---+
  0   |
  |   |
      |
     ===
''', '''
  +---+
  0   |
 /|   |
      |
     ===
''', '''
  +---+
  0   |
 /|\  |
      |
     ===
''', '''
 +---+
  0   |
 /|\  |
   \  |
     ===
''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===
''', '''
  +---+
  0]  |
 /|\  |
 / \  |
     ===
''', '''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===
''']

words = {'Спорт': ' баскетбол футбол гандбол волейбол теннис хоккей сноубординг серфинг скейтбординг скаолазание '\
                  ' плавание самбо борьба каратэ айкидо дзюдо велоспорт'.split(),
         'Животные': ' аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра'\
                     ' мея индюк кит кобра коза козел койот корова кошка кролик крыса курца лама ласка лебедь лев лиса'\
                     ' лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь'\
                     ' олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка'\
                     ' форель хорек черепаха ястреб ящерица'.split(),
         'Фигуры:': ' квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник'\
                    ' шестиугольник восьмиугольник'.split(),
         'Цвета': ' красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
         'НБА': ' роектс селтикс кавальерс наггетс блэйззерс тандер лэйкерс клипперс варриорс сперс бакс рэпторс нетс'\
                ' сиксиерс никс хит джаз буллз маверикс пистонс мэджик кингз пэйсерс тимбервулвз санз пеликанс хорнетс'\
                ' хокс уизардс гриззлис'.split()}


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):  # заменяет пропуски отгаданными буквами
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между букв
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    """Возвращает букву, введенную игроком. Проверяет, чтоб игрок ввел только одну букву и ничего больше"""
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
        elif guess in already_guessed:
            print('Вы уже вводили эту букву. Введите другую')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ!')
        else:
            return guess


def play_again():
    print('Хотите сыграть еще?(да или нет)')
    return input().lower().startswith('д')


def choose_difficulty():
    ''' Функция для выбора уровня сложности игры'''
    while True:
        print('Выберите уровень сложности: Л-легкий, С-средний, Т-тяжелый ')
        diff = input()
        diff = diff.upper()
        if len(diff) != 1:
            print("Пожалуйста, введите одну букву.")
        elif diff not in 'ЛСТ':
            print('Пожалуйста, введите одну из перечисленных букв(ЛСТ)')
        else:
            return diff


def choose_category(words):
    '''Функция для выбора категории слов из передаваемого словаря'''
    while True:
        print('Выберите категорию: ')
        j = 0
        for key in words:
            j += 1
            print(str(j) + '-' + key)
        print(str(j+1) + '-случайный выбор')
        answer = input()
        if int(answer) > j+1:
            print('Пожалуйста, выберите один ответ из перечисленных.')
        elif answer not in '1234567890':
            print('Введите цифру!')
        else:
            i = 0
            answer = int(answer)
            for key in words:
                i += 1
                if (answer == i) and (answer - 1 != len(words.keys())):
                    word_key = key
                    word_index = random.randint(0, len(words[word_key]) - 1)
                    return words[word_key][word_index], word_key
                elif answer-1 == len(words.keys()):
                    word_key = random.choice(list(words.keys()))
                    word_index = random.randint(0, len(words[word_key]) - 1)
                    return words[word_key][word_index], word_key


print('В И С Е Л И Ц А')
difficulty = ''
difficulty = choose_difficulty()
if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
elif difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
missed_letters = ''
correct_letters = ''
secret_word, secret_set = choose_category(words)
gameIsDone = False

while True:
    print("Секретное слво из набора:" + secret_set)
    display_board(missed_letters, correct_letters, secret_word)
    # Позволяет игроку ввести букву.
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        correct_letters = correct_letters + guess
        # Проверяет, выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово- "' + secret_word + '"! Вы угадали!')
            gameIsDone = True
    else:
        missed_letters += guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('Вы исчерпали все ' + str(len(missed_letters)) + ' попыток!\nУгаданно букв: ' +
                  str(len(correct_letters)) + '\nЗагаданное слово: ' + secret_word)
            gameIsDone = True
    # Запрашивает, хочет ли игрок сыграть снова
    if gameIsDone:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            gameIsDone = False
            secretWord, secret_set = choose_category(words)
        else:
            break
