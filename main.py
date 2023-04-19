import datetime as dt


class Presentation:
    def __init__(self, start, end, name):
        self.start, self.end, self.name = start, end, name

    def perekr(self, st, en):
        if en < self.start or self.end < st:
            return True
        return False

    def print_presentation(self):
        return f'Начало: {self.start}, конец: {self.end}, тема: {self.name}'


class Conference:
    def __init__(self):
        self.present = []
        self.conf_start = False
        self.conf_end = False

    def add_presentation(self):
        data = list(map(int, input('Введите дату выступления (ЧЧ-ММ-ГГГГ): ').split('-')))
        while len(data) != 3:
            print('Ошибка, повторите ввод')
            data = list(map(int, input('Введите дату (ЧЧ-ММ-ГГГГ): ').split('-')))
        time = list(map(int, input('Введите время начала выступления (ЧЧ:ММ): ').split(':')))
        while len(time) != 2:
            print('Ошибка, повторите ввод')
            time = list(map(int, input('Введите время (ЧЧ:ММ): ').split(':')))
        try:
            start = dt.datetime(data[2], data[1], data[0], time[0], time[1])
        except ValueError:
            print('Ошибка, повторите ввод')
            self.add_presentation()
        delta = list(map(int, input('Задайте время выступления (ЧЧ:ММ): ').split(':')))
        while len(delta) != 2:
            print('Ошибка, повторите ввод')
            delta = list(map(int, input('Задайте время выступления (ЧЧ:ММ): ').split(':')))
        try:
            delta = dt.timedelta(hours=delta[0], minutes=delta[1])
        except ValueError:
            print('Ошибка, повторите ввод')
            self.add_conference()
        end = start + delta
        theme = input('Введите тему выступления: ')
        for i in self.present:
            if not i.perekr(start, end):
                print('Этот доклад перекрывает другой, создайте другой.')
                return
        self.present.append(Presentation(start, end, theme))
        if self.conf_start:
            if start < self.conf_start:
                self.conf_start = start
        else:
            self.conf_start = start
        if self.conf_end:
            if end > self.conf_end:
                self.conf_end = end
        else:
            self.conf_end = end
        print('Вы успешно добавили доклад!')

    def end_conference(self):
        self.present = sorted(self.present, key=lambda x: x.start)
        print('Вы успешно создали конференцию!')
        print(f'Начало: {self.conf_start}, конец: {self.conf_end}')
        print(f'Общая продолжительность: {self.conf_end - self.conf_start}')
        print(f'Количество выступлений: {len(self.present)}')
        print('Список выступлений:')
        for i in range(len(self.present)):
            print(f'    {i + 1}: {self.present[i].print_presentation()}')
        print('Работа менеджера конференций завершена')


def main():
    conference = Conference()
    print('--------------Менеджер Конференций--------------')
    print('Доступные команды:')
    print('------new - добавление нового доклада------')
    print('------end - вывод информации о конференции и завершение работы------')
    while True:
        command = input('Введите команду: ').lower().strip()
        while command not in ['new', 'end']:
            command = input('Команда не распознана, повторите ввод: ').lower().strip()
        if command == 'new':
            conference.add_presentation()
        else:
            conference.end_conference()
            break


main()
