car = { "Brand" : "Ford" ,
    "Model" : "Mustang" ,
    "Year" :   2022 ,   
}

x = car.keys()
y = car.values()
z = car.items()
'''

dict_keys(['Brand', 'Model', 'Year'])dict_values(['Ford', 'Mustang', 2022])
dict_items([('Brand', 'Ford'), ('Model', 'Mustang'), ('Year', 2022)])
dict_keys(['Brand', 'Model', 'Year', 'color'])

'''
print(x)
print(y)
print(z)
car["color"] = "white"
car["Year"] = 2023
print(x)

'''
dict_items([('Brand', 'Ford'), ('Model', 'Mustang'), ('Year', 2022)])
'''