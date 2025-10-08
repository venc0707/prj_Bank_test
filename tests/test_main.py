import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import sys
import os


from main import (main, financial_transaction, filter_by_state, sort_by_date, filter_by_currency, process_bank_search,
                  process_bank_operations, get_date, mask_account_card, amount_transaction)


class TestMainFunction(unittest.TestCase):

    def setUp(self):
        """Настройка тестовых данных"""
        self.test_transactions = [
            {
                'id': 1,
                'state': 'EXECUTED',
                'date': '2023-11-12T16:17:52Z',
                'operationAmount': {
                    'amount': 1000.0,
                    'currency': {
                        'code': 'RUB',
                        'name': 'Russian Ruble'
                    }
                },
                'description': 'Payment for services',
                'from': 'Visa 1234567812345678',
                'to': 'Account 987654321'
            },
            {
                'id': 2,
                'state': 'CANCELED',
                'date': '2023-10-10T10:00:00Z',
                'operationAmount': {
                    'amount': 500.0,
                    'currency': {
                        'code': 'USD',
                        'name': 'US Dollar'
                    }
                },
                'description': 'Online purchase',
                'from': 'MasterCard 1111222233334444',
                'to': 'Account 5555666677778888'
            }
        ]

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('main.financial_transaction')
    def test_main_json_executed_rub(self, mock_financial, mock_print, mock_input):
        """Тест основного сценария: JSON, EXECUTED, рублевые транзакции"""
        # Мокируем ввод пользователя
        input_responses = [
            '1',  # JSON файл
            'EXECUTED',  # статус
            'нет',  # сортировка по дате
            'да',  # только рублевые
            'нет'  # фильтр по описанию
        ]
        mock_input.side_effect = input_responses

        # Мокируем возвращаемые данные
        mock_financial.return_value = self.test_transactions

        # Мокируем вспомогательные функции
        with patch('main.filter_by_state') as mock_filter_state, \
                patch('main.filter_by_currency') as mock_filter_currency, \
                patch('main.process_bank_operations') as mock_process_ops, \
                patch('main.get_date') as mock_get_date, \
                patch('main.mask_account_card') as mock_mask:
            mock_filter_state.return_value = [self.test_transactions[0]]
            mock_filter_currency.return_value = (x for x in [self.test_transactions[0]])
            mock_process_ops.return_value = {'Payment': 1}
            mock_get_date.return_value = '12.11.2023'
            mock_mask.return_value = 'Visa 1234 56** **** 5678'

            # Вызываем основную функцию
            main()

            # Проверяем вызовы функций
            mock_financial.assert_called_once_with('data/operations.json')
            mock_filter_state.assert_called_once_with(self.test_transactions, 'EXECUTED')

    @patch('builtins.input')
    @patch('main.get_data_is_csv_xlsx')
    def test_main_csv_canceled(self, mock_get_data, mock_input):
        """Тест сценария с CSV файлом и статусом CANCELED"""
        input_responses = [
            '2',  # CSV файл
            'CANCELED',  # статус
            'да',  # сортировка по дате
            'по убыванию',  # направление сортировки
            'нет',  # только рублевые
            'нет'  # фильтр по описанию
        ]
        mock_input.side_effect = input_responses
        mock_get_data.return_value = self.test_transactions

        with patch('main.filter_by_state') as mock_filter_state, \
                patch('main.sort_by_date') as mock_sort, \
                patch('main.process_bank_operations') as mock_process_ops:
            mock_filter_state.return_value = [self.test_transactions[1]]
            mock_sort.return_value = [self.test_transactions[1]]
            mock_process_ops.return_value = {'Online': 1}

            main()

            mock_get_data.assert_called_once_with('data/transactions.csv')
            mock_filter_state.assert_called_once_with(self.test_transactions, 'CANCELED')

    @patch('builtins.input')
    @patch('main.get_data_is_csv_xlsx')
    def test_main_xlsx_with_description_filter(self, mock_get_data, mock_input):
        """Тест сценария с XLSX и фильтром по описанию"""
        input_responses = [
            '3',  # XLSX файл
            'PENDING',  # статус
            'нет',  # сортировка по дате
            'нет',  # только рублевые
            'да',  # фильтр по описанию
            'Online'  # слово для фильтра
        ]
        mock_input.side_effect = input_responses
        mock_get_data.return_value = self.test_transactions

        with patch('main.filter_by_state') as mock_filter_state, \
                patch('main.process_bank_search') as mock_search:
            mock_filter_state.return_value = self.test_transactions
            mock_search.return_value = [self.test_transactions[1]]

            main()

            mock_search.assert_called_once_with(self.test_transactions, 'Online')

    @patch('builtins.input')
    @patch('main.financial_transaction')
    def test_main_invalid_file_format_then_valid(self, mock_financial, mock_input):
        """Тест обработки неверного формата файла с последующим исправлением"""
        input_responses = [
            '5',  # неверный формат
            '1',  # затем верный формат (JSON)
            'EXECUTED',  # статус
            'нет',  # сортировка по дате
            'нет',  # только рублевые
            'нет'  # фильтр по описанию
        ]
        mock_input.side_effect = input_responses
        mock_financial.return_value = self.test_transactions

        with patch('main.filter_by_state') as mock_filter_state:
            mock_filter_state.return_value = [self.test_transactions[0]]

            main()

            # Должен быть вызван с правильным путем
            mock_financial.assert_called_once_with('data/operations.json')

    @patch('builtins.input')
    @patch('main.financial_transaction')
    def test_main_invalid_status_then_valid(self, mock_financial, mock_input):
        """Тест обработки неверного статуса с последующим исправлением"""
        input_responses = [
            '1',  # JSON файл
            'INVALID',  # неверный статус
            'EXECUTED',  # затем верный статус
            'нет',  # сортировка по дате
            'нет',  # только рублевые
            'нет'  # фильтр по описанию
        ]
        mock_input.side_effect = input_responses
        mock_financial.return_value = self.test_transactions

        with patch('main.filter_by_state') as mock_filter_state:
            mock_filter_state.return_value = [self.test_transactions[0]]

            main()

            mock_filter_state.assert_called_once_with(self.test_transactions, 'EXECUTED')

    def test_filter_by_state(self):
        """Тест фильтрации по статусу"""
        from src.processing import filter_by_state

        result = filter_by_state(self.test_transactions, 'EXECUTED')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)

        result = filter_by_state(self.test_transactions, 'CANCELED')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 2)

    def test_filter_by_currency(self):
        """Тест фильтрации по валюте"""
        from src.generators import filter_by_currency

        # Создаем генератор
        generator = filter_by_currency(self.test_transactions, 'RUB')
        # Преобразуем в список для проверки
        result = list(generator)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)
        self.assertEqual(result[0]['operationAmount']['currency']['code'], 'RUB')

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output_structure(self, mock_stdout):
        """Тест структуры вывода"""
        with patch('builtins.input') as mock_input, \
                patch('main.financial_transaction') as mock_financial:
            mock_input.side_effect = ['1', 'EXECUTED', 'нет', 'нет', 'нет']
            mock_financial.return_value = [self.test_transactions[0]]

            with patch('main.filter_by_state') as mock_filter_state, \
                    patch('main.get_date') as mock_get_date, \
                    patch('main.mask_account_card') as mock_mask:
                mock_filter_state.return_value = [self.test_transactions[0]]
                mock_get_date.return_value = '12.11.2023'
                mock_mask.return_value = 'Visa 1234 56** **** 5678 -> Account **4321'

                main()

                output = mock_stdout.getvalue()
                self.assertIn('Распечатываю итоговый список транзакций', output)
                self.assertIn('Всего банковских операций в выборке', output)

    def test_error_handling(self):
        """Тест обработки ошибок"""
        with patch('builtins.input') as mock_input, \
                patch('main.financial_transaction') as mock_financial:
            mock_input.side_effect = ['1', 'EXECUTED', 'нет', 'нет', 'нет']
            # Симулируем исключение
            mock_financial.side_effect = Exception("Test error")

            with patch('builtins.print') as mock_print:
                main()
                # Проверяем, что ошибка была обработана и выведена
                mock_print.assert_any_call('Test error')


if __name__ == '__main__':
    # Запуск тестов
    unittest.main()