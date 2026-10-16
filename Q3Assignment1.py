
amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").lower()

if amount < 0 or amount > 100000:
    print("Invalid order amount")
    print("Eligibility: Invalid")
else:
    if amount >= 5000:
        discount_percent = 15
    elif amount >= 2000 and membership == "yes":
        discount_percent = 10
    else:
        discount_percent = 0

    discount = amount * discount_percent / 100
    final_amount = amount - discount

    print("Original amount: ₹", amount)
    print("Discount percentage:", discount_percent, "%")
    print("Discount amount: ₹", discount)
    print("Final payable amount: ₹", final_amount)

    if discount_percent > 0:
        print("Eligibility: Eligible for discount")
    else:
        print("Eligibility: No discount")
