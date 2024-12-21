import sys  #Импортируем модуль sys
from transport.client import Client  #Импортируем класс Client
from transport.van import Van  #Импортируем класс Van
from transport.ship import Ship  #Импортируем класс Ship
from transport.transportcompany import TransportCompany  #Импортируем класс TransportCompany

def print_menu():  #Отображение меню
    print("Меню:")  #Вывод заголовка меню
    print("1. Добавить клиента")
    print("2. Создать фургон") 
    print("3. Создать судно")  
    print("4. Загрузить груз в транспортное средство")  
    print("5. Показать информацию о транспортном средстве")
    print("6. Оптимизировать распределение грузов")
    print("7. Выйти")

def main():
    company = TransportCompany("Моя Транспортная Компания")  #Создаем экземпляр класса TransportCompany

    while True:  #Работа с меню
        print_menu()  #Выводим меню на экран
        choice = input("Выберите пункт меню: ")  #Выбор пункта меню

        if choice == '1':  #Если 1
            name = input("Введите имя клиента: ")  #Ввод данных
            cargo_weight = float(input("Введите вес груза клиента: "))
            is_vip = input("Клиент VIP? (да/нет): ").lower() == 'да'
            client = Client(name, cargo_weight, is_vip)  #Создаем экземпляр класса Client
            company.add_client(client)  #Добавляем клиента в компанию
            print(f"Клиент {name} добавлен.\n")  #Выводим сообщение о добавлении клиента

        elif choice == '2':  #Если 2
            capacity = float(input("Введите грузоподъемность фургона (в тоннах): "))  #Ввод данных
            is_refrigerated = input("Фургон с холодильником? (да/нет): ").lower() == 'да' 
            van = Van(capacity, is_refrigerated)  #Создаем экземпляр класса Van
            company.add_vehicle(van)  #Добавляем фургон в компанию
            print(f"Фургон создан. ID: {van.vehicle_id}\n")  #Выводим сообщение о создании фургона

        elif choice == '3':  #Если 3
            capacity = float(input("Введите грузоподъемность судна (в тоннах): "))  #Ввод данных
            name = input("Введите название судна: ")
            ship = Ship(capacity, name)  #Создаем экземпляр класса Ship
            company.add_vehicle(ship)  #Добавляем судно в компанию
            print(f"Судно создано. Название: {name}, ID: {ship.vehicle_id}\n")  #Выводим сообщение о создании судна

        elif choice == '4':  #Если 4
            client_name = input("Введите имя клиента для загрузки: ")  #Ввод данныз
            vehicle_id = input("Введите ID транспортного средства: ")

            client = next((c for c in company.clients if c.name == client_name), None)  #Поиск клиента
            vehicle = next((v for v in company.vehicles if v.vehicle_id == vehicle_id), None)  #Поиск транспорта

            if client is None:  #Если клиент не найден - ошибка
                print(f"Клиент с именем {client_name} не найден.\n")
                continue

            if vehicle is None:  #Если транспорт не найден - ошибка
                print(f"Транспортное средство с ID {vehicle_id} не найдено.\n")
                continue

            try:
                vehicle.load_cargo(client)  #Загрузка груза
            except ValueError as e:  #Ошибка превышение грузоподъёмности
                print(f"Ошибка загрузки: {e}\n")
            except TypeError as e:  #Ошибка неверного ввода типа данных
                print(f"Ошибка типа данных: {e}\n")

        elif choice == '5':  #Если 5
            if not company.vehicles:  #Если нет транспортных средств
                print("Нет доступных транспортных средств для отображения.\n")
                continue

            for vehicle in company.vehicles:  #Перебор всего транспорта
                print(vehicle)  #вывод информации
                for client in vehicle.clients_list:  #Перебор всех клиентов с перегрузом
                    print(f"  - Клиент: {client.name}, Вес груза: {client.cargo_weight} т., VIP: {'Да' if client.is_vip else 'Нет'}")

            print()

        elif choice == '6':  #Если 6
            company.optimize_cargo_distribution()  #распределение грузов
            print("Распределение грузов оптимизировано.\n")

        elif choice == '7':  #Если 7
            sys.exit()  #Выход из программы

        else:  #Если выбран неверный пункт меню - ошибка
            print("Неверный пункт меню, попробуйте снова.\n")

if __name__ == '__main__':
    main()
