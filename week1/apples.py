applePrice = .50
userPrompt = "Please enter your name: "
applePrompt = "How many apples would you like to buy?: "
thankYou = "Thank you for your purchase."
username = input(userPrompt)
print(username)

applePurchase = input(applePrompt)
print(f"Thank you {username} for your purchase of {applePurchase} Apples at {(applePrice):,.2f} each.")