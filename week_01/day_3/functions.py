
# def greet():
#     words = "Hey"
#     return words
    
# def greet_1():
#     return words

# print (greet_1())


# name_1 = "Peter"
# time_of_the_day_1= "Morning"
# greeting = greet(name_1,time_of_the_day_1)
# print(greeting)

# name_2 = "Steven"
# time_of_the_day_2= "Afternoon"
# greeting = greet(name_2, time_of_the_day_2)
# print(greeting)

# greeting = greet("Steven", "morning")
# print (greeting)







# my_functions.py
chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]
def count_eggs(list):
    total_eggs = 0

    for item in list:
        total_eggs += item["eggs"]
        item["eggs"] = 0 # eggs have been collected
    return total_eggs

print(count_eggs(chickens))