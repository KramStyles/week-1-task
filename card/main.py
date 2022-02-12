american = [375987654321001, 379996620002002, 377107234567890]
american2 = [378282246310005, 371449635398431, 378734493671000]
master = [5555555555554444, 5105105105105100]
visa = [4111111111111111, 4012888888881881, 4222222222222, 4003600000000014]


def validate_card(card):
    msg = ""
    card_length = len(str(card))
    if card_length == 15:
        msg = "American Express"
    elif card_length == 16 and str(card)[0:2] in ['51', '52', '53', '54', '55']:
        msg = "Master Card"
    elif (card_length == 13 or len(str(card)) == 16) and str(card)[0] == '4':
        msg = "Visa Card"
    else:
        return "Card not identified"

    products = [str(card)[x] for x in range(len(str(card)) - 2, -1, -2)]
    dbl_products = [int(x) * 2 for x in products]
    sum_products = 0

    sum_others = sum([int(str(card)[x]) for x in range(card_length - 1, -1, -2)])

    for x in dbl_products:
        if len(str(x)) > 1:
            double = sum([int(x) for x in str(x)])
            sum_products += double
        else:
            sum_products += x

    sum_total = sum_products + sum_others
    if sum_total % 10:
        msg += f" {card} is Invalid"
    else:
        msg += f" {card} is Valid"

    return msg


cards = american + american2 + master + visa
for card in cards:
    print(validate_card(card))