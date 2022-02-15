from art import art


def cryptography():
    print(art)
    print("Hello. Welcome to the Crypt Program")
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    repeat = 'Yes'
    try:
        while repeat:
            msg = ''
            choice = input("\nType 1 if you want to encrypt. \nType 0 if you want to decrypt: ")
            if choice == '0':
                word = input('\nEnter ciphertext to be decoded: ')
                bad_level = True
                while bad_level:
                    try:
                        level = int(input('\nEnter the key: '))
                    except Exception as err:
                        print("Please input a valid integer", err)
                    else:
                        bad_level = False

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
                word = input('\nEnter plaintext to be encoded: ')
                bad_level = True
                while bad_level:
                    try:
                        level = int(input('\nEnter the key: '))
                    except Exception as err:
                        print("\nPlease input a valid integer", err)
                    else:
                        bad_level = False
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
                msg = '\nPlease, make a valid choice. Type 1 or 0'
            print(msg)
            repeat = input('\nDo you want to use our crypt service again? Yes | No: ')
            if repeat.title() == 'No':
                print('\nThank you for testing our product. We hope to see you soon!')
                break
    except Exception as err:
        print("An Error occurred:", err)


cryptography()
