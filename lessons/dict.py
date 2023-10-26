"""Practice with dictionary syntax."""

# Creating a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my dictionary: ")
print(ice_cream)

# Addings a key, value pair
ice_cream["mint"] = 3
print("Added mint to my dictionary: ")
print(ice_cream)

# Removing a key, valye pair
ice_cream.pop("mint")
print("Removed mint: ")
print(ice_cream)

# Printing how many orders of chocolate
print(f"There are {ice_cream['chocolate']} orders of chocolate.")

# Updating a value (vanilla orders)
ice_cream["vanilla"] = 10
# ice_cream["vanilla"] += 2
print("After updating vanilla:")
print(ice_cream)

#Print the length
print(f"There are {len(ice_cream)} flavors.")

# Checking if values are in dictionary
print("chocolate in dictionary?")
print("chocolate"in ice_cream)
print("mint in dictionary?")
print("mint" in ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint.")

# Printing values of keys
for flavor in ice_cream:
    # print out <flavor> has <num order> orders
    print(f"{flavor} has {ice_cream[flavor]} orders.")