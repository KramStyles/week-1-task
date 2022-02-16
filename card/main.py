
def validate_card():
    """
    The Validate_Card Function take a credit card number and determine whether that number is an
    American Express Credit Card number or Master Card number or Visa or something else. 
    The card number is provided as a string input and it has to satisfy a checksum or Luhn Algorithm
    to be a valid credit card number.

    return: AMEX | MASTERCARD | VISA | INVALID - Depending on the result of the validation 
    """
    print("Hello and Welcome")
    card = input("Please enter your Card Number: ").strip()
    msg = "heyy"
    try:
        card_length = len(card)
        if card_length == 15:
            msg = "amex"
        elif card_length == 16 and str(card)[0:2] in ['51', '52', '53', '54', '55']:
            msg = "MasterCard"
        elif (card_length == 13 or len(card) == 16) and card[0] == '4':
            msg = "Visa"
        else:
            return "INVALID"

        products = [card[x] for x in range(len(card) - 2, -1, -2)]
        dbl_products = [int(x) * 2 for x in products]
        sum_products = 0

        sum_others = sum([int(card[x]) for x in range(card_length - 1, -1, -2)])

        for x in dbl_products:
            if len(str(x)) > 1:
                double = sum([int(x) for x in str(x)])
                sum_products += double
            else:
                sum_products += x

        sum_total = sum_products + sum_others
        if sum_total % 10:
            msg = "Invalid"
    except [ValueError, TypeError, ArithmeticError] as err:
        msg = "Please ensure only numbers were inputted"
    except Exception as err:
        msg = f"An Exception Occurred: {err}"
    
    return msg.upper()


