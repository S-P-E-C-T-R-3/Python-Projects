print("Welcome To tip Calculator")
bill=float(input("What Was the total bill:$"))
tip=int(input("What % tip you would like to give? 10, 12 or 15 "))
num_persons=int(input("How many people to split the bill:"))
tipamt=0
"""if tip==10:
    tipamt=totalbill*0.01
    totalbill +=tipamt
elif tip == 12:
    tipamt=totalbill*0.12
    totalbill +=tipamt
elif tip == 15:
    tipamt=totalbill*0.15
    totalbill +=tipamt """
tip_in_percent=tip/100
bill_after_tip=bill*tip_in_percent
totalbill=bill+bill_after_tip
split=totalbill/num_persons
finalamt=round(split, 2)
finalamt = "{:.2f}".format(finalamt)
print(f"Each should pay ${finalamt}")

