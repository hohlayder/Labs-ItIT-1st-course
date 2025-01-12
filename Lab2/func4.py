def describe_person(name, age=30):
    print(
        f'Имя: {name}; Возраст: {age} {"лет" if age % 10 >= 5 or age % 10 == 0 or age // 10 % 10 == 1 else ("год" if age % 10 == 1 else "года")}')


describe_person("Женя")
describe_person("Даня", 21)
