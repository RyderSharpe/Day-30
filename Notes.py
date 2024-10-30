# -------------------- ERRORS --------------------
# File not found
with open("afile.txt") as file:
    file.read

# Key error
a_dictionary = {"key": "value"}
value = a_dictionary["non_existant_key"]

# Index error
fruit_list = ["apple", "pear", "ban"]
fruit = fruit_list[3]

# Type error
text = "abc"
print(text + 5)

# -------------------- CATCHING EXCEPTIONS --------------------
try: Something that might cause an exception
except: Do this if there was an exception
else: Do this if there were no exceptions ie. Execute when the thing you're trying all succeeds
finally: Do this no matter what happens.

Example...
try:
    with open("a_file.txt") as file:
        file.read
except:
    print("there was an error")
# ----------------------------------------
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["wegqerbv"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("whatever you want")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
# ----------------------------------------
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("whatever you want")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")

# ----------------------------------------JSON----------------------------------------
# Save data to data_file
with open("data.json", "r") as data_file:

    # -------------UPDATE ('w')-----------
    # reading old data
    data = json.load(data_file)
    # updating old data with new data
    data.update(new_data)

with open("data.json", "w") as data_file:
    # saving updated data
    json.dump(data, data_file, indent=4)

    # -------------WRITE ('w')-----------
    json.dump(new_data, data_file, indent=4)

    # -------------READ ('r')-----------
    data = json.load(data_file)
    print(data)
    print(type(data))
