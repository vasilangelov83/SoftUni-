def avg(values):
    return sum(values) / len(values)
students_dict = {}

for _ in range(int(input())):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_dict:
        students_dict[name] = []
        students_dict[name].append(grade)
    else:
        students_dict[name].append(grade)

for name, grades in students_dict.items():
    grades_formatted = " ".join(f'{grade:.2f}' for grade in grades)

    average = avg(grades)
    print(f"{name} -> {grades_formatted} (avg: {average:.2f})")