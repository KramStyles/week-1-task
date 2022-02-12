american = [375987654321001, 379996620002002, 377107234567890]
american2 = [378282246310005, 371449635398431, 378734493671000]
master = [5555555555554444, 5105105105105100]
visa = [4111111111111111, 4012888888881881, 4222222222222]


def validate_card(card):
    msg = ""
    if len(str(card)) == 15:
        msg = "American Express"
    elif len(str(card)) == 16 and str(card)[0:2] in ['51', '52', '53', '54', '55']:
        msg = "Master Card"
    elif (len(str(card)) == 13 or len(str(card)) == 16) and str(card)[0] == '4':
        msg = "Visa Card"
    else:
        msg = "Card not identified"
    print(msg)
