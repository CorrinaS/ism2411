# Self-Assessment Questions:
# 1.) There were 3 different bugs. I spotted a missing colon at the end of the for loop, 
# it showed a syntaxerror and showed which line was wrong. 
# I used ChatGBT to help me understand what it meant before fixing it. 

# 2.) The apply_discount function takes a price and customer tier as input.
# The tier is gold, silver, bronze, or none. The function applies the right discount depending
# on the function. It also applies the correct discount to the original price and returns
# final price. A colleague could use the function without reading the body as long as they know
# what values to enter for price and tier. 

# 3.) AI Disclosure, I used ChatGBT to help me understand the Why behind the error rather
# than telling me the answer in exercise 5. It helped me build an understanding. 
# I made corrections based on the explanation and ran the program to see if they worked.
# I found and understand the Syntax errors, index error, and logic error. 


# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate 

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") #7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") #20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") #7.50


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze": 
        return price * 0.95
    else:
        return price

# calling the function 

price = 200
tiers = ["gold", "siilver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

    # --- Exercise 3 ---

    # Write it out manually first, then refactor into a function

    discounted = apply_discount(200, "gold")
    tax = calculate_tax(discounted, 0.07)
    after_tax = discounted + tax
    print(f"After gold discount: ${discounted:.2f}")
    print(f"After Tax: ${after_tax:.2f}")

    # Refactor into a function

    def final_price(price, tier, tax_rate):
        discounted = apply_discount(price, tier)
        tax = calculate_tax(discounted, tax_rate)
        return discounted + tax 

    print(f"FInal price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders: 
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")


# --- Exercise 6 --- 

x = 100    # apple.  # Global

def double_it():
#    x = 999    # local another apple (not the same apple as above) 
    return x * 2

print(x)
print(double_it())
print(x)



