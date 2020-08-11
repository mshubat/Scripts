
class Ceasar:

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


    @classmethod
    def shift(cls, char, amount):
        if char.lower() in cls.alphabet:
            new_index = (cls.alphabet.index(char.lower()) + amount) % 26
            return cls.alphabet[new_index]
        else:
            return char

    @classmethod
    def encrypt(cls, message, amount):
        encrypted = ''
        for letter in message:
            new_letter = cls.shift(letter, amount)
            encrypted += new_letter
        return encrypted


if __name__ == "__main__":
    message = ''

    print('\nThis is a Ceasar cipher program.')
    print('Type "quit" or "exit" to end\n')
    while(True):
        message = input('Enter the message to be encrypted: ')
        if (message == 'quit' or message == 'exit'):
            break
        amount = int(input("Enter the shift amount: "))


        encrypted = Ceasar.encrypt(message, amount)
        print(encrypted)