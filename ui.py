from core import Company
from data import DataStorage
from typing import Optional
import os


def clear_screen() -> None:
    """Очистка экрана консоли."""

    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu() -> None:
    """Вывод главного меню."""

    print("\n" + "=" * 50)
    print("         CRM - УПРАВЛЕНИЕ ПРЕДПРИЯТИЕМ")
    print("=" * 50)
    print("\n=== УПРАВЛЕНИЕ ТОВАРАМИ ===")
    print("1. Добавить товар")
    print("2. Список товаров")

    print("\n=== УПРАВЛЕНИЕ СОТРУДНИКАМИ ===")
    print("3. Найм сотрудника")
    print("4. Увольнение сотрудника")
    print("5. Список сотрудников")

    print("\n=== УПРАВЛЕНИЕ СКЛАДАМИ ===")
    print("6. Открыть склад")
    print("7. Закрыть склад")
    print("8. Информация о складе")
    print("9. Товары на складе")
    print("10. Переместить товар между складами")
    print("11. Назначить ответственного на склад")
    print("12. Добавить сотрудника на склад")

    print("\n=== УПРАВЛЕНИЕ ПУНКТАМИ ПРОДАЖ ===")
    print("13. Открыть пункт продаж")
    print("14. Закрыть пункт продаж")
    print("15. Информация о пункте продаж")
    print("16. Товары в пункте продаж")
    print("17. Назначить ответственного в пункт продаж")
    print("18. Добавить сотрудника в пункт продаж")

    print("\n=== ОПЕРАЦИИ ===")
    print("19. Закупка товара (на склад)")
    print("20. Продажа товара")
    print("21. Возврат товара")
    print("22. Закупка товара со склада в пункт продаж")

    print("\n=== ФИНАНСЫ ===")
    print("23. Доходность предприятия")
    print("24. Доходность пункта продаж")

    print("\n=== СИСТЕМА ===")
    print("25. Сохранить данные")
    print("26. Загрузить данные")
    print("0. Выход")
    print("-" * 50)


def add_product(company: Company) -> None:
    """Добавление товара."""

    clear_screen()

    print("\n=== ДОБАВЛЕНИЕ ТОВАРА ===")
    name = input("Название товара: ")

    try:
        purchase_price = float(input("Закупочная цена: "))
        selling_price = float(input("Продажная цена: "))
        product = company.add_product(name, purchase_price, selling_price)
        print(f"✅ Товар добавлен! ID: {product.id}")
    except ValueError:
        print("❌ Ошибка: цена должна быть числом")

    input("\nНажмите Enter для продолжения...")


def list_products(company: Company) -> None:
    """Список всех товаров."""

    clear_screen()

    print("\n=== ВСЕ ТОВАРЫ ===")
    products = company.products.values()
    if not products:
        print("Нет добавленных товаров")
    else:
        for product in products:
            print(f"  {product}")

    input("\nНажмите Enter для продолжения...")


def hire_employee(company: Company) -> None:
    """Найм сотрудника."""

    clear_screen()

    print("\n=== НАЙМ СОТРУДНИКА ===")
    name = input("ФИО сотрудника: ")
    position = input("Должность: ")

    try:
        salary = float(input("Зарплата: "))
        employee = company.hire_employee(name, position, salary)
        print(f"✅ Сотрудник нанят! ID: {employee.id}")
    except ValueError:
        print("❌ Ошибка: зарплата должна быть числом")

    input("\nНажмите Enter для продолжения...")


