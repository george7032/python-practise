students = [
    {"name": "George", "class": "1", "dorm": "Amazon"},
    {"name" : "Peter", "class": "2", "dorm": "Tsavo"},
    {"name": "Sammy", "class": "3", "dorm": "Amboseli"},
    {"name": "Ben", "class": "4", "dorm": "Serengeti"}
]

for student in students:
    print(student["name"], student["dorm"], student["class"], sep="-")
