
class Spravka(object):
    """класс для описания справки \n
       name - название справки\n
       url - адрес справки\n
       url_test - адрес справки с тестового портала\n
       sas - названия .sas, которые используются при разрваботке справки\n
       hp - названия хранимой процедуры, которые используются при разрваботке справки\n
       js - названия .js, которые используются при разрваботке справки\n
       css - названия .css, которые используются при разрваботке справки\n
       task - название задания\n
       developer - информация о разработчике\n
    """

    def __init__(self, name: str = '', url: str = '', url_test: str = '', sas: str = '', hp: str = '',
                 js: str = '', css: str = '', task: str = '', developer: str = ''):
        self.name = name
        self.url = url
        self.url_test = url_test
        self.sas = sas
        self.hp = hp
        self.js = js
        self.css = css
        self.task = task
        self.developer = developer

    def __str__(self):
        """Вывод информации о справке"""
        message = """
            Название справки - %s 
            URL справки - %s 
            SAS - %s 
            Хранимая процедура - %s 
            JS's - %s 
            CSS's - %s 
            Задание - %s 
            Разработчик - %s 
                  """ % (self.name, self.url, self.sas, self.hp, self.js, self.css, self.task, self.developer)
        return message

    def __repr__(self):
        """Вывод информации о справке"""
        message = """
            Название справки - %s 
            URL справки - %s 
            SAS - %s 
            Хранимая процедура - %s 
            JS's - %s 
            CSS's - %s 
            Задание - %s 
            Разработчик - %s 
                  """ % (self.name, self.url, self.sas, self.hp, self.js, self.css, self.task, self.developer)
        return message


def grid(it, count: int = 1):
    """
    :param it: список который будет разбит по спискам по count
    :param count: количество столбцов
    :return: grid(it=[1,2,3,5,6,7,8,9], count=3) -> [[1,2,3], [4,5,6], [7,8,9]]
    """
    new_it = []
    while it:
        new_it.append(it[:count])
        it = it[count:]

    return new_it
