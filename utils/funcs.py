# Импортируем requests для работы с данными по ссылке и datetime для перевода даты
import requests
from datetime import datetime

# Прописываем переменную для ссылки
DATA_SOURCE = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676711634694&signature=uelI_cqcmX-NRRaGmDXro1aj2I3oVR8Xd-cULayjQmQ&downloadName=operations.json'


def load_executed_operations():
    '''Функция для выгрузки всех успешных операций из .json файла'''
    response = requests.get(DATA_SOURCE, verify=False)
    data = response.json()
    executed_operations = []
    for i in range(len(data)):
        if len(data[i]) == 0:
            pass
        elif data[i]['state'] == "EXECUTED":
            executed_operations.append(data[i])
    return executed_operations


def data_correcting_and_sorting():
    '''Функция для перевода формата даты и сортировки по возрастанию даты операции'''
    data = load_executed_operations()
    for element in data:
        year, month, day = element['date'][:10].split('-')
        element['date'] = f'{day}.{month}.{year}'
    sorted_data = sorted(data, key=lambda date: datetime.strptime(date['date'], '%d.%m.%Y'), reverse=True)
    return sorted_data


def masking_digits(number):
    '''функция для маскировки цифр в номере счета и карте'''
    if "Счет" in number:
        return f'счет **{number[-4:]}'
    else:
        data_list = number.split()
        card_number = data_list[-1]
        card_type = ' '.join(data_list[:-1])
        list_card_number = list(card_number)
        for i in range(6, 12):
            list_card_number[i] = '*'
        card_number = []
        for i in range(0, len(list_card_number), 4):
            card_number.append(list_card_number[i:i + 4])
        correct_card_number = ''
        for i in range(len(card_number)):
            numbers = "".join(card_number[i])
            correct_card_number += numbers + " "
        return f'{card_type} {correct_card_number[:-1]}'


def description(description):
    '''функция проверки на открытие вклада'''
    if "Открытие вклада" in description:
        return True
    else:
        return False
