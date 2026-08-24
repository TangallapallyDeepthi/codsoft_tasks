# Product Brand Recommendation System

product_brands = {
    "laptop": [
        "Dell",
        "HP",
        "Lenovo",
        "ASUS",
        "Acer"
    ],

    "gaming laptop": [
        "ASUS",
        "Lenovo",
        "MSI",
        "Acer",
        "Alienware"
    ],

    "smartphone": [
        "Samsung",
        "Apple",
        "OnePlus",
        "Google",
        "Xiaomi"
    ],

    "iphone": [
        "Apple"
    ],

    "android phone": [
        "Samsung",
        "OnePlus",
        "Google",
        "Xiaomi",
        "Motorola"
    ],

    "headphones": [
        "Sony",
        "Bose",
        "JBL",
        "Sennheiser",
        "Boat"
    ],

    "wireless earbuds": [
        "Apple",
        "Samsung",
        "Sony",
        "JBL",
        "Boat"
    ],

    "smart watch": [
        "Apple",
        "Samsung",
        "Garmin",
        "Fossil",
        "Noise"
    ],

    "tv": [
        "Samsung",
        "LG",
        "Sony",
        "TCL",
        "Hisense"
    ],

    "refrigerator": [
        "LG",
        "Samsung",
        "Whirlpool",
        "Godrej",
        "Haier"
    ],

    "washing machine": [
        "LG",
        "Samsung",
        "Whirlpool",
        "IFB",
        "Bosch"
    ],

    "air conditioner": [
        "LG",
        "Daikin",
        "Voltas",
        "Blue Star",
        "Samsung"
    ],

    "camera": [
        "Canon",
        "Nikon",
        "Sony",
        "Fujifilm",
        "Panasonic"
    ]
}


# Program Heading
print("==============================================")
print("       PRODUCT BRAND RECOMMENDATION SYSTEM")
print("==============================================")


# Display available products
print("\nAvailable Products:")
print("------------------------------")

for product in product_brands:
    print("-", product.title())


# Continuous input
while True:

    print("\n----------------------------------------------")

    product = input("Enter product name: ")

    product = product.strip().lower()


    # Exit condition
    if product == "exit":

        print("\nThank you for using the Recommendation System!")
        break


    # Check product
    if product in product_brands:

        brands = product_brands[product]

        print("\nRecommended Brands for:",
              product.title())

        print("----------------------------------------------")

        for number, brand in enumerate(brands, start=1):

            print(f"{number}. {brand}")


    else:

        print("\nSorry! Product not found.")

        print("\nPlease select a product from the available list.")