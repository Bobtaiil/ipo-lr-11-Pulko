from transport.vehicle import Vehicle  #Импортируем класс Vehicle

class Ship(Vehicle):  #Определяем класс Ship
    def __init__(self, capacity, name):  #Инициализация класса
        super().__init__(capacity)  #Родительский класс Vehicle
        self.name = name  #name

    def __str__(self):  #строковое представление
        return f"Судно {self.name} - {super().__str__()}"  #Возвращаем строку с названием судна и строковым представлением родительского класса Vehicle
