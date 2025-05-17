# Constant part of the sentence
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    final_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"

    print("\n" + final_sentence)

if __name__ == '__main__':
    main()
