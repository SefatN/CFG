def isogram_check(word):
    # Convert the input to lowercase
    word = word.lower()

    # for Loop through each character in the input
    for letter in word:
        # If the character appears more than once, return False
        if word.count(letter) > 1:
            return False

    #if the letter count is less than 1 that is it does not appear more than once it returns true
    return True
print(isogram_check("isogram"))

print(isogram_check("uncopyrightable"))

print(isogram_check("ambidextrously"))

print(isogram_check('hello'))

