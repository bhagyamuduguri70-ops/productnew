def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result


if __name__ == "__main__":
    # Example usage
    print(product_details("P101", "Keyboard", 10, 450))
