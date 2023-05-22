car = { "Brand" : "Ford" ,
    "Model" : "Mustang" ,
    "Year" :   2022 ,   
}

car.pop("Model")

car.update({"Year" : 2026})

# del car["Brand"]

# car.clear

car.popitem()

print(car)
'''
for pop {'Brand': 'Ford', 'Year': 2022}

for update {'Brand': 'Ford', 'Year': 2026}

for del {'Year': 2026} 

del car (car is not defined)

for popitem {'Brand': 'Ford'}

for clear {}


'''

