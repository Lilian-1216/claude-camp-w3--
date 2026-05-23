import json

f = open("students.csv", "r")
content = f.read()  
f.close()

def total_students():
    lines = content.split("\n")
    count = 0
    for line in lines[1:]:   
        if line:             
            count += 1
    return count

def students_per_country():
    students_per_country = {}
    lines = content.split("\n")
    for line in lines[1:]:
        if line:
            country = line.split(",")[3]
            if country in students_per_country:
                students_per_country[country] += 1
            else:
                students_per_country[country] = 1
    return students_per_country

def students_bet_percentage():
    counts = {}
    lines = content.split("\n")
    for line in lines[1:]:
        if line:
            bet = line.split(",")[4]    
            if bet in counts:
                counts[bet] += 1
            else:
                counts[bet] = 1
    
    # 算完成率
    total = sum(counts.values())
    if "completed" in counts:
        completed = counts["completed"]
    else:
        completed = 0
    rate = completed / total
    
    return {"counts": counts, "completion_rate": rate}

print("Total number of students:", total_students())
print("Number of students per country:", students_per_country())
print("Percentage of students who bet:", students_bet_percentage())


with open("students_analysis.json", "w") as json_file:
    json.dump({
        "total_students": total_students(),
        "students_per_country": students_per_country(),
        "students_bet_percentage": students_bet_percentage()
    }, json_file, indent=4)




