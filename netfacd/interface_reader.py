#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:    # This is a new line, you also need to indent the code below this line by 4 whitespaces
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

# customization request 1
def ipaddr(adaptname):
    print("ip address ", end="")
    print((netifaces.ifaddresses(adaptname)[netifaces.AF_INET])[0]['addr']) # Prints the IP address

def macaddr(adaptname):
    print("mac address ", end="")  
    print((netifaces.ifaddresses(adaptname)[netifaces.AF_LINK])[0]['addr']) # Prints the IP address

adaptername = input("What adapter name are you looking for?")
ipaddr(adaptername)
macaddr(adaptername) 
