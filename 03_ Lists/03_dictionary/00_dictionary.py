thisdictionary = {
    "Brand" : "Ford" ,
    "Model" : "Mustang" ,
    "Year" :   2023
    }


'''
{'Brand': 'Ford', 'Model': 'Mustang', 'Year': 2023}

'''


print(thisdictionary)

x = thisdictionary["Brand"]
print(x)

''' output
Ford'''

y = thisdictionary.get("Model")
z = thisdictionary["Model"]

print(y)
print(z)