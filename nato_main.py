# ---------------------ORIGINAL CODE--------------------
# import pandas
#
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# # Create a dictionary using dictionary comprehension
# p_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#
# # Get user input and convert it to uppercase to match dictionary keys
# user_input = input(str("Enter a string: ")).upper()
#
# # Iterate through each letter in the user input
# nato_output = [p_dict[letter] for letter in user_input]
# # nato_output = [p_dict.get(letter) for letter in user_input]
#
# print(nato_output)

# --------------MY VERSION gpt----------------

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary using dictionary comprehension
p_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def get_user_input():
    user_input = input(str("Enter a string: ")).upper()
    nato_output = []
    for letter in user_input:
        code = p_dict.get(letter)
        if code:
            nato_output.append(code)
        else:
            print("Only use letters.")
            return get_user_input()  # Recursive call
    return nato_output

nato_output = get_user_input()
print(nato_output)

# ------------------ CLASS VERSION part 1 -----------------

# import pandas
#
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# # Create a dictionary using dictionary comprehension
# p_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#
# # Get user input and convert it to uppercase to match dictionary keys
# user_input = input(str("Enter a string: ")).upper()
#
# try:
#     # Iterate through each letter in the user input
#     # Occasionally problematic
#     nato_output = [p_dict[letter] for letter in user_input]
#
# except KeyError:
#     print("nar")
#
# else:
#     print(nato_output)

# ------ CLASS VERSION part 2 -------

# import pandas
#
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# # Create a dictionary using dictionary comprehension
# p_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#
# def generate_phonetic():
#     user_input = input(str("Enter a string: ")).upper()
#     try:
#         nato_output = [p_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Gnar! Use letters mate!")
#         generate_phonetic()
#     else:
#         print(nato_output)
#
# generate_phonetic()