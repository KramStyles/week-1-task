from art import art


def cryptography():
    print(art)
    print("Hello. Welcome to the Crypt Program")
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    repeat = 'Yes'
    try:
        while repeat:
            msg = ''
            choice = input("Input 1 if you want to encrypt and 0 if you want to decrypt: ")
            if choice == '0':
                word = input('Enter ciphertext to be decoded: ')
                level = int(input('Enter the key: '))
                if level > len(lowers):
                    level %= len(lowers)
                for x in word:
                    if x in lowers:
                        indx = lowers.index(x) - level
                        if indx < 0:
                            indx += len(lowers)
                        if indx == 26:
                            indx = 0
                        msg += lowers[indx]
                    else:
                        msg += x
            elif choice == '1':
                word = input('Enter plaintext to be encoded: ')
                level = int(input('Enter the key: '))
                if level > len(lowers):
                    level %= len(lowers)
                for x in word:
                    if x in lowers:
                        indx = lowers.index(x) + level
                        if indx > len(lowers):
                            indx -= len(lowers)
                        if indx == 26:
                            indx = 0
                        msg += lowers[indx]
                    else:
                        msg += x
            else:
                msg = 'Please, make a valid choice'
            print(msg)
            repeat = input('Do you want to use our crypt service again? ')
            if repeat.title() == 'No':
                print('Thank you for testing our product. We hope to see you soon!')
                break
    except Exception as err:
        print("An Error occurred:", err)


cryptography()
