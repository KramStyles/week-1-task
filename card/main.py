american = [375987654321001, 379996620002002, 377107234567890]
american2 = [378282246310005, 371449635398431, 378734493671000]
master = [5555555555554444, 5105105105105100]
visa = [4111111111111111, 4012888888881881, 4222222222222, 4003600000000014]


def validate_card(card):
    msg = ""
    card_length = len(str(card))
    if card_length == 15:
        card = "American Express"
    elif card_length == 16 and str(card)[0:2] in ['51', '52', '53', '54', '55']:
        card = "Master Card"
    elif (card_length == 13 or len(str(card)) == 16) and str(card)[0] == '4':
        card = "Visa Card"
    else:
        return "Card not identified"

    chosen = [str(card)[x] for x in range(len(str(card)) - 2, -1, -2)]
    dbl_chosen = [int(x) * 2 for x in chosen]
    sum_of = 0

    for x in dbl_chosen:
        if len(str(x)) > 1:
            double = sum([int(x) for x in str(x)])
            sum_of += double
        else:
            sum_of += x

    msg = sum_of
    print(msg)


validate_card(visa[2])