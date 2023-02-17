# Импортируем функции из пакета, которые будем использовать
from utils.funcs import data_correcting_and_sorting, masking_digits, description

# создаем переменную для списка данных
data = data_correcting_and_sorting()

# создаем цикл, в котором выводим 5 последних операций
for i in range(5):
    print(f"{data[i]['date']} {data[i]['description']}")
    if description(data[i]['description']):
        print(f"{masking_digits(data[i]['to'])}")
    else:
        print(f"{masking_digits(data[i]['from'])} -> {masking_digits(data[i]['to'])}")
    print(f"{data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}")
    print()
