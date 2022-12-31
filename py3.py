from json import loads, dumps
from pympler import asizeof

wel = "Введите номер месяца: "
print(wel)
text = int(input())
my_dict = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
dumped_dict = dumps(my_dict)
"""Перевожу словарь в формат json"""
out_dict = loads(dumped_dict)
for keys in my_dict:
    if text in my_dict[keys]:
        text = keys
        break
print(text)

print('Размер dict: ', asizeof.asizeof(my_dict))
print('Размер json: ', asizeof.asizeof(dumped_dict))
"""Размер словаря уменьшился
Размер dict:  1192
Размер json:  136"""