def fire_employee(company: Company) -> None:
    """Увольнение сотрудника."""

    clear_screen()

    print("\n=== УВОЛЬНЕНИЕ СОТРУДНИКА ===")

    try:
        emp_id = int(input("ID сотрудника: "))
        if company.fire_employee(emp_id):
            print("✅ Сотрудник уволен")
        else:
            print("❌ Сотрудник не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def list_employees(company: Company) -> None:
    """Список сотрудников."""

    clear_screen()

    print("\n=== СОТРУДНИКИ ===")
    employees = company.employees.values()
    if not employees:
        print("Нет сотрудников")
    else:
        for emp in employees:
            print(f"  {emp}")

    input("\nНажмите Enter для продолжения...")


def open_warehouse(company: Company) -> None:
    """Открытие склада."""

    clear_screen()

    print("\n=== ОТКРЫТИЕ СКЛАДА ===")

    name = input("Название склада: ")
    address = input("Адрес: ")
    warehouse = company.add_warehouse(name, address)

    print(f"✅ Склад создан! ID: {warehouse.id}")
    print("⚠️  Склад пока не может работать - нужно назначить ответственного!")

    input("\nНажмите Enter для продолжения...")


def close_warehouse(company: Company) -> None:
    """Закрытие склада."""

    clear_screen()

    print("\n=== ЗАКРЫТИЕ СКЛАДА ===")

    try:
        wh_id = int(input("ID склада: "))
        if company.close_warehouse(wh_id):
            print("✅ Склад закрыт")
        else:
            print("❌ Склад не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def warehouse_info(company: Company) -> None:
    """Информация о складе."""

    clear_screen()

    print("\n=== ИНФОРМАЦИЯ О СКЛАДЕ ===")

    try:
        wh_id = int(input("ID склада: "))
        print(company.get_warehouse_info(wh_id))
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def warehouse_products(company: Company) -> None:
    """Товары на складе."""

    clear_screen()

    print("\n=== ТОВАРЫ НА СКЛАДЕ ===")

    try:
        wh_id = int(input("ID склада: "))
        print(company.get_warehouse_products(wh_id))
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def move_product(company: Company) -> None:
    """Перемещение товара между складами."""

    clear_screen()

    print("\n=== ПЕРЕМЕЩЕНИЕ ТОВАРА ===")

    try:
        from_id = int(input("ID склада-отправителя: "))
        to_id = int(input("ID склада-получателя: "))
        product_id = int(input("ID товара: "))
        quantity = int(input("Количество: "))

        from_wh = company.get_warehouse(from_id)
        to_wh = company.get_warehouse(to_id)

        if from_wh and to_wh:
            if from_wh.move_product_to(to_wh, product_id, quantity):
                print("✅ Товар перемещен")
            else:
                print("❌ Ошибка: недостаточно товара или склад закрыт")
        else:
            print("❌ Склад не найден")
    except ValueError:
        print("❌ Ошибка: ID и количество должны быть числами")

    input("\nНажмите Enter для продолжения...")


def assign_warehouse_responsible(company: Company) -> None:
    """Назначение ответственного на склад."""

    clear_screen()

    print("\n=== НАЗНАЧЕНИЕ ОТВЕТСТВЕННОГО НА СКЛАД ===")

    try:
        wh_id = int(input("ID склада: "))
        emp_id = int(input("ID сотрудника: "))

        warehouse = company.get_warehouse(wh_id)
        if warehouse and emp_id in company.employees:
            warehouse.set_responsible_employee(emp_id)
            print("✅ Ответственный назначен")
        else:
            print("❌ Склад или сотрудник не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def add_employee_to_warehouse(company: Company) -> None:
    """Добавление сотрудника на склад."""

    clear_screen()

    print("\n=== ДОБАВЛЕНИЕ СОТРУДНИКА НА СКЛАД ===")

    try:
        wh_id = int(input("ID склада: "))
        emp_id = int(input("ID сотрудника: "))

        warehouse = company.get_warehouse(wh_id)
        if warehouse and emp_id in company.employees:
            warehouse.hire_employee(emp_id)
            print("✅ Сотрудник добавлен на склад")
        else:
            print("❌ Склад или сотрудник не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def open_sale_point(company: Company) -> None:
    """Открытие пункта продаж."""

    clear_screen()

    print("\n=== ОТКРЫТИЕ ПУНКТА ПРОДАЖ ===")

    name = input("Название пункта: ")
    address = input("Адрес: ")
    point = company.add_sale_point(name, address)

    print(f"✅ Пункт продаж создан! ID: {point.id}")
    print("⚠️  Пункт продаж пока не может работать - нужно назначить ответственного!")

    input("\nНажмите Enter для продолжения...")


def close_sale_point(company: Company) -> None:
    """Закрытие пункта продаж."""

    clear_screen()

    print("\n=== ЗАКРЫТИЕ ПУНКТА ПРОДАЖ ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        if company.close_sale_point(point_id):
            print("✅ Пункт продаж закрыт")
        else:
            print("❌ Пункт продаж не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def sale_point_info(company: Company) -> None:
    """Информация о пункте продаж."""

    clear_screen()

    print("\n=== ИНФОРМАЦИЯ О ПУНКТЕ ПРОДАЖ ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        print(company.get_sale_point_info(point_id))
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def sale_point_products(company: Company) -> None:
    """Товары в пункте продаж."""

    clear_screen()

    print("\n=== ТОВАРЫ В ПУНКТЕ ПРОДАЖ ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        print(company.get_sale_point_products(point_id))
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def assign_sale_point_responsible(company: Company) -> None:
    """Назначение ответственного в пункт продаж."""

    clear_screen()

    print("\n=== НАЗНАЧЕНИЕ ОТВЕТСТВЕННОГО В ПУНКТ ПРОДАЖ ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        emp_id = int(input("ID сотрудника: "))

        point = company.get_sale_point(point_id)
        if point and emp_id in company.employees:
            point.set_responsible_employee(emp_id)
            print("✅ Ответственный назначен")
        else:
            print("❌ Пункт продаж или сотрудник не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def add_employee_to_sale_point(company: Company) -> None:
    """Добавление сотрудника в пункт продаж."""

    clear_screen()

    print("\n=== ДОБАВЛЕНИЕ СОТРУДНИКА В ПУНКТ ПРОДАЖ ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        emp_id = int(input("ID сотрудника: "))

        point = company.get_sale_point(point_id)
        if point and emp_id in company.employees:
            point.hire_employee(emp_id)
            print("✅ Сотрудник добавлен в пункт продаж")
        else:
            print("❌ Пункт продаж или сотрудник не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def purchase_product(company: Company) -> None:
    """Закупка товара на склад."""

    clear_screen()

    print("\n=== ЗАКУПКА ТОВАРА ===")

    try:
        wh_id = int(input("ID склада: "))
        product_id = int(input("ID товара: "))
        quantity = int(input("Количество: "))

        warehouse = company.get_warehouse(wh_id)
        if warehouse:
            if warehouse.add_product(product_id, quantity):
                print("✅ Товар закуплен и добавлен на склад")
            else:
                print("❌ Ошибка: склад закрыт")
        else:
            print("❌ Склад не найден")
    except ValueError:
        print("❌ Ошибка: ID и количество должны быть числами")

    input("\nНажмите Enter для продолжения...")


def sell_product(company: Company) -> None:
    """Продажа товара."""

    clear_screen()

    print("\n=== ПРОДАЖА ТОВАРА ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        product_id = int(input("ID товара: "))
        quantity = int(input("Количество: "))

        point = company.get_sale_point(point_id)
        if point:
            product = company.get_product(product_id)
            if product:
                if point.sell_product(product_id, quantity, product.selling_price):
                    print(f"✅ Товар продан! Выручка: {product.selling_price * quantity:.2f}₽")
                else:
                    print("❌ Ошибка: недостаточно товара или пункт закрыт")
            else:
                print("❌ Товар не найден")
        else:
            print("❌ Пункт продаж не найден")
    except ValueError:
        print("❌ Ошибка: ID и количество должны быть числами")

    input("\nНажмите Enter для продолжения...")


def return_product(company: Company) -> None:
    """Возврат товара."""

    clear_screen()

    print("\n=== ВОЗВРАТ ТОВАРА ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        product_id = int(input("ID товара: "))
        quantity = int(input("Количество: "))

        point = company.get_sale_point(point_id)
        if point:
            if point.return_product(product_id, quantity):
                print("✅ Товар возвращен")
            else:
                print("❌ Ошибка: пункт закрыт")
        else:
            print("❌ Пункт продаж не найден")
    except ValueError:
        print("❌ Ошибка: ID и количество должны быть числами")

    input("\nНажмите Enter для продолжения...")


def restock_from_warehouse(company: Company) -> None:
    """Закупка товара со склада в пункт продаж."""

    clear_screen()

    print("\n=== ЗАКУПКА ТОВАРА СО СКЛАДА В ПУНКТ ПРОДАЖ ===")

    try:
        wh_id = int(input("ID склада: "))
        point_id = int(input("ID пункта продаж: "))
        product_id = int(input("ID товара: "))
        quantity = int(input("Количество: "))

        warehouse = company.get_warehouse(wh_id)
        point = company.get_sale_point(point_id)

        if warehouse and point:
            if point.restock_from_warehouse(warehouse, product_id, quantity):
                print("✅ Товар передан в пункт продаж")
            else:
                print("❌ Ошибка: недостаточно товара на складе")
        else:
            print("❌ Склад или пункт продаж не найден")
    except ValueError:
        print("❌ Ошибка: ID и количество должны быть числами")

    input("\nНажмите Enter для продолжения...")


def profitability_company(company: Company) -> None:
    """Доходность предприятия."""

    clear_screen()

    print("\n=== ДОХОДНОСТЬ ПРЕДПРИЯТИЯ ===")
    print(company.get_profitability())
    input("\nНажмите Enter для продолжения...")


def profitability_sale_point(company: Company) -> None:
    """Доходность пункта продаж."""

    clear_screen()

    print("\n=== ДОХОДНОСТЬ ПУНКТА ПРОДАЖ ===")

    try:
        point_id = int(input("ID пункта продаж: "))
        print(company.get_profitability(point_id))
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")

    input("\nНажмите Enter для продолжения...")


def save_data(company: Company) -> None:
    """Сохранение данных."""

    clear_screen()

    print("\n=== СОХРАНЕНИЕ ДАННЫХ ===")
    DataStorage.save(company)
    input("\nНажмите Enter для продолжения...")


def load_data() -> Company:
    """Загрузка данных."""

    clear_screen()

    print("\n=== ЗАГРУЗКА ДАННЫХ ===")
    company = DataStorage.load()
    if company:
        print("✅ Данные загружены успешно")
    else:
        print("❌ Файл не найден, создана новая компания")
        name = input("Введите название предприятия: ")
        company = Company(name)

    input("\nНажмите Enter для продолжения...")

    return company


def main() -> None:
    """Главная функция запуска программы."""

    clear_screen()

    print("=" * 50)
    print("     ДОБРО ПОЖАЛОВАТЬ В CRM СИСТЕМУ")
    print("=" * 50)

    company = DataStorage.load()
    if not company:
        name = input("\nВведите название предприятия: ")
        company = Company(name)
        print(f"✅ Предприятие '{name}' создано!")

    while True:
        print_menu()
        choice = input("\nВыберите действие: ")

        if choice == "1":
            add_product(company)
        elif choice == "2":
            list_products(company)
        elif choice == "3":
            hire_employee(company)
        elif choice == "4":
            fire_employee(company)
        elif choice == "5":
            list_employees(company)
        elif choice == "6":
            open_warehouse(company)
        elif choice == "7":
            close_warehouse(company)
        elif choice == "8":
            warehouse_info(company)
        elif choice == "9":
            warehouse_products(company)
        elif choice == "10":
            move_product(company)
        elif choice == "11":
            assign_warehouse_responsible(company)
        elif choice == "12":
            add_employee_to_warehouse(company)
        elif choice == "13":
            open_sale_point(company)
        elif choice == "14":
            close_sale_point(company)
        elif choice == "15":
            sale_point_info(company)
        elif choice == "16":
            sale_point_products(company)
        elif choice == "17":
            assign_sale_point_responsible(company)
        elif choice == "18":
            add_employee_to_sale_point(company)
        elif choice == "19":
            purchase_product(company)
        elif choice == "20":
            sell_product(company)
        elif choice == "21":
            return_product(company)
        elif choice == "22":
            restock_from_warehouse(company)
        elif choice == "23":
            profitability_company(company)
        elif choice == "24":
            profitability_sale_point(company)
        elif choice == "25":
            save_data(company)
        elif choice == "26":
            company = load_data()
        elif choice == "0":
            save = input("Сохранить данные перед выходом? (y/n): ")
            if save.lower() == 'y':
                DataStorage.save(company)
            print("\nДо свидания!")
            break
        else:
            print("❌ Неверный выбор! Попробуйте снова.")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()