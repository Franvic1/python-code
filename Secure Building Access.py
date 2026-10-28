card_valid = True
pin_correct = False 
if card_valid == True:
    print("access card accepted")
    if pin_correct:
        print("access granted")
    else :
        print ("Incorrect PIN")
else:
    print ("invalid access card")