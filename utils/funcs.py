import requests
from datetime import datetime

DATA_SOURCE = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676711634694&signature=uelI_cqcmX-NRRaGmDXro1aj2I3oVR8Xd-cULayjQmQ&downloadName=operations.json'


def load_executed_operations():
    response = requests.get(DATA_SOURCE, verify=False)
    data = response.json()
    executed_operations = []
    for i in range(len(data)):
        if len(data[i]) == 0:
            pass
        elif data[i]['state'] == "EXECUTED":
            executed_operations.append(data[i])
    return executed_operations

def date_correcting_and_sorting():
    data = load_executed_operations()
    for element in data:
        year, month, day = element['date'][:10].split('-')
        element['date'] = f'{day}.{month}.{year}'
    sorted_data = sorted(data, key=lambda date: datetime.strptime(date['date'], '%d.%m.%Y'), reverse=True)
    return sorted_data
