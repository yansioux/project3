import os.path
import re
import sys
from termios import TCIFLUSH, tcflush

from . import dictionary_utl, sentence_utl

PERLS_FILE = 'out.txt'


def main():

    tcflush(sys.stdin, TCIFLUSH)

    # приветствие
    print('\033[0;34m***********************************************\033[0m')
    print('\033[0;32mProject3 - генератор грамматических конструкций\033[0m')
    print('\033[0;32mавтор: Ян Пак 2020 MIT License\033[0m')
    print('\033[0;34m***********************************************\033[0m')

    # загрузка словаря
    dict_file = sys.argv[1]
    print(
        '\033[0;33mСловарь загружается. Пожалуйста подождите...\n\033[0m')
    dict = dictionary_utl.load_dict(dict_file)
    print('Поехали!')

    # начало интерактивной работы. Ввод исходного предложения для генерации результатов
    sentence = ''
    while not sentence:

        print('Введите предложение для примера грамматической конструкции (либо 0 для выхода):')
        sentence = input()

    # если пользователь ввел 0 - выходим
    if sentence == '0':
        print(
            '\033[0;32mЭх жаль! Вы лишаете себя интересного опыта. Ну, до скорой встречи! :)\033[0m')
        return

    # определим доступные схемы по вводному предложению
    (schemes_set, words) = sentence_utl.get_schemes(dict, sentence)

    # по каждому слову из вводного предложения попросим выбрать возможные схемы для генерации
    selected_schemes_set = []
    for a in range(len(words)):
        if len(schemes_set[a]) == 0:
            continue
        print('Выберите схемы для слова (вводите номера схем через пробел) "',
              words[a], '":')
        ind = 0
        for b in schemes_set[a]:
            print(ind, ' -> ', b)
            ind += 1
        if ind == 1:
            selected_schemes_set.append(schemes_set[a])
            print('0')
        else:
            choose = input()
            schemes_nums = re.split(r'\s', choose)
            selected_schemes = [schemes_set[a]
                                [int(scheme_num)] for scheme_num in schemes_nums]
            selected_schemes_set.append(selected_schemes)

    # подготовим запись в файл сохраненных решений
    perl = ''
    out = open(PERLS_FILE, 'a')
    out.write(
        'Результаты для предложения-примера "{}"\n'.format(sentence))
    out.write(
        'Грамматической конструкции "{}":\n'.format(' + '.join(['|'.join(selected_schemes_set[a])+'(%s)' % words[a] for a in range(len(selected_schemes_set))])))

    # выполняем в цикле показ сгенерированных предложений по выбранным схемам
    # пока пользователь не набрал 0 для выхода
    print('Вот что получилось (результаты будут сохраняться в %s):' % PERLS_FILE)
    while sentence.strip().lower() != '0':
        # сгенерируем случайное предложение из выбранных схем
        perl = sentence_utl.get_randomized_variant(
            dict, selected_schemes_set)[0]
        print(perl)

        # сохраняем сгенерированную конструкцию
        out.write(perl)
        out.write('\n')
        out.flush()

        # ждем ввод пользователя для продолжения
        sentence = input()

    # закрываем файл
    out.write('\n')
    out.close()
    print('\033[0;32mДо скорой встречи!\033[0m')
