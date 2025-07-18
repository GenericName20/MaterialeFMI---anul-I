def task_1():
    print("Task 1:")
    sentence = input().strip()
    words = [x + "p" + x for x in "aeiou"] + [x + "P" + x for x in "AEIOU"]
    
    for word in words:
        sentence = sentence.replace(word[0], word)
    print(sentence.capitalize())

    for word in words:
        sentence = sentence.replace(word, word[0])
    print(sentence.capitalize(), end="\n\n")

def task_2():
    print("Task 2:")
    sentence = input().strip()
    sentence += " "
    wordsHyphen = [x + "p" + x + "-" for x in "aeiou"] + [x + "P" + x + "-" for x in "AEIOU"]
    wordsSpace = [x + "p" + x for x in "aeiou"] + [x + "P" + x for x in "AEIOU"]

    for word in wordsHyphen:
        sentence = sentence.replace(word[2] + word[3], word)

    for word in wordsSpace:
        sentence = sentence.replace(word[0] + " ", word + " ")
    
    print(sentence.capitalize())
    print(sentence.replace("-", "").capitalize())

    for word in wordsHyphen:
        sentence = sentence.replace(word, word[2] + word[3])

    for word in wordsSpace:
        sentence = sentence.replace(word + " ", word[0] + " ")

    print(sentence.capitalize())

task_1()
task_2()