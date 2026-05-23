from typing import (
    Dict,
    List,
    Optional
)

class Product:
    """Товар - базовый класс для продукции."""

    _next_id = 1

    def __init__(self, name: str, purchase_price: float, selling_price: float) -> None:
        """
        Инициализация товара.

        :param name: название товара.
        :param purchase_price: закупочная цена.
        :param selling_price: продажная цена.
        """

        self.id = Product._next_id
        Product._next_id += 1
        self.name = name
        self.purchase_price = purchase_price
        self.selling_price = selling_price

    def __str__(self) -> str:

        return f"[{self.id}] {self.name} | Закуп: {self.purchase_price}₽ | Продажа: {self.selling_price}₽"


class Employee:
    """Работник компании."""

    _next_id = 1

    def __init__(self, full_name: str, position: str, salary: float) -> None:
        """
        Инициализация сотрудника.

        :param full_name: ФИО сотрудника.
        :param position: должность.
        :param salary: зарплата.
        """

        self.id = Employee._next_id
        Employee._next_id += 1
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.is_active = True  # работает или уволен

    def fire(self) -> None:
        """Увольнение сотрудника."""

        self.is_active = False

    def __str__(self) -> str:
        status = "Работает" if self.is_active else "Уволен"

        return f"[{self.id}] {self.full_name} | {self.position} | {self.salary}₽ | {status}"


class StorageCell:
    """Ячейка склада - хранит товар в определенном количестве."""

    _next_id = 1

    def __init__(self, product_id: int, quantity: int = 0) -> None:
        """
        Инициализация ячейки склада.

        :param product_id: ID товара.
        :param quantity: количество товара.
        """

        self.id = StorageCell._next_id
        StorageCell._next_id += 1
        self.product_id = product_id
        self.quantity = quantity
        self.max_capacity = 1000  # максимальное количество товара в одной ячейке

    def add(self, quantity: int) -> bool:
        """
        Добавление товара в ячейку.

        :param quantity: количество для добавления.

        :return: True если добавлено успешно, False если превышает вместимость.
        """

        # проверяем, не превысит ли добавление максимальную вместимость
        if self.quantity + quantity <= self.max_capacity:
            self.quantity += quantity

            return True

        return False  # недостаточно места в ячейке

    def remove(self, quantity: int) -> bool:
        """
        Удаление товара из ячейки.

        :param quantity: количество для удаления.

        :return: True если удалено успешно, False если недостаточно товара.
        """

        # проверяем, есть ли на складе нужное количество
        if self.quantity >= quantity:
            self.quantity -= quantity

            return True

        return False  # недостаточно товара

    def __str__(self) -> str:

        return f"Ячейка #{self.id} | Товар ID: {self.product_id} | Кол-во: {self.quantity}"


