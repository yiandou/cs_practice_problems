students = {"Bowie": "F", "Kalp": "F", "Jacob": "D", "Jonathan": "A", "Kaleb": "B+"}

students["Jacob"] = "F"
students["Ian"] = "A-"

del students["Jacob"]

num_f = 0
for key in students:
    if (students[key] == "F"):
        num_f = num_f +1

print(num_f)
