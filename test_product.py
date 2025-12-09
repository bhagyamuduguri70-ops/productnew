from product import product_details

def test_product_details():
    expected_output = (
        "Product ID: P101\n"
        "Name: Keyboard\n"
        "Quantity: 10\n"
        "Price: 450"
    )

    assert product_details("P101", "Keyboard", 10, 450) == expected_output
