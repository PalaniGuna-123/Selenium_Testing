add = lambda a,b : a+b
print(add(12,1))

data=[
    {"name": "Guna" , "Age": 19},
    {"name": "Gokul", "Age" : 17}
]
print(data[1]["name"])


numbers=[1,2,3,4,5,6]
squared_numbers=map(lambda x : x * 2 , numbers)
print(list(squared_numbers))

filtered_numbers=filter(lambda x:x%2==0, numbers)
print(list(filtered_numbers))