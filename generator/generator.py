import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10000, 20000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generated_file():
    path = rf'C:\Users\Nik\PycharmProjects\artLessons\filetest{random.randint(0, 99)}.txt'
    file = open(path, "w+")
    file.write(f'It`s random text for file, {random.randint(0, 99)}')
    file.close()
    return file.name, path

