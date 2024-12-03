from cs50 import get_int


def card_type(card):

    card = str(card)

    if (card[0] == '4' and (len(card) == 13 or len(card) == 16)):
        print("VISA\n")
    elif (card[:2] == '34' or card[:2] == '37' and len(card) == 15):
        print("AMEX\n")
    elif (int(card[:2]) >= 51 and int(card[:2]) <= 55 and len(card) == 16):
        print("MASTERCARD\n")
    else:
        print("INVALID\n")


def check_sum(card):

    card = str(card)

    sum_p = 0
    sum_o = 0

    card_copy = card[::-1]

    for i in card_copy[1:len(card_copy):2]:
        digit = int(i) * 2
        if digit >= 10:
            digit1 = str(digit)
            digit = int(digit1[0]) + int(digit1[1])
        sum_p += digit

    for i in card_copy[0:len(card_copy):2]:
        sum_o += int(i)

    sum = sum_p + sum_o

    if (str(sum)[-1] == '0'):
        return True
    else:
        return False


def main():

    credit_card = get_int("Credit Card Number: ")

    if (check_sum(credit_card) == True):
        card_type(credit_card)
    else:
        print("INVALID")


main()