class Warehouse:
    """Склад - хранит товары в ячейках"""

    _next_id = 1

    def __init__(self, name: str, address: str) -> None:
        """
        Инициализация склада.

        :param name: название склада.
        :param address: адрес склада.
        """

        self.id = Warehouse._next_id
        Warehouse._next_id += 1
        self.name = name
        self.address = address
        self.cells = {}  # словарь ячеек: ключ - id ячейки, значение - объект ячейки
        self.employees = []  # список id сотрудников, работающих на складе
        self.responsible_employee_id = None  # id ответственного сотрудника
        self.is_open = True  # открыт ли склад для операций

    def check_responsible(self) -> bool:
        """Проверка наличия ответственного лица."""

        return self.responsible_employee_id is not None

    def open_warehouse(self) -> None:
        """Открытие склада."""

        # без ответственного склада работать не может
        if not self.check_responsible():
            print("❌ Нельзя открыть склад без ответственного лица!")

            return

        self.is_open = True

    def close_warehouse(self) -> None:
        """Закрытие склада."""

        self.is_open = False

    def set_responsible_employee(self, employee_id: int) -> None:
        """
        Смена ответственного лица.

        :param employee_id: ID нового ответственного сотрудника.
        """

        self.responsible_employee_id = employee_id

    def hire_employee(self, employee_id: int) -> None:
        """
        Найм сотрудника на склад.

        :param employee_id: ID сотрудника.
        """

        # добавляем сотрудника, если его еще нет в списке
        if employee_id not in self.employees:
            self.employees.append(employee_id)

    def fire_employee(self, employee_id: int) -> None:
        """
        Увольнение сотрудника со склада.

        :param employee_id: ID сотрудника.
        """

        # удаляем сотрудника из списка, если он там есть
        if employee_id in self.employees:
            self.employees.remove(employee_id)

    def add_product(self, product_id: int, quantity: int) -> bool:
        """
        Закупка товара - добавление на склад.

        :param product_id: ID товара.
        :param quantity: количество товара.
        :return: True если добавлено успешно, False если склад закрыт или нет ответственного.
        """

        # проверяем, можно ли выполнять операции на складе
        if not self.is_open:
            print("❌ Склад закрыт!")

            return False

        if not self.check_responsible():
            print("❌ На складе нет ответственного лица! Операция невозможна.")

            return False

        # ищем существующую ячейку с таким же товаром
        for cell in self.cells.values():
            if cell.product_id == product_id:

                return cell.add(quantity)  # добавляем в существующую ячейку

        # если ячейка не найдена, создаем новую
        new_cell = StorageCell(product_id, quantity)
        self.cells[new_cell.id] = new_cell

        return True

    def remove_product(self, product_id: int, quantity: int) -> bool:
        """
        Удаление товара со склада.

        :param product_id: ID товара.
        :param quantity: количество товара.

        :return: True если удалено успешно, False если товара недостаточно или склад закрыт.
        """

        # проверяем, можно ли выполнять операции на складе
        if not self.is_open:
            print("❌ Склад закрыт!")

            return False

        if not self.check_responsible():
            print("❌ На складе нет ответственного лица! Операция невозможна.")

            return False

        # ищем ячейку с нужным товаром
        for cell in self.cells.values():
            if cell.product_id == product_id:

                return cell.remove(quantity)  # удаляем товар из ячейки

        return False  # товар не найден на складе

    def move_product_to(self, target_warehouse: 'Warehouse', product_id: int, quantity: int) -> bool:
        """
        Перемещение товара на другой склад.

        :param target_warehouse: целевой склад.
        :param product_id: ID товара.
        :param quantity: количество товара.

        :return: True если перемещено успешно, False если ошибка.
        """

        # сначала удаляем товар с текущего склада
        if self.remove_product(product_id, quantity):
            # затем добавляем на целевой склад
            target_warehouse.add_product(product_id, quantity)

            return True

        return False  # не удалось удалить товар с исходного склада

    def get_all_products(self) -> Dict[int, int]:
        """
        Получение всех товаров на складе.

        :return: словарь {product_id: quantity}.
        """

        result = {}
        # проходим по всем ячейкам и собираем товары с ненулевым количеством
        for cell in self.cells.values():
            if cell.quantity > 0:
                result[cell.product_id] = cell.quantity

        return result

    def get_info(self) -> str:
        """
        Получение информации о складе.

        :return: отформатированная строка с информацией.
        """

        status = "Открыт" if self.is_open else "Закрыт"
        has_responsible = "Да" if self.check_responsible() else "Нет"
        total_items = sum(cell.quantity for cell in self.cells.values())  # общее количество товаров на складе

        return f"""
        === СКЛАД ===
        Название: {self.name}
        Адрес: {self.address}
        Статус: {status}
        Ответственный: {self.responsible_employee_id or 'Не назначен'}
        Ответственный назначен: {has_responsible}
        Сотрудников: {len(self.employees)}
        Товаров на складе: {total_items} ед.
        """

    def __str__(self) -> str:

        return f"Склад #{self.id}: {self.name}"


