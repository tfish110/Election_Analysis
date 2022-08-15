my_info = {"name": "Rex",
"age": 3,
"hobbies": ["barking", "eating", "sleeping", "loving my owner"],
"wake-up":{"Mon": 5, "Fri": 5, "Sat": 7, "Sunday": 7}
}

print(f"Hello I am {my_info['name']} and I am {my_info['age']}")
print(f"I have {len(my_info['hobbies'])} hobbies!")
print(f"One of my favorite hobbies is {my_info['hobbies'][0]}")
print(f"On Saturday I get up at {my_info['wake-up']['Sat']}")