# code to show a sample hashtable in python

# create a hashtable at once

items1 = dict({"key1": 1, "key2":2, "key3": 3})
print(items1)

# create a hashtable progessively

items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# replacing an item

items2["key2"] = "two"
print(items2)

# iterate the key and values in dictionary 
for key, value in items2.items():
    print("Key: ", key, " value: ", value)
