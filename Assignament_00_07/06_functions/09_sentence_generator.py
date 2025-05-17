def genrate_sentence(user_word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("I am excited to add this " + user_word + " to my vast collection of them!") 
    elif part_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + user_word + "!")
    elif part_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + user_word + "!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    user_word : str = input("Please type a noun, verb, or adjective: ")  
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    genrate_sentence(part_of_speech)

if __name__ == '__main__':
    main()