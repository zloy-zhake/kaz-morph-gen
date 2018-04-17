# читать по строке из stdin (слово:часть_речи)
# часть_речи соответствет тегам Apertium
# (http://wiki.apertium.org/wiki/List_of_symbols)
# генерировать для каждого слова все возможные словоформы исходя из части речи

# TODO сделать вариант с сохранением в CSV.
# (Возможно для этого нужно сохранять теги в виде кортежей)

# TODO добавить ключи для чтения из файла и для записи в файл

import sys
from generate_noun_forms import generate_noun_forms
from generate_number_forms import generate_number_forms

# Читаем данные из стандартного ввода
for line in sys.stdin:
    # очищаем лишние символы - \n в конце строки
    # отделяем слово от тега части речи
    word, pos = line.strip().split(':')
    # result = ""
    result = []
    # если слово - существительное - генерируем все формы для существительного
    if pos == 'n':
        # result += generate_noun_forms((word, "<n>"))
        result += generate_noun_forms((word, {"pos": "<n>"}))
    elif pos == "num":
        result += generate_number_forms((word, {"pos": "<num>"}))
    else:
        # TODO не выводить ничего или заменить на что-то более полезное?
        result = word + " has a wrong tag."
    # result += '\n'
    for generated_item in result:
        sys.stdout.write(generated_item[0] +
                         ':' +
                         str(generated_item[1]) +
                         '\n')
