list0 = ['чихание', 'сковорода', 'болтливость', 'подросток', 'каблук', 'ложь', 'терроризм', 'ошибка']
cikl = 1
while cikl == 1 and len(list0) != 0:
    word = list0.pop()
    word0 = '_' * len(word)
    print('Ваше слово:', word0)
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    popitki = 3
    vsevo0popitok = 0
    cikl = 2
    while cikl == 2:
        print('Выберите действие:')
        print('1. сдаться')
        print('2. ввести букву')
        print('3. отгадать слово')
        number = input()
        while number != '1' and number != '2' and number != '3':
            print('Вы ввели недопустимое значение, попробуйте снова:')
            number = input()
        if number == '1':
            print('Удачи в следующий раз :(')
            print('Хотите попробовать еще раз?')
            print('1. да')
            print('2. нет')
            number1 = input()
            while number1 != '1' and number1 != '2':
                print('Вы ввели недопустимое значение, попробуйте снова:')
                number1 = input()
            if number1 == '1':
                cikl = 1
            elif number1 == '2':
                cikl = 3
        elif number == '2':
            vsevo0popitok += 1
            print(*alphabet)
            bukva = input()
            bukva = bukva.lower()
            while bukva not in alphabet or len(bukva) > 1:
                print('Ошибка, вы ввели не букву либо букву которая уже была, введите снова:')
                bukva = input()
                bukva = bukva.lower()
            alphabet.remove(bukva)
            wordl = list(word)
            word0 = list(word0)
            if bukva in word:
                print('Вы угадали букву, вы умница и красавица!')
            else:
                print('Вы не угадали букву')
            for i in range(wordl.count(bukva)):
                word0.insert(wordl.index(bukva), bukva)
                del word0[wordl.index(bukva) + 1]
                del wordl[wordl.index(bukva)]
            print(''.join(word0))
            if word == ''.join(word0):
                print('Вы отгадали слово! Вашему умению можно позавидовать!')
                print('Кол-во потраченных попыток:', vsevo0popitok)
                print('Хотите попробовать еще раз?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Вы ввели недопустимое значение, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    cikl = 1
                else:
                    cikl = 3
        elif number == '3':
            print('Введите слово:')
            answer = input()
            popitki += 1
            answer = answer.lower()
            if answer == word:
                print('Вы отгадали слово! Вашему умению можно позавидовать!')
                print('Кол-во потраченных попыток:', vsevo0popitok)
                print('Хотите попробовать еще раз?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Вы ввели недопустимое значение, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    cikl = 1
                else:
                    cikl = 3
            elif answer != word and popitki > 1:
                print('Вы не отгадали слово :(')
                popitki -= 1
                print('Осталось', popitki, 'попыток')
                print('Хотите продолжить отгадывать слово?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Вы ввели недопустимое значение, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    cikl = 2
                else:
                    print('Хотите попробовать еще раз?')
                    print('1. да')
                    print('2. нет')
                    number1 = input()
                    while number1 != '1' and number1 != '2':
                        print('Вы ввели недопустимое значение, попробуйте снова:')
                        number1 = input()
                    if number1 == '1':
                        cikl = 1
                    else:
                        cikl = 3
            else:
                print('Попытки закончились :(')
                print('Хотите попробовать еще раз?')
                print('1. да')
                print('2. нет')
                number1 = input()
                while number1 != '1' and number1 != '2':
                    print('Вы ввели недопустимое значение, попробуйте снова:')
                    number1 = input()
                if number1 == '1':
                    cikl = 1
                else:
                    cikl = 3
if len(list0) == 0:
    print('Ой, кажется слова закончились :(')
print('Приходите еще!')
print('(для окончания введите любой символ)')
input()
