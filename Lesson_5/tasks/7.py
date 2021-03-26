"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:  название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json

firms_info = []

with open('7.txt', encoding='utf-8') as f:
    firms = {}
    profit_list = []

    lines = f.readlines()

    for line in lines:
        line = line.split(' ')
        name = line[0]
        firms[name] = round(float(line[2]) - float(line[3]), 2)
        if firms[name] > 0:
            profit_list.append(firms[name])

    firms_info.append(firms)
    firms_info.append({
        "average_profit": round(sum(profit_list) / len(profit_list), 2)
    })

with open('7.json', 'w', encoding='utf-8') as f_json:
    json.dump(firms_info, f_json)
     
