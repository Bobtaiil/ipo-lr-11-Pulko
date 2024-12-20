from transport.vehicle import Vehicle  #Импортируем класс Vehicle

class Van(Vehicle):  #Определяем класс Van
    def __init__(self, capacity, is_refrigerated=False):  #Метод инициализации класса
        super().__init__(capacity)  #Вызываем метод Vehicle
        self.is_refrigerated = is_refrigerated  #Инициализируем атрибут is_refrigerated