class SalePoint:
    """Пункт продаж - торговая точка"""

    _next_id = 1

    def __init__(self, name: str, address: str) -> None:
        """
        Инициализация пункта продаж.

        :param name: название пункта продаж.
        :param address: адрес пункта продаж.
        """

        self.id = SalePoint._next_id
        SalePoint._next_id += 1
        self.name = name
        self.address = address
        self.inventory = {}  # словарь товаров в наличии: ключ - id товара, значение - количество
        self.employees = []  # список id сотрудников, работающих в пункте
        self.responsible_employee_id = None  # id ответственного сотрудника
        self.is_open = True  # открыт ли пункт для продаж
        self.total_revenue = 0.0  # общая выручка пункта

    def check_responsible(self) -> bool:
        """Проверка наличия ответственного лица."""

        return self.responsible_employee_id is not None

    def open_point(self) -> None:
        """Открытие пункта продаж."""

        # без ответственного пункт работать не может
        if not self.check_responsible():
            print("❌ Нельзя открыть пункт продаж без ответственного лица!")

            return

        self.is_open = True

    def close_point(self) -> None:
        """Закрытие пункта продаж."""

        self.is_open = False

    def set_responsible_employee(self, employee_id: int) -> None:
        """
        Смена ответственного лица.

        :param employee_id: ID нового ответственного сотрудника.
        """

        self.responsible_employee_id = employee_id

    def hire_employee(self, employee_id: int) -> None:
        """
        Найм сотрудника.

        :param employee_id: ID сотрудника.
        """

        # добавляем сотрудника, если его еще нет в списке
        if employee_id not in self.employees:
            self.employees.append(employee_id)

    def fire_employee(self, employee_id: int) -> None:
        """
        Увольнение сотрудника.

        :param employee_id: ID сотрудника.
        """

        # удаляем сотрудника из списка, если он там есть
        if employee_id in self.employees:
            self.employees.remove(employee_id)

    def sell_product(self, product_id: int, quantity: int, price: float) -> bool:
        """
        Продажа товара.

        :param product_id: ID товара.
        :param quantity: количество товара.
        :param price: цена продажи за единицу.

        :return: True если продажа успешна, False если товара нет или пункт закрыт.
        """

        # проверяем, можно ли выполнять операции в пункте
        if not self.is_open:
            print("❌ Пункт продаж закрыт!")

            return False

        if not self.check_responsible():
            print("❌ В пункте продаж нет ответственного лица! Операция невозможна.")

            return False

        # проверяем наличие товара в нужном количестве
        if product_id in self.inventory and self.inventory[product_id] >= quantity:
            self.inventory[product_id] -= quantity  # списываем товар

            # если товар закончился, удаляем его из словаря
            if self.inventory[product_id] == 0:
                del self.inventory[product_id]

            self.total_revenue += price * quantity  # добавляем выручку

            return True

        return False  # недостаточно товара

    def return_product(self, product_id: int, quantity: int) -> bool:
        """
        Возврат товара.

        :param product_id: ID товара.
        :param quantity: количество товара для возврата.

        :return: True если возврат успешен, False если пункт закрыт.
        """

        # проверяем, можно ли выполнять операции в пункте
        if not self.is_open:
            print("❌ Пункт продаж закрыт!")

            return False

        if not self.check_responsible():
            print("❌ В пункте продаж нет ответственного лица! Операция невозможна.")

            return False

        # добавляем товар обратно в инвентарь
        if product_id in self.inventory:
            self.inventory[product_id] += quantity
        else:
            self.inventory[product_id] = quantity

        return True

    def restock_from_warehouse(self, warehouse: Warehouse, product_id: int, quantity: int) -> bool:
        """
        Закупка товара со склада.

        :param warehouse: склад-источник.
        :param product_id: ID товара.
        :param quantity: количество товара.

        :return: True если закупка успешна, False если на складе недостаточно товара.
        """

        # пытаемся удалить товар со склада
        if warehouse.remove_product(product_id, quantity):
            # если успешно, добавляем товар в пункт продаж
            if product_id in self.inventory:
                self.inventory[product_id] += quantity
            else:
                self.inventory[product_id] = quantity

            return True

        return False  # на складе недостаточно товара

    def get_all_products(self) -> Dict[int, int]:
        """
        Получение всех товаров в пункте продаж.

        :return: копия словаря инвентаря {product_id: quantity}.
        """

        return self.inventory.copy()  # возвращаем копию, чтобы внешний код не мог изменить оригинал

    def get_info(self) -> str:
        """
        Получение информации о пункте продаж.

        :return: отформатированная строка с информацией.
        """

        status = "Открыт" if self.is_open else "Закрыт"
        has_responsible = "Да" if self.check_responsible() else "Нет"
        total_items = sum(self.inventory.values())  # общее количество товаров в пункте

        return f"""
        === ПУНКТ ПРОДАЖ ===
        Название: {self.name}
        Адрес: {self.address}
        Статус: {status}
        Ответственный назначен: {has_responsible}
        Ответственный: {self.responsible_employee_id or 'Не назначен'}
        Сотрудников: {len(self.employees)}
        Товаров в наличии: {total_items} ед.
        Выручка: {self.total_revenue:.2f}₽
        """

    def __str__(self) -> str:

        return f"Пункт продаж #{self.id}: {self.name}"


