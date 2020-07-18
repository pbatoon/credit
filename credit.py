import math

# Card Validation function
def card_validation(card_number):
    card_type = ""                                                      # initialize card_type and valid variables
    valid = False

    num_digits = int(math.log10(card_number)+1)                         # fetch num of digits in card_number

    if num_digits != 13 and num_digits != 15 and num_digits != 16:      # if num of digits isn't valid, then set card_type to invalid
        card_type = "INVALID\n"

    str_cardnum = str(card_number)[::-1]                                # convert card_number to string and reverse it
    index1_cardnum = str_cardnum[1:]                                    # start reversed string at index 1
    every_other = index1_cardnum[::2]                                   # get every other digit in card number
    digits = list(map(int,every_other))                                 # convert digits to int and and to array

    n2_digits = [i * 2 for i in digits]                                 # multiply every digit by 2
    n2_sum = 0
    n = 0

    for i in range(len(n2_digits)):                                     # if digits[i] has 2 digits then split digits into two different elements
        if n2_digits[i] / 10 >= 1 and digits[i] != 0:
            last_digit = n2_digits[i] % 10
            n2_digits[i] = n2_digits[i] // 10
            n2_digits.append(last_digit)

    n2_sum = sum(n2_digits)                                             # get sum of digits

    n1_str = str_cardnum[::2]                                           # now get digits that weren't used and add to array
    n1_digits = list(map(int,n1_str))
    n1_sum = sum(n1_digits)                                             # get sum of n1 digits

    n1_n2 = n1_sum + n2_sum                                             # get sum of n1 and n2

    if n1_n2 % 10 == 0:                                                 # if n1_n2 ends in 0 then the card is valid
        valid = True
    else:
        card_type = "INVALID\n"

    card_num = str(card_number)

    if valid:                                                           # find card_type according to first two digits in card_number
        if card_num[0:2] == "34" or card_num[0:2] == "37":
            card_type = "AMEX\n"
        elif card_num[0:2] == "51" or card_num[0:2] == "52" or card_num[0:2] == "53" or card_num[0:2] == "54" or card_num[0:2] == "55":
            card_type = "MASTERCARD\n"
        elif card_num[0] == "4":
            card_type = "VISA\n"
        else:
            card_type = "INVALID\n"

    return card_type

card_number = 0
while card_number <= 0:
    card_number = int(input("What's your credit card number? "))

print(card_validation(card_number))




