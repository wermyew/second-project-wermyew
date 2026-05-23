from core import (
    Product,
    Employee,
    Warehouse,
    SalePoint,
    Company,
    StorageCell
)
import json
from typing import Optional
import os


class DataStorage:
    """Класс для работы с файлами (сохранение/загрузка)."""

    @staticmethod
    def save(company: Company, filename: str = "crm_data.json") -> None:
        """
        Сохранить все данные компании в файл.

        :param company: объект компании для сохранения.
        :param filename: имя файла для сохранения.
        """

        data = {
            'company_name': company.name,
            'products': [],
            'employees': [],
            'warehouses': [],
            'sale_points': []
        }

        # сохраняем товары
        for product in company.products.values():
            data['products'].append({
                'id': product.id,
                'name': product.name,
                'purchase_price': product.purchase_price,
                'selling_price': product.selling_price
            })

        # сохраняем сотрудников
        for emp in company.employees.values():
            data['employees'].append({
                'id': emp.id,
                'full_name': emp.full_name,
                'position': emp.position,
                'salary': emp.salary,
                'is_active': emp.is_active
            })

        # сохраняем склады
        for wh in company.warehouses.values():
            cells_data = []
            for cell_id, cell in wh.cells.items():
                cells_data.append([cell_id, cell.product_id, cell.quantity])
            data['warehouses'].append({
                'id': wh.id,
                'name': wh.name,
                'address': wh.address,
                'cells': cells_data,
                'employees': wh.employees,
                'responsible_employee_id': wh.responsible_employee_id,
                'is_open': wh.is_open
            })

        # сохраняем пункты продаж
        for sp in company.sale_points.values():
            data['sale_points'].append({
                'id': sp.id,
                'name': sp.name,
                'address': sp.address,
                'inventory': sp.inventory,
                'employees': sp.employees,
                'responsible_employee_id': sp.responsible_employee_id,
                'is_open': sp.is_open,
                'total_revenue': sp.total_revenue
            })

        # запись в файл
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ Данные сохранены в {filename}")

    @staticmethod
    def load(filename: str = "crm_data.json") -> Optional[Company]:
        """
        Загрузить данные из файла.

        :param filename: имя файла для загрузки.

        :return: объект компании или None если файл не найден.
        """

        if not os.path.exists(filename):

            return None

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        company = Company(data['company_name'])

        # восстанавливаем товары
        max_product_id = 0
        for p_data in data.get('products', []):
            product = Product(p_data['name'], p_data['purchase_price'], p_data['selling_price'])
            product.id = p_data['id']
            company.products[product.id] = product
            max_product_id = max(max_product_id, product.id)
        Product._next_id = max_product_id + 1

        # восстанавливаем сотрудников
        max_emp_id = 0
        for e_data in data.get('employees', []):
            emp = Employee(e_data['full_name'], e_data['position'], e_data['salary'])
            emp.id = e_data['id']
            emp.is_active = e_data['is_active']
            company.employees[emp.id] = emp
            max_emp_id = max(max_emp_id, emp.id)
        Employee._next_id = max_emp_id + 1

        # восстанавливаем склады
        max_wh_id = 0
        for wh_data in data.get('warehouses', []):
            wh = Warehouse(wh_data['name'], wh_data['address'])
            wh.id = wh_data['id']

            # восстанавливаем ячейки
            for cell_id, product_id, quantity in wh_data.get('cells', []):
                cell = StorageCell(product_id, quantity)
                cell.id = cell_id
                wh.cells[cell_id] = cell

            wh.employees = wh_data.get('employees', [])
            wh.responsible_employee_id = wh_data.get('responsible_employee_id')
            wh.is_open = wh_data.get('is_open', True)
            company.warehouses[wh.id] = wh
            max_wh_id = max(max_wh_id, wh.id)
        Warehouse._next_id = max_wh_id + 1

        # восстанавливаем пункты продаж
        max_sp_id = 0
        for sp_data in data.get('sale_points', []):
            sp = SalePoint(sp_data['name'], sp_data['address'])
            sp.id = sp_data['id']
            sp.inventory = sp_data.get('inventory', {})
            sp.employees = sp_data.get('employees', [])
            sp.responsible_employee_id = sp_data.get('responsible_employee_id')
            sp.is_open = sp_data.get('is_open', True)
            sp.total_revenue = sp_data.get('total_revenue', 0)
            company.sale_points[sp.id] = sp
            max_sp_id = max(max_sp_id, sp.id)
        SalePoint._next_id = max_sp_id + 1

        print(f"✅ Данные загружены из {filename}")

        return company