class Company:
    """Предприятие - управляет складами, пунктами продаж, товарами и сотрудниками."""

    def __init__(self, name: str) -> None:
        """
        Инициализация предприятия.

        :param name: название предприятия.
        """

        self.name = name
        self.products = {}  # каталог товаров: ключ - id товара, значение - объект товара
        self.employees = {}  # каталог сотрудников: ключ - id сотрудника, значение - объект сотрудника
        self.warehouses = {}  # каталог складов: ключ - id склада, значение - объект склада
        self.sale_points = {}  # каталог пунктов продаж: ключ - id пункта, значение - объект пункта

    # управление товарами
    def add_product(self, name: str, purchase_price: float, selling_price: float) -> Product:
        """
        Добавление нового товара в каталог.

        :param name: название товара.
        :param purchase_price: закупочная цена.
        :param selling_price: продажная цена.

        :return: созданный объект товара.
        """

        product = Product(name, purchase_price, selling_price)
        self.products[product.id] = product  # сохраняем в каталог

        return product

    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Получение товара по ID.

        :param product_id: ID товара.

        :return: объект товара или None если не найден.
        """

        return self.products.get(product_id)

    def get_available_products(self) -> List[Product]:
        """
        Получение товаров, доступных к закупке.

        :return: список всех товаров из каталога.
        """

        return list(self.products.values())  # все товары в каталоге доступны для закупки

    # управление сотрудниками
    def hire_employee(self, full_name: str, position: str, salary: float) -> Employee:
        """
        Найм сотрудника.

        :param full_name: ФИО сотрудника.
        :param position: должность.
        :param salary: зарплата.

        :return: созданный объект сотрудника.
        """

        employee = Employee(full_name, position, salary)
        self.employees[employee.id] = employee  # сохраняем в каталог

        return employee

    def fire_employee(self, employee_id: int) -> bool:
        """
        Увольнение сотрудника.

        :param employee_id: ID сотрудника.

        :return: True если сотрудник найден и уволен, False если не найден.
        """

        if employee_id in self.employees:
            self.employees[employee_id].fire()  # вызываем метод увольнения

            return True

        return False  # сотрудник не найден

    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """
        Получение сотрудника по ID.

        :param employee_id: ID сотрудника.

        :return: объект сотрудника или None если не найден.
        """

        return self.employees.get(employee_id)

    # управление складами
    def add_warehouse(self, name: str, address: str) -> Warehouse:
        """
        Открытие нового склада.

        :param name: название склада.
        :param address: адрес склада.

        :return: созданный объект склада.
        """

        warehouse = Warehouse(name, address)
        self.warehouses[warehouse.id] = warehouse  # сохраняем в каталог

        return warehouse

    def close_warehouse(self, warehouse_id: int) -> bool:
        """
        Закрытие склада.

        :param warehouse_id: ID склада.

        :return: True если склад найден и закрыт, False если не найден.
        """

        if warehouse_id in self.warehouses:
            self.warehouses[warehouse_id].close_warehouse()  # вызываем метод закрытия

            return True

        return False  # склад не найден

    def get_warehouse(self, warehouse_id: int) -> Optional[Warehouse]:
        """
        Получение склада по ID.

        :param warehouse_id: ID склада.

        :return: объект склада или None если не найден.
        """

        return self.warehouses.get(warehouse_id)

    # управление пунктами продаж
    def add_sale_point(self, name: str, address: str) -> SalePoint:
        """
        Открытие пункта продаж.

        :param name: название пункта продаж.
        :param address: адрес пункта.

        :return: созданный объект пункта продаж.
        """

        point = SalePoint(name, address)
        self.sale_points[point.id] = point  # сохраняем в каталог

        return point

    def close_sale_point(self, point_id: int) -> bool:
        """
        Закрытие пункта продаж.

        :param point_id: ID пункта продаж.

        :return: True если пункт найден и закрыт, False если не найден.
        """

        if point_id in self.sale_points:
            self.sale_points[point_id].close_point()  # вызываем метод закрытия

            return True

        return False  # пункт не найден

    def get_sale_point(self, point_id: int) -> Optional[SalePoint]:
        """
        Получение пункта продаж по ID.

        :param point_id: ID пункта продаж.

        :return: объект пункта продаж или None если не найден.
        """

        return self.sale_points.get(point_id)

    # информационные методы
    def get_warehouse_info(self, warehouse_id: int) -> str:
        """
        Получение информации о складе.

        :param warehouse_id: ID склада.

        :return: отформатированная строка с информацией.
        """

        warehouse = self.get_warehouse(warehouse_id)

        return warehouse.get_info() if warehouse else "Склад не найден"

    def get_sale_point_info(self, point_id: int) -> str:
        """
        Получение информации о пункте продаж.

        :param point_id: ID пункта продаж.

        :return: отформатированная строка с информацией.
        """

        point = self.get_sale_point(point_id)

        return point.get_info() if point else "Пункт продаж не найден"

    def get_warehouse_products(self, warehouse_id: int) -> str:
        """
        Получение информации о товарах на складе.

        :param warehouse_id: ID склада.

        :return: отформатированная строка с товарами.
        """

        warehouse = self.get_warehouse(warehouse_id)
        if not warehouse:

            return "Склад не найден"

        products = warehouse.get_all_products()
        if not products:

            return "На складе нет товаров"

        result = f"\n=== Товары на складе '{warehouse.name}' ===\n"

        # проходим по всем товарам и выводим информацию о каждом
        for prod_id, qty in products.items():
            product = self.get_product(prod_id)
            if product:
                result += f"{product} | Количество: {qty}\n"

        return result

    def get_sale_point_products(self, point_id: int) -> str:
        """
        Получение информации о товарах в пункте продаж.

        :param point_id: ID пункта продаж.

        :return: отформатированная строка с товарами.
        """

        point = self.get_sale_point(point_id)
        if not point:

            return "Пункт продаж не найден"

        products = point.get_all_products()
        if not products:

            return "В пункте продаж нет товаров"

        result = f"\n=== Товары в пункте '{point.name}' ===\n"

        # проходим по всем товарам и выводим информацию о каждом
        for prod_id, qty in products.items():
            product = self.get_product(prod_id)
            if product:
                result += f"{product} | Количество: {qty}\n"

        return result

    def get_profitability(self, point_id: Optional[int] = None) -> str:
        """
        Получение информации о доходности.

        :param point_id: ID пункта продаж (если None - доходность всего предприятия).

        :return: отформатированная строка с доходностью.
        """

        # если указан конкретный пункт продаж
        if point_id:
            point = self.get_sale_point(point_id)
            if point:

                return f"Доходность пункта '{point.name}': {point.total_revenue:.2f}₽"

            return "Пункт продаж не найден"

        # суммируем выручку всех пунктов продаж для общей доходности предприятия
        total_revenue = sum(p.total_revenue for p in self.sale_points.values())

        return f"Доходность предприятия '{self.name}': {total_revenue:.2f}₽"