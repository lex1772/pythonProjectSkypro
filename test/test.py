# Импортируем pytest и функции для тестирования
import pytest
import coverage
from utils.funcs import load_executed_operations, data_correcting_and_sorting, masking_digits


class Test:
    '''Создаем класс для теслирования и прописываем функции, которые будем тестировать'''

    def test_load_operations(self):
        assert load_executed_operations(), "Тест не пройден"

    def test_data(self):
        assert data_correcting_and_sorting(), "Тест не пройден"

    def test_masking_digits_card(self):
        assert masking_digits("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199", "Тест не пройден"

    def test_masking_digits_account(self):
        assert masking_digits("Счет 64686473678894779589") == "счет **9589", "Тест не пройден"

    '''Вызываем функции при запуске скрипта'''
    if __name__ == '__main--':
        pytest.main()
