# Lesson 5 Task 7

import json
result = []
with open('my_ex7.json', 'w', encoding='utf-8') as f:
    with open('my_file7.txt', encoding='utf-8') as f1:
        profit = {}
        for line in f1:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len(
           [int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({"avarage_profit": round(average_profit)})
    json.dump(result, f)




