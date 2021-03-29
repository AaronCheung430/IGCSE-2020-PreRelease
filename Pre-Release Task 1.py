#Created by Aaron Cheung from Barnard Castle School
#Last editied on 2020/03/31 17:09 HKT
#Copyright © 2020 Aaron Cheung. All rights reserved.
#Pre-release Task 1 v1.0

#Using Arrays to store item code, description, price information for phones, tablets, SIM cards, cases and chargers
PT_ItemCode = ["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL"]
SIM_ItemCode = ["SMNO", "SMPG"]
Case_ItemCode = ["CSST", "CSLX"]
Charger_ItemCode = ["CGCR", "CGHM", "CGCR & CGHM"]
#Description for all phones, tablets, SIM cards, cases and chargers
PT_Description = ["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64 GB memory", "RoboPhone – 6-inch screen and 256 GB memory", "Y-Phone Standard – 6-inch screen and 64 GB memory", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "RoboTab – 8-inch screen and 64 GB memory", "RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", "Y-Tab Deluxe – 10-inch screen and 256 GB memory"]
SIM_Description = ["SIM Free (no SIM card purchased)", "Pay As You Go (SIM card purchased)"]
Case_Description = ["Standard Case", "Luxury Case"]
Charger_Description = ["Car Charger", "Home Charger", "Both Car Charger and Home Charger"]
#Price for all phones, tablets, SIM cards, cases and chargers
PT_Price = [29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99]
SIM_Price = [0.00, 9.99]
Case_Price = [0.00, 50.00]
Charger_Price = [19.99, 15.99, 35.98]
#This array is for the items that the customer have chosen
Choice_ItemCode = []
Choice_Description = []
Choice_Price = []

#Set customer total
OrderTotal = 0

#Asking do the customer want a phone or tablet or not
print("Welcome to the shop...")
print("where you can find a range of newest mobile devices, SIM cars and accessories.")
print("\n")
print("Do you want to order a phone or a tablet?")
PT_ans = input("Y/N: ")

#Checking the customer  input is it a yes or not
if PT_ans == "Y" or PT_ans == "Yes" or PT_ans == "yes" or PT_ans == "y" or PT_ans == "YES":
    print("Great to know that. Here is the list of phones or tablets that you can choose from.")

    #Using while true to keep letting the customer choose the phone or tablet
    while True:
        #Print the phone and tablet menu for the customer to choose
        for i in range(0,10):
            print([i+1], PT_ItemCode[i], PT_Description[i] + " $"+ str(PT_Price[i]))

        #Asking the customer which item the customer wants and print the item price and the item description that the customer has chosen 
        try:
            PT_Choice = int(input("Please type the number of the item you want: "))

            #To prevent the program using a reverse string which will get the element in reverse order of the array
            if PT_Choice <= 0:
                print(".")
                print("Oops! That was no valid number. Try again...")
            else:
                PT_Choice_Index = PT_Choice - 1
                
                PT_Choice_Description = PT_Description[PT_Choice_Index]
                PT_Choice_Price = PT_Price[PT_Choice_Index]
                
                Choice_Description.append(PT_Choice_Description)
                Choice_Price.append(PT_Choice_Price)
                Choice_ItemCode.append(PT_ItemCode[PT_Choice_Index])
                
                OrderTotal = OrderTotal + PT_Choice_Price
                print("You have chosen: " + PT_Choice_Description + ", and the total: $" + str(round(OrderTotal,2)) + ".")

                #While true is an infinite loop, by using break, it will break the loop when the customer has chosen the phone or tablet
                break
        
        #Prevent invalid input, in order to prevent the program stopped
        except IndexError:
            print("\n")
            print("Oops! That was no valid number. Try again...")
        except ValueError:
            print("\n")
            print("Oops! That was a text. Please try again with a valid number...")

    #Checking is the customer choosing a phone and ask what SIM does the customer wants if the customer has chosen a phone
    if 0 <= PT_Choice_Index <= 5:
        print("\n")
        print("Which SIM card do you want for your phone?")
        
        while True:
            #Print the SIM card menu for the customer to choose
            for i in range(0,2):
                print([i+1], SIM_ItemCode[i], SIM_Description[i] + " $" + str(SIM_Price[i]))

            try:
                SIM_Choice = int(input("Please type the number of the item you want: "))
                if SIM_Choice == 1:
                    print("So you don't need a SIM card for your phone.")
                    SIM_Choice_Index = SIM_Choice - 1
                    
                    SIM_Choice_Description = SIM_Description[SIM_Choice_Index]
                    SIM_Choice_Price = SIM_Price[SIM_Choice_Index]
                
                    Choice_Description.append(SIM_Choice_Description)
                    Choice_Price.append(SIM_Choice_Price)
                    Choice_ItemCode.append(SIM_ItemCode[SIM_Choice_Index])

                    OrderTotal = OrderTotal + SIM_Choice_Price
                    print("The Total is $" + str(round(OrderTotal,2)))
                    break
                elif SIM_Choice == 2:
                    print("So you would like to have a Pay As You Go.")
                    SIM_Choice_Index = SIM_Choice - 1
                    
                    SIM_Choice_Description = SIM_Description[SIM_Choice_Index]
                    SIM_Choice_Price = SIM_Price[SIM_Choice_Index]
                
                    Choice_Description.append(SIM_Choice_Description)
                    Choice_Price.append(SIM_Choice_Price)
                    Choice_ItemCode.append(SIM_ItemCode[SIM_Choice_Index])

                    OrderTotal = OrderTotal + SIM_Choice_Price
                    print("The Total is $" + str(round(OrderTotal,2)))
                    break
                else:
                    print("\n")
                    print("Oops! That was no valid number. Try again...")

            #Prevent invalid input, in order to prevent the program stopped        
            except ValueError:
                print("\n")
                print("Oops! That was a text. Please try again with a valid number...")
    else:
        print("You have chosen a tablet, so you won't need a SIM card")
    
