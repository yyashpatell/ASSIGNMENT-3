print("\n------------------WELCOME TO OUR CLOTHING SHOP--------------------")
shirt_price = 25.99
short_price = 19.99
print("\nhere are two items you wanted to purchase")
print("Shirt which will cost: 25.99")
print("Short which will cost: 19.99")

class Shirts():
    def __init__(self,shirt_type, shirt_color, num_shirts):
        self.shirt_type = shirt_type
        self.shirt_color = shirt_color
        self.num_shirts = num_shirts

    shirt_type = int(input("\nDo you want a Polo-Shirt or T-shirt(For Polo-Shirt enter 1 and for T-Shirt enter 2: "))
    if shirt_type == 1:
       shirt_selected_1 = "Polo-Shirt"
       print("The type of shirt you selected is", shirt_selected_1)
       
    elif shirt_type == 2:
       shirt_selected_2 = "T-Shirt"
       print("The type of shirt you selected is ", shirt_selected_2)
    
    else:
       print("Incorrect number")
    
    shirt_color = input("\nEnter the color of shirt: ")
    print("The color of your shirts are: ", shirt_color)
    

class Shorts():
    def __init__(self,short_type, short_color, num_shorts):
        self.short_type = short_type
        self.short_color = short_color
        self.num_shorts = num_shorts 
        
    short_type = int(input("\nDo you want Jeans or Cotton shorts (For Jeans shorts enter 3 and for Cotton shorts enter 4: "))
    if short_type == 3:
        short_selected_1 = "Jeans"
        print("The type of short you selected is ", short_selected_1)

    elif short_type == 4:
        short_selected_2 = "Cotton"
        print("The type of short you selected is ", short_selected_2)

    else:
        print("Incorrect input")

    short_color = input("\nEnter the color of short: ")
    print("The color of your shorts is: ", short_color)

class Calculate():
    def calcDiscount(self, num_shirts, num_shorts, total, discount, s_discount):
        self.num_shirts = num_shirts
        self.num_shorts = num_shorts
        self.discount = discount
        self.s_discount = s_discount
        self.total = total

    num_shirts = int(input("\nNumber of shirts: "))
    num_shorts = int(input("Number of shorts: "))
    print("\nThe total number of shirts you selected are: ", num_shirts)
    print("The total number of shorts you selected are: ", num_shorts)

    total = (shirt_price * num_shirts) + (short_price * num_shorts)
    print("\nprice of your order is: ", total)

    if num_shirts >= 3 or num_shorts >= 3:
        discount_1 = total*(15/100)
        final_discount = total - discount_1
        print("you got quantity discount of 15 percent on your order, discounted price is: ", final_discount)
    else:
        print("no quantity discount applicable on your order, your total remains the same: ", total)

    s_discount = int(input("\nif you are a student or senior citizen type 1 (get 10% DISCOUNT!!), else type 0: "))
    if s_discount == 1:
        discount_2 = total*(10/100)
        f_discount = total - discount_2
        print("\nyour price after adding discount(student or senior citizen) is: ", f_discount)
    elif s_discount ==0:
       print("sorry you are not eligible for student or senior citizen discount")
    if num_shirts >= 3 or num_shorts >= 3 and s_discount == 1:
        d_total = total - (discount_1 + total*(10/100))
        print("\nprice of your order after deducting all discounts: ", d_total)
    else:
        print("\nyour total is: ", total - (discount_1 + total*(10/100)))
    
    def calcTotal(self, tax, total_1, total_2, total_3, total_4):
        self.tax = tax
        self.total_1 = total_1
        self.total_2 = total_2
        self.total_3 = total_3
        self.total_4 = total_4

    tax = 0.13 * total
    total_1 = tax + final_discount 
    total_2 = tax + f_discount
    total_3 = tax + d_total
    total_4 = tax + total

    print("\ntax here added would be 13% to your order")

    if num_shirts >= 3 or num_shorts >= 3 and s_discount ==1:
        print("\nCOST of your order after adding all discounts and tax is: ", total_3)
    elif num_shirts >= 3 or num_shorts >= 3:
        print("\nTOTAL COST of your order after adding all discounts and tax is: ", total_1)
    elif s_discount == 1:
        print("\nTOTAL COST of your order after adding all discounts and tax is: ", total_2)

    







    

        






        


