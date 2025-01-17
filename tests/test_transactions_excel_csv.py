from unittest.mock import patch

import pandas as pd

from src.transactions_excel_csv import read_transactions_csv, read_transactions_excel


def test_transactions_excel():
    with patch('pandas.read_excel') as mock_read_excel:
        mock_data = pd.DataFrame(columns=['date', 'amount', 'description'])
        mock_read_excel.return_value = mock_data
        result = read_transactions_excel('dummy_file.excel')
        expected_result = []
        assert result == expected_result
        mock_read_excel.assert_called_once_with('dummy_file.excel')


def test_transactions_csv():
    with patch('pandas.read_csv') as mock_read_csv:
        mock_data = pd.DataFrame(columns=['date', 'amount', 'description'])
        mock_read_csv.return_value = mock_data
        result = read_transactions_csv('dummy_file.csv')
        expected_result = []
        assert result == expected_result
        mock_read_csv.assert_called_once_with('dummy_file.csv', sep=';')


def test_read_transactions_csv_file_not_found():
    with patch('pandas.read_csv', side_effect=FileNotFoundError):
        result = read_transactions_csv('non_existent_file.csv')

        expected = []
        assert result == expected, f'Expected {expected}, but got {result}'


def test_read_transactions_excel_file_not_found():
    with patch('pandas.read_excel', side_effect=FileNotFoundError):
        result = read_transactions_excel('non_existent_file.xlsx')

        expected = []
        assert result == expected, f'Expected {expected}, but got {result}'
