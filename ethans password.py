import time                                                                            
def x():
    
    print("*************************")
    print("ENTER ETHANS PASSWORD")
    print("*************************")


    password=input("")
    if password=="Josh2003123":
        f = open("welcome.txt", "r")
        print(f.read())
        time.sleep(2)
        print("Hi")
        time.sleep(1)
        print("ethan")
        time.sleep(1)
        print ("cort")
        time.sleep(1)
        answer=input("Do you have airpods? ")
        if answer=="yes":
            time.sleep(1)
            print("not broke")
        if answer=="no":
            time.sleep(1)
            print("broke")
            time.sleep(1)
        input("Press enter to log out")
        x()
    else:
        print("You are Not ethan cort")
        x()



x()


                                                                
