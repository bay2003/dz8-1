import unittest
import os
from unittest.mock import patch

import dz8  # Импортируйте ваш модуль

class TestDz(unittest.TestCase):

    def setUp(self):
        # Инициализация данных перед каждым тестом
        self.fe = 'test_orders_pik09.txt'
        self.history_file = 'test_purchase_history.json'
        dz8.total_cost = 0
        dz8.purchase_history = []
        dz8.orders = []

    def tearDown(self):
        # Удаление временных файлов после каждого теста
        if os.path.exists(self.fe):
            os.remove(self.fe)
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
        if os.path.exists('listdir.txt'):
            os.remove('listdir.txt')

    def test_add_purchase(self):
        # Проверка функции добавления покупки
        name = 'Тестовый товар'
        cost = 10.0

        # Вызываем функцию добавления покупки
        dz8.orders.append((name, cost))
        dz8.total_cost += cost

        # Проверяем, что товар добавлен корректно
        self.assertEqual(len(dz8.orders), 1)
        self.assertEqual(dz8.orders[0], (name, cost))
        self.assertEqual(dz8.total_cost, cost)

    @patch('builtins.print')
    def test_show_purchase_history(self, mock_print):
        # Проверка функции отображения истории покупок
        dz8.purchase_history = [{"name": "Товар1", "cost": 10.0}, {"name": "Товар2", "cost": 20.0}]

        # Вызываем функцию отображения истории
        dz8.show_purchase_history()

        # Проверяем, что вывод соответствует ожиданиям
        expected_output = [
            "История покупок:",
            'Товар: Товар1, Цена: 10.0',
            'Товар: Товар2, Цена: 20.0'
        ]
        calls = [unittest.mock.call(item) for item in expected_output]
        mock_print.assert_has_calls(calls, any_order=True)


