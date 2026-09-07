#Dictionary Basics

student={
     "name":"Homayra Erin",
     "age":21,
     "city":"Barishal", 
}

print(student)
print(type(student))
for key, value in student.items():
    print(key, ":", value)
print(student["name"])
student["city"]="Dhaka"
print(student)
student["favSubject"]="Math"
print(student)
student.pop("age")
print(student)

#Method
print(student.keys())
print(student.values())
print(student.items())
print(student.get("city"))
print(student.update({"city":"London"}))
print(student)
