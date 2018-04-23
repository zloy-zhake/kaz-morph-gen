# читать по строке из stdin (слово:часть_речи)
# часть_речи соответствет тегам Apertium
# (http://wiki.apertium.org/wiki/List_of_symbols)
# генерировать для каждого слова все возможные словоформы исходя из части речи

# TODO сделать вариант с сохранением в CSV.
# TODO добавить ключи для чтения из файла и для записи в файл
# TODO для местоимений сделать отдельные готовый список
# TODO добавить проверку на латинские буквы в вводе (напр.: i и і)

import sys
from generate_noun_forms import generate_noun_forms
from generate_number_forms import generate_number_forms
from generate_verb_forms import generate_verb_forms
from generate_adjective_forms import generate_adjective_forms

# Читаем данные из стандартного ввода
for line in sys.stdin:
    # очищаем лишние символы - \n в конце строки
    # отделяем слово от тега части речи
    word, pos = line.strip().split(':')
    # result = ""
    result = []
    # если слово - существительное - генерируем все формы для существительного
    if pos == 'n':
        result += generate_noun_forms((word, {"pos": "<n>"}))
    elif pos == "num":
        result += generate_number_forms((word, {"pos": "<num>"}))
    elif pos == 'v':
        result += generate_verb_forms((word, {"pos": "<v>"}))
    elif pos == 'adj':
        result += generate_adjective_forms((word, {"pos": "<adj>"}))
    else:
        # TODO не выводить ничего или заменить на что-то более полезное?
        result = word + " has a wrong tag."
    for generated_item in result:
        sys.stdout.write(generated_item[0] +
                         ':' +
                         str(generated_item[1]) +
                         '\n')
