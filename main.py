registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

log_in_username = input("Enter your username: ")
log_in_password = input("Enter your password: ")

available_texts = len(TEXTS)

if registered_users.get(log_in_username) == log_in_password:
    print("Welcome to the app,", log_in_username,
          "\n" + 40 * "-",
          "\nWe have", available_texts, "texts to be analyzed.",
          "\n" + 40 * "-",
          )
    text_selection = input(f"Enter a number btw. 1 and {available_texts} to select: ")
else:
    print("unregistered user, terminating the program...")
    exit()


if not text_selection.isnumeric():
    print("You have to enter a number!")
    exit()

if not (0 < int(text_selection) <= available_texts):
    print("Please choose only from available number of texts!")
    exit()


text_to_analyse = TEXTS[int(text_selection)-1]
chopped_text = text_to_analyse.split()

number_of_words = 0
titlecases = 0
uppercases = 0
lowercases = 0
numeric_strings = 0
all_the_numbers = list()
length_of_words = {}

number_of_words = number_of_words + len(chopped_text)

for word in chopped_text:
    clean_word = word.strip(",.:;!?")
    length = len(clean_word)
    if length > 0:
        if length in length_of_words:
            length_of_words[length] += 1
        else:
            length_of_words[length] = 1
    if clean_word.istitle():
        titlecases = titlecases + 1
    if clean_word.isupper():
        uppercases = uppercases + 1
    if clean_word.islower():
        lowercases = lowercases + 1
    if clean_word.isnumeric():
        numeric_strings = numeric_strings + 1
        all_the_numbers.append(int(clean_word))

print(f"""
----------------------------------------
There are {number_of_words} words in the selected text.
There are {titlecases} titlecase words.
There are {uppercases} uppercase words.
There are {lowercases} lowercase words.
There are {numeric_strings} numeric strings.
The sum of all the numbers {sum(all_the_numbers)}
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------""")

for length, amount in sorted(length_of_words.items()):
    stars = "*" * amount
    print(f"{length:3}| {stars:18} |{amount:5}")