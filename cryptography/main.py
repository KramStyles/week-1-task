from art import art


def cryptography():
    print(art)
    print("Hello. Welcome to the Crypt Program")
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    repeat = 'Yes'
    while repeat:
      msg = ''
      choice = input("Input 1 if you want to encrypt and 0 if you want to decrypt: ")
      if choice == '0':
        word = input('Enter word to be decoded: ')
        level = int(input('Enter the key: '))
        for x in word:
          if x in lowers:
            indx = lowers.index(x) - level
            if indx < 0:
              indx += len(lowers)
            msg += lowers[indx]
          else:
            msg += x
      elif choice == '1':
        word = input('Enter word to be encoded: ')
        level = int(input('Enter the key: '))
        for x in word:
          if x in lowers:
            indx = lowers.index(x) + level
            if indx > len(lowers):
              indx -= len(lowers)
            msg += lowers[indx]
          else:
            msg += x
      else:
        msg = 'Please, make a valid choice'
      print(msg)
      repeat = input('Do you want to use our crypt service again? ')
      if repeat.title() == 'No':
        print('Thank you for testing our product. We hope to see you soon!')
        break;



    return msg


cryptography()
