dog = dict()
dog = {"name": "Fairy", "color": "Brown", "breed": "pug", "legs": 4, "age": 3}
student_dictionary = {"first_name": "Rabia Aminu", "last_name": "Ahmad", "gender": "F", "age": 23, "marital_status": "Single", "skills": ["Computer scientist"], "country": "Nigeria", "city": "Kano", "address": "Sharada phase 1"}
print(len(student_dictionary))
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
student_dictionary["skills"].append("Reading")
list_keys = list(student_dictionary.keys())
list_values = list(student_dictionary.values())
list_of_tuples = [(r, a) for r, a in student_dictionary.items()]
student_dictionary.pop("gender")
del dog
