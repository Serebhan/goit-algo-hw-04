
from pathlib import Path

def total_salary(path):
    path=Path(path)
    try:
        with open(path, encoding='utf-8') as f:
            lines=f.readlines()
    except FileNotFoundError:
        print (f"Оце так, файлу {path} не можу знайти")
    i=0
    total_salary=0
    for line in lines:
        _,salary = line.split(",")
        total_salary=int(salary)+total_salary
        i+=1
    median_salary=total_salary/i

    return total_salary, median_salary


total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")