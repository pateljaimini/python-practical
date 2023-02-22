binary_value = int(input('enter your binary number:-'))
decimal = 0
counter = 0
start=0
while (binary_value != 0):
       digit = binary_value %10
       decimal = decimal + digit*(2**start)
       binary_value = binary_value//10
       counter = counter + 1
       start=start+1

print('decimal number is',decimal)
