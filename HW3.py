#Применить написанный логгер к приложению из любого предыдущего д/з.

import types
from HW2 import logger
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(list_documents):
    num_doc = str(input('Введите номер документа'))
    for document in list_documents:
        if num_doc == document['number']:
            print(document['name'])
            break
    else:
        print('Документа с таким номером не существует')


def shelf(list_directories):
    num_doc = str(input('Введите номер документа'))
    for shelfs, doc in list_directories.items():
        if num_doc in doc:
            print(shelfs)
            break
    else:
        print('Документа с таким номером не существует')


def list(list_documents):
    for dict in list_documents:
        print(f'{dict["type"]} "{dict["number"]}" "{dict["name"]}"')


def add(list_documents, list_directories):
    name_owner = str(input('Имя владельца'))
    number_doc = str(input('Введите номер документа'))
    type_doc = str(input('Введите тип документа'))
    number_shelf = str(input('Введите номер полки'))
    new_doc = dict(zip(["type", "number", "name"], [type_doc, number_doc, name_owner]))
    list_documents.append(new_doc)
    list_shelfs = []

    for shelfs, doc in list_directories.items():
        list_shelfs.append(shelfs)
    if number_shelf in list_shelfs:
        list_directories[number_shelf].append(number_doc)
        print(list_directories)
        print(list_documents)
    else:
        print('Полки под таким номером не существует')


def delete(list_documents, list_directories):
    num_doc = '10006'
    for doc in list_documents:
        if num_doc == doc['number']:
            list_documents.remove(doc)
            print(list_documents)
            break
    else:
        print('Документа с таким номером не существует')

    for shelfs, docs in list_directories.items():
        if num_doc in docs:
            docs.remove(num_doc)
            print(list_directories)


def move(list_directories):
    num_doc = '10006'
    num_shelf = '3'
    list_shelfs = []
    for shelfs, docs in list_directories.items():
        list_shelfs.append(shelfs)
    for shelfs, docs in list_directories.items():
        if (num_doc in docs) and num_shelf in list_shelfs:
            docs.remove(num_doc)
            list_directories[num_shelf].append(num_doc)
            print(list_directories)
            break
    else:
        print('Документа или полки с таким номером не существует')


def add_shelf(list_directories):
    num_shelf = str(input('Введите номер полки'))
    list_shelfs = []
    for shelfs in list_directories.keys():
        list_shelfs.append(shelfs)

    if num_shelf not in list_shelfs:
        list_directories[num_shelf] = []
        print(list_directories)

    elif num_shelf in list_shelfs:
        print('Полка под таким номером уже существует')
        # add_shelf(directories)

@logger('text.txt')
def all_func():
    print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;')
    print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;')
    print('l– list – команда, которая выведет список всех документов;')
    print('a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, '
          'имя владельца и номер полки, на котором он будет храниться;')
    print('d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога '
          'и его номер из перечня полок')
    print('m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую')
    print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень')
    custom_command = str(input('Введите соответствующую букву'))
    if custom_command == 'p':
        people(documents)
    elif custom_command == 's':
        shelf(directories)
    elif custom_command == 'l':
        list(documents)
    elif custom_command == 'a':
        add(documents, directories)
    elif custom_command == 'd':
        delete(documents, directories)
    elif custom_command == 'm':
        move(directories)
    elif custom_command == 'as':
        add_shelf(directories)
    else:
        print('Введите букву из списка  выше')
all_func()
