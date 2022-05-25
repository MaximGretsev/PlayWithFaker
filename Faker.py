import json

from faker import Faker


fake_ru = Faker('ru_RU')

# print(fake_ru.simple_profile())
# print(fake_ru.isbn10())

# fake_ru.phone_number
# fake_ru.job
# fake_ru.address

faker_dict = {}

for i in range(1, 251):
    faker_name = fake_ru.name()
    faker_job = fake_ru.job()
    faker_address = fake_ru.address()
    faker_phone = fake_ru.phone_number()
    faker_email = fake_ru.ascii_email()
    faker_city = fake_ru.city()
    faker_dict[i] = {
        "Number_of_people": i,
        "Name": faker_name,
        "City": faker_city,
        "Address": faker_address,
        "Job": faker_job,
        "Phone": faker_phone,
        "email": faker_email
         }
    with open('list_of_peoples.json', 'w', encoding='utf8') as file:
        json.dump(faker_dict, file, indent=4, ensure_ascii=False)