else:
    print("No problem at all!")
    print("The Total is $" + str(round(OrderTotal,2)))

print("\n")
print("Do you want to order a case?")
Case_ans = input("Y/N: ")

if Case_ans == "Y" or Case_ans == "Yes" or Case_ans == "yes" or Case_ans == "y" or Case_ans == "YES":
    print("Great to know that. Here is the list of cases that you can choose from.")

    while True:
        #Print case menu
        for i in range(0,2):
            print([i+1], Case_ItemCode[i], Case_Description[i] + " $" + str(Case_Price[i]))

        #Prevent invaild input, in order to stop the program
        try:
            Case_Choice = int(input("Please type the number of the item you want: "))

            if Case_Choice <= 0:
                print(".")
                print("Oops! That was no valid number. Try again...")
            else:
                Case_Choice_Index = Case_Choice - 1
                
                Case_Choice_Description = Case_Description[Case_Choice_Index]
                Case_Choice_Price = Case_Price[Case_Choice_Index]
                
                Choice_Description.append(Case_Choice_Description)
                Choice_Price.append(Case_Choice_Price)
                Choice_ItemCode.append(Case_ItemCode[Case_Choice_Index])
                
                OrderTotal = OrderTotal + Case_Choice_Price
                
                print("You have chosen: " + Case_Choice_Description + ", and the total: $" + str(round(OrderTotal,2)) + ".")
                break
        
        except IndexError: 
            print("\n")
            print("Oops! That was no valid number. Try again...")
        except ValueError:
            print("\n")
            print("Oops! That was a text. Please try again with a valid number...")

else:
    print("No problem at all!")
    print("The Total is $" + str(round(OrderTotal,2)))

print("\n")
print("Do you want to order any chargers?")
Charger_ans = input("Y/N: ")

if Charger_ans == "Y" or Charger_ans == "Yes" or Charger_ans == "yes" or Charger_ans == "y" or Charger_ans == "YES":
    print("Great to know that. Here is the list of chargers that you can choose from.")

    while True:
        #Print case menu
        for i in range(0,3):
            print([i+1], Charger_ItemCode[i], Charger_Description[i] + " $" + str(Charger_Price[i]))

        #Prevent invaild input, in order to stop the program
        try:
            Charger_Choice = int(input("Please type the number of the item you want: "))
            
            if Charger_Choice <= 0:
                print(".")
                print("Oops! That was no valid number. Try again...")
            else:
                Charger_Choice_Index = Charger_Choice - 1
                
                Charger_Choice_Description = Charger_Description[Charger_Choice_Index]
                Charger_Choice_Price = Charger_Price[Charger_Choice_Index]
                
                Choice_Description.append(Charger_Choice_Description)
                Choice_Price.append(Charger_Choice_Price)
                Choice_ItemCode.append(Charger_ItemCode[Charger_Choice_Index])
                
                OrderTotal = OrderTotal + Charger_Choice_Price
                
                print("You have chosen: " + Charger_Choice_Description + ", and the total: $" + str(round(OrderTotal,2)) + ".")
                break
        
        except IndexError: 
            print("\n")
            print("Oops! That was no valid number. Try again...")
        except ValueError:
            print("\n")
            print("Oops! That was a text. Please try again with a valid number...")

else:
    print("No problem at all!")
    print("The Total is $" + str(round(OrderTotal,2)))


#Print the reciept for the customer
print("\n")
print("===========================")
print("ORDER SUMMARY\n")

NumberOfItems = len(Choice_Description)
if NumberOfItems == 0:
    Empty = "NOTHING"
else:
    Empty = ""
for i in range(0,NumberOfItems):
    print(" - ", Choice_Description[i] + " $"+ str(Choice_Price[i]))

print("\n")
print("You want to buy " + str(NumberOfItems) +" item(s) and the total is $" + str(round(OrderTotal,2)))
print("===========================")
print("\n")
print("FOR INTERNAL USE:")
for i in range(0,NumberOfItems):
    print(" - ", Choice_ItemCode[i], Choice_Description[i])
