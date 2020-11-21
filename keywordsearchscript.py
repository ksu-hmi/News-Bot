# Module 4.3
# [ ] create Get Name program

while True:
    familar_name = input("Enter a familar name: \n")
    
    if familar_name.isalpha() == True:
        print("Hi", familar_name, ", glad you could make it!")
        break
        
    else:
        print("Input has to be one word - no spaces\n")

# Module 4.2
# [ ] create and test pre_word()

def pre_word(word):
    if word.isalpha():
        if word.startswith('pre'):
            print("Valid \"pre\" word")
        else:
            print("Not a \"pre\" word")
    else:
        print("This is not a word")
    
testword = input("enter a word that starts with \"pre\": ").lower()
pre_word(testword)                 