def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

try:
    price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount)

    if discount >= 20:
        print(f"Final price after {discount}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numbers only.")
