# IP CLass Address Checker - Teaching Exercise Script throughout Section 7.

import sys

def user_prompt():
    global user_ip_address_input
    user_ip_address_input = input("Enter IP Address: ")

user_prompt()

count = 0

while user_ip_address_input != "exit":

    
    divide_ip_address = user_ip_address_input.split(".")

    if len(divide_ip_address) != 4:
        print("Invalid IP Address Supplied")
        sys.exit()

    convert_ip_address = list(map(int, divide_ip_address))

    for i in convert_ip_address:
        if i > 255:
            print("All octets must be a value of 255 or less.")
            sys.exit()

    first_octet = convert_ip_address[0]


    if first_octet >= 1 and first_octet <= 126:
        print(user_ip_address_input + " is a Class A")

    elif first_octet >= 128 and first_octet <= 191:
        print(user_ip_address_input + " is a Class B")

    elif first_octet >= 192 and first_octet <= 223:
        print(user_ip_address_input + " is a Class C")

    elif first_octet >= 224 and first_octet < 239:
        print(user_ip_address_input + " is a Class D")

    elif first_octet >= 240 and first_octet < 254:
        print(user_ip_address_input + " is a Class E")

    else:
        print("Invalid IP Address Supplied")
        sys.exit()

    user_prompt()
    count += 1


print("Total number of IP address entered was " + str(count))



