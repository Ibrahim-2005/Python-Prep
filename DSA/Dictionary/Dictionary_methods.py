"""
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
clear()	        Removes all the elements from the dictionary

"""

dict1 = {"First_Name": "Mohamed", "Last_Name": "Ibrahim", "Age": 20, "Location": "Chennai"}

dict_copy = dict1.copy()
print(dict_copy)


keys = ["Name", "Age", "Place"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)


age = dict1.get("Age")
print(age)

print(dict1.items())

print(dict1.keys())

print(dict1.values())


removed_value = dict1.pop("Location")
print(dict1)


last_item = dict1.popitem()
print(dict1)


default_age = dict1.setdefault("Age", 25)
print(dict1)


default_city = dict1.setdefault("City", "Coimbatore")
print(dict1)


dict1.update({"Country": "India", "Gender": "Male"})
print(dict1)


dict1.clear()
print(dict1)

del dict1