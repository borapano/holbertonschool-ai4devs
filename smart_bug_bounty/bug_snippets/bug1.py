def process_students(students):
    total_score = 0
    
    for student in students:
        total_score += student["score"]
    
    average = total_score / len(students)
    return average


students = [
    {"name": "Ana", "score": 80},
    {"name": "Beni", "score": 90},
    {"name": "Cila", "score": 75}
]

if len(students) > 0
    avg = process_students(students)
    print("Average score:", avg)
else:
    print("No students found")

print("Process completed")