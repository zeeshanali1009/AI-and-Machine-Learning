# get method is used to get the particualar key 's value

car_record = {"name": "Car", "model" : "latest model", "make": "latest"}
print(f"The dictionary is {car_record}")
car_model = car_record.get("model","not found")
print(f"The model of the car is : {car_model}")