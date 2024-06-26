# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep


class Knife(Thread):

    def __init__(self, my_name, skill, enemies):
        self.my_name = my_name
        self.skill = skill
        self.enemies = enemies
        super().__init__()

    def run(self):
        day = 0  # Количество дней войны
        print(f'Sir {self.my_name}, на нас напали!')
        while self.enemies > 0:
            day += 1
            sleep(1)  # 1 сек соответствует 1 дню в игре
            self.enemies -= self.skill
            print(f'Sir {self.my_name} сражается {day} день. Осталось {self.enemies} врагов')

        print(f'Sir {self.my_name} одержал победу спустя {day} дней!')


# Объявляем потоки
Knife1 = Knife("Вася", 10, 100)
Knife2 = Knife("Иван", 20, 100)
# Запускаем потоки
Knife1.start()
sleep(0.1)  # Чтобы два потока не накладывались друг на друга
Knife2.start()
# join
Knife1.join()
Knife2.join()
print('-------- The End --------')
