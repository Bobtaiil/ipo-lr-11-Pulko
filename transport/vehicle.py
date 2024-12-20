import uuid  #Импортируем модуль uuid
from transport.client import Client  #Импортируем класс Client

class Vehicle:  #Определяем класс Vehicl
    def __init__(self, capacity):  #Инициализация класса
        self.vehicle_id = str(uuid.uuid4())  #Генерация уникального идентификатора для транспорта
        self.capacity = self.validate_capacity(capacity)  #Установка грузоподъёмности и её валидация
        self.current_load = 0  #Текущая загрузка ( по умолчанию 0 )
        self.clients_list = []  #Список клиентов с перегрузом

    def validate_capacity(self, capacity):  #Валидация грузоподъёмности
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Грузоподъемность - положительное число ")
        return capacity  #Возвращаем грузоподъёмность

    def load_cargo(self, client):  #Загрузка груза клиента
        if not isinstance(client, Client):  #Проверка на принадлежность Client
            raise TypeError("Ожидается объект класса Client")
        
        if self.current_load + client.cargo_weight > self.capacity:  #Проверка на превышение грузоподъемности
            raise ValueError("Превышение грузоподъемности")
        
        self.current_load += client.cargo_weight  #Увеличение текущей загрузки на вес груза клиента
        self.clients_list.append(client)  #Добавление клиента в список загруженных клиентов
        print(f"Груз клиента {client.name} весом {client.cargo_weight} т. загружен.")  #Вывод сообщения о загрузке груза

    def __str__(self):  #строковое представление
        return f"ID транспортного средства: {self.vehicle_id}, Грузоподъемность: {self.capacity} т., Текущая загрузка = {self.current_load} т."
