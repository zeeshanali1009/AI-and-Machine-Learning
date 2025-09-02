# pop method is used to remove the record of the particular item of the particualr dictionary

car_record = {"name": "Car", "model" : "latest model", "make": "latest"}

car_record_items = car_record.pop("make", "not found!")
print(car_record_items)