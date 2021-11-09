import database


def menu():
    print("Please select one of the following option:")
    print("[1] Display the stock level")
    print("[2] Display the supplier")
    print("[3] Display supplier locations")
    print("{4] Display missing supplier")
    print("[5] Display missing products")
    print("[6] Display missing data")
    option = int(input("Your selection:"))
    return option


def run():
    option = menu()
    if option == 1:
        database.display_product_with_stock_levels()
    elif option == 2:
        database.display_product_suppliers()
    elif option == 3:
        database.display_product_supplier_locations()
    elif option == 4:
        database.display_products_missing_suppliers()
    elif option == 5:
        database.display_suppliers_missing_products()
    elif option == 6:
        database.display_missing_data()


if __name__ == "__main__":
    run()
