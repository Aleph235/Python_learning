def make_car(manufacturer, model_name,**car_info):
    """make a car with manufacturer and model_name and more info"""
    car_info['manufacturer']= manufacturer
    car_info['model_name']= model_name
    return car_info

my_car = make_car('Renault','clio',color = 'blue',shape = 'classic')
your_car = make_car('BMW','serie3',color = 'red',shape = 'coupe')

print(my_car)
print(your_car)

