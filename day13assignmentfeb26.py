print("**welcome to 5 tirties packages**")
def agra():
    print("agra package is 10k per person")
    var=input("do you want to book this package: ")
    if var == "yes":
        per_person=10000
        fullname=input("enter your fullname: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        address=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+15
        total_amount=gst_amount*number_of_persons
        print(f"hi {fullname} you're booked goa total amount is:",{total_amount})
        print("thank you sir")
    else:
        print("thank you sir")

def arunachalam():
    print("arunachalam package is 5k per person")
    var=input("do you want to book this packaage: ")
    if var == "yes":
        per_person=5000
        fullname=input("enter yourfullname: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        address=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+10
        total_amount=gst_amount*number_of_persons
        print(f"hi{fullname} your ticket is conformed total price is :",{total_amount})
        print("thank you sir")

    else :
        print("thank you")

def ayodhya():
    print("ayodhya package is 10k per person ")
    var=input("do you want to book this package: ")
    if var == "yes":
        per_person=10000
        fullname=input("enter your fullnmae: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        address=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+20
        total_amount=gst_amount*number_of_persons
        print(f"hi{fullname} your ticket is conformed total price is: ",{total_amount})
        print("thank you sir")

    else:
        print("thank you sir")
def thiruvananthapuram():
    print("thiruvananthapuram package is 10k per person ")
    var=input("do you want to book this package: ")
    if var == "yes":
        per_person=10000
        fullname=input("enter you fullname: ")
        age=int(input("enter your age: "))
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        address=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: "))
        number_of_persons=int(input("enter the number of persons: "))
        gst_amount=per_person+10
        total_amount=gst_amount*number_of_persons
        print(f"hi{fullname} your ticket is conformed total price is: ",{total_amount})
        print("thank you sir")
    else:
        print("thank you sir")  

def kerala():
    print("kerala package is 10k per person") 
    var=input("do you want to book this package: ") 
    if var == "yes":
        per_person=10000
        fullname=input("enter you fullname: ")
        age=int(input("enter your age: ")) 
        phone_number=int(input("enter your phone_number: "))
        emai_id=input("enter your email_id: ")
        address=int(input("enter your address: "))
        number_of_persons=int(input("enter the number of persons: ")) 
        gst_amount=per_person+10 
        total_amount=gst_amount*number_of_persons 
        print(f"hi{fullname} your ticket is conformed total price is: ",{total_amount})
        print("thank you sir")
    else:
        print("thank you sir")        

def main():
    print("***welcome harsha travels***")
    print("1.agra")
    print("2.arunachalam")
    print("3.ayodhya")
    print("4.thiruvananthapuram")
    print("5.kerala")
    choose_number= int(input("enter your choice: "))
    if choose_number == 1:
        agra()
    elif choose_number == 2:
        arunachalam()
    elif choose_number == 3:
        ayodhya()
    elif choose_number == 4:
        thiruvananthapuram()
    elif choose_number == 5:
        kerala()       

    else:
        print("invalid choice")

main()
                                

                
                
                
            
            
        
        
        
                
             