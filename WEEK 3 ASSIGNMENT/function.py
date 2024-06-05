def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount if the discount percentage is 20% or higher.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after applying the discount or the original price if the discount is less than 20%
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and the discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values for the price and discount percentage.")
