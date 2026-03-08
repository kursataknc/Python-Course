import pandas
import os

script_directory = os.path.dirname(__file__)
csv_path = os.path.join(script_directory, "nato_phonetic_alphabet.csv")

data = pandas.read_csv(csv_path)
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_input = input("Enter a Word: ").upper()
    try:
        phonetic_output = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_output)

generate_phonetic()