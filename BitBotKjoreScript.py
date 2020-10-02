from microbit import *
from time import sleep

# Farten kan være 0 til 1023
fart = 700 

def fram():
    #Kjør høyre motor fram
    pin14.write_analog(fart)
    pin12.write_analog(0)
    #Kjør venstre motor fram
    pin16.write_analog(fart)
    pin8.write_analog(0)

def bak():
    #Kjør høyre motor bak
    pin14.write_analog(0)
    pin12.write_analog(fart)
    #Kjør venstre motor bak
    pin16.write_analog(0)
    pin8.write_analog(fart)
    
def sving_venstre():
    #Kjør høyre motor fram
    pin14.write_analog(fart)
    pin12.write_analog(0)
    #Kjør venstre motor bak
    pin16.write_analog(0)
    pin8.write_analog(fart)
    
def sving_hoyre():
    #Kjør høyre motor bak
    pin14.write_analog(0)
    pin12.write_analog(fart)
    #Kjør venstre motor fram
    pin16.write_analog(fart)
    pin8.write_analog(0)

def stopp():
    #Kjør høyre motor bak
    pin14.write_analog(0)
    pin12.write_analog(0)
    #Kjør venstre motor fram
    pin16.write_analog(0)
    pin8.write_analog(0)


# Her skriver du algoritmen din
fram()
sleep(2)
sving_hoyre()
sleep(0.5)
bak()
sleep(2)
sving_venstre()
sleep(0.5)
stopp()
