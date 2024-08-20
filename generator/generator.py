import random
from pathlib import Path
from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        mobile=faker_ru.msisdn(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10000, 20000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


# def generated_file():
#     path = rf'C:\Users\Nik\PycharmProjects\artLessons\filetest{random.randint(0, 99)}.jpeg'
#     file = open(path, "w+")
#     file.write(f'It`s random text for file, {random.randint(0, 99)}')
#     file.close()
#     return file.name, path

def generated_file():
    project_root = Path(__file__).parent.parent.resolve()
    filename = f'filetest{random.randint(0, 99)}.txt'
    path = project_root / filename
    with path.open("w+") as file:
        file.write(f'It`s random text for file, {random.randint(0, 99)}')
    return filename, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )
