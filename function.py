import functions_with_files
import Note
import ui


def add():
    note = ui.create_note()
    array = functions_with_files.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    functions_with_files.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    global date
    logic = True
    array = functions_with_files.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('Индивидуальный номер: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic:
        print('Заметки не найдены')


def id_edit_del_show(text):
    id = input('Введите индивидуальный номер: ')
    array = functions_with_files.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note()
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic:
        print('Данной заметки не существует')
    functions_with_files.write_file(array, 'a')
