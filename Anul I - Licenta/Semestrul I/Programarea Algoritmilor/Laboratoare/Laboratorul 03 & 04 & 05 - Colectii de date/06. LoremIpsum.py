sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

letters = {}
for i in range(len(sentence)):
    if sentence[i].lower() not in letters and sentence[i].isalpha():
        letters[sentence[i].lower()] = 1
    elif sentence[i].lower() in letters and sentence[i].isalpha():
        letters[sentence[i].lower()] += 1

for letter in letters:
    print(letter, letters[letter])