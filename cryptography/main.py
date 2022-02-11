from art import art


def cryptography():
  print(art)
  print("Hello. Welcome to the Crypt Program")
  choice = input("Input 1 if you want to encrypt and 0 if you want to decrypt: ")
  if choice != '1' or choice != '0':
    print('Please, make a valid choice')
  elif choice == '1':
    pass
  else:
    word = 'baby'
    level = 5
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in word:
      if x in lowers:
        indx = lowers.index(x) + level
        if indx > len(lowers):
          indx -= len(lowers)
        print(lowers[indx])



cryptography()
