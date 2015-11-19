## -*- coding: utf-8 -*-

"""Написать абстрактный класс в котором будет только один атрибут котороый
и есть введённое нами число  по умолчанию в конструкторе задается значение ноль

написать Класс в котором будут описанны все функции с первого домашнего задания
создаем конечный класс в котором наследуем два предыдущих класса в не же перегружаем конструктор
"""

class Number():
    y=None
    def __init__(self,x=0):
        self.y=x

class Check():

    def check_input(self):

        if 1<=self.y<4:
            self.btw_one_and_four()

        elif self.y<7:
            self.btw_four_and_seven()

        elif self.y<10:
            self.btw_seven_and_ten()
        else:
            print "Number is out of specified range... Quiting the programm..."

    def btw_one_and_four(self):
        s=raw_input("Enter a string: ")
        n=int(raw_input("Enter repetition times: "))
        for repetion in range(0,n,1):
            print s

    def btw_four_and_seven(self):
        m=int(raw_input("Enter Power degree: "))
        print x**m

    def btw_seven_and_ten(self):
        for repetition in range(x, x+10, 1):
            print repetition

class Inheriter(Number, Check):
    self.check_input()

while True:
    try:
        x=int(raw_input("Enter a number between 1 and 9: "))
        break
    except:
        print "It is not a number... Try again..."

number=Inheriter(x) # создает объект класса и вызывает интеравктив (атрибут в этом случае равен нулю)

    
