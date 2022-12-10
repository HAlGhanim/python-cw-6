# الجزء الاول
person = {
    "name":"Humoud",
    "age":"23",
    "hobbies": ["Coding", "Gaming", "Boxing"]
}

print(person["name"])
print(person["age"])

# الجزء الثاني
person["age"] = "25"
person["country"] = "Kuwait"
print(person)
print(len(person))

# الجزء الثالث
person["hobbies"] = "Coding", "Gaming", "Boxing", "Sleeping"
def check_hobbies(person):
    if len(person["hobbies"]) > 3:
        print("WOW YOU ARE AMAZING")
check_hobbies(person)