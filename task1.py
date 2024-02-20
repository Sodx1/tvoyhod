import pandas as pd
from faker import Faker
import random
from datetime import datetime
import time

print('Создается DataFrame пожалуйста подожди!')
start_time = time.time()
# Создание фиктивных данных
# https://faker.readthedocs.io/en/master/#
fake = Faker('ru_RU')

# Генерация данных для 1 миллиона записей
data = {
    'id': range(1, 1000001),
    'ФИО': [fake.name() for _ in range(1000000)],
    'Дата рождения': [fake.date_of_birth(minimum_age=18, maximum_age=40) for _ in range(1000000)],
    'Номер телефона': [fake.phone_number() for _ in range(1000000)],
    'Регион': [fake.region() for _ in range(1000000)],
    'Дата регистрации': [fake.date_between(start_date='-5y', end_date='today') for _ in range(1000000)],
    'Курс обучения': [random.choice(['Курс1', 'Курс2', 'Курс3', 'Курс 4']) for _ in range(1000000)],
    'Вуз': [fake.company() for _ in range(1000000)]
}


# Создание DataFrame
df = pd.DataFrame(data)


# А. Количество регистраций по регионам
registrations_by_region = df['Регион'].value_counts()
print("A. Количество регистраций по регионам:")
print(registrations_by_region)
print()

# Б. Количество регистраций за определенный промежуток времени
# Промежутки задаются в формате datetime(год, месяц, число)
start_date = datetime(2024, 1, 1).date()
end_date = datetime(2024, 12, 31).date()
mask = (df['Дата регистрации'] >= start_date) & (df['Дата регистрации'] <= end_date)
registrations_within_period = df.loc[mask]
print("B. Количество регистраций за период с", start_date, "по", end_date, ":")
print(registrations_within_period.shape[0])
print()

# В. Отобразить пользователей в возрасте от 18 до 35 лет
current_year = datetime.now().year
df['возраст'] = df['Дата рождения'].apply(lambda x: current_year - x.year)
users_age_18_to_35 = df[(df['возраст'] >= 18) & (df['возраст'] <= 35)]
print("В. Пользователи в возрасте от 18 до 35 лет:")
print(users_age_18_to_35)

end_time = time.time()
exection_time = end_time - start_time
print(f"Время выполнения {round(exection_time)} сек.")