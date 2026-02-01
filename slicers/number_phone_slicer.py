number_phone = input('Enter your morocain number phone : ')

contrie = number_phone[:number_phone.index("6")+1]
nbr_phone = number_phone[number_phone.index("6")+1:]


print('contrie ; ', contrie)
print('your number phone : ', nbr_phone)
