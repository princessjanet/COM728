import sqlite3

product_name = 0
product_description = 1
product_quantity = 2


def display_product_with_stock_levels():
    file_path = "catalogue.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT product.name, product.description, stock.quantity FROM product NATURAL JOIN stock"
    cursor.execute(sql)
    records = cursor.fetchall()
    print(f"There are {len(records)} product in the catalogue")
    print("The stock level for each product is as follows:")
    for record in records:
        print(f"product:{record[product_name]}")
        print(f"description:{record[product_description]}")
        print(f"stock_level:{record[product_quantity]}")
        print()
    db.close()


def display_product_suppliers():
    file_path = "catalogue.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name FROM product INNER JOIN supplier ON product.supplier_id=supplier.id"
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    for record in records:
        print(f"product: {record[0]}, supplier: {record[1]}")
    db.close()


def display_product_supplier_locations():
    file_path = "catalogue.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name, location.city, location.country FROM product INNER JOIN supplier ON " \
          "product.supplier_id=supplier.id INNER JOIN location ON supplier.location_id=location.id "
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    for record in records:
        print(f"product:{record[0]}, supplier: {record[1]}, location city:{record[2]}, location country: {record[3]}")
    db.close()


def display_products_missing_suppliers():
    file_path = "catalogue.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name FROM product  LEFT OUTER JOIN supplier ON product.supplier_id= " \
          "supplier.id "
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    for record in records:
        print(f"product: {record[0]}, supplier: {record[1]}")
    db.close()


def display_suppliers_missing_products():
    file_path = "catalogue.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name FROM supplier LEFT OUTER JOIN product ON supplier.id= " \
          "product.supplier_id "
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The suppliers for each product are as follows:")
    for record in records:
        print(f" product:{record[0]}, supplier: {record[1]}")
    db.close()


def display_missing_data():
    file_path = "catalogue.db"
    db = sqlite3.connect(file_path)
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name FROM product  LEFT OUTER JOIN supplier ON product.supplier_id= " \
          "supplier.id UNION product.name, supplier.name FROM supplier LEFT OUTER JOIN product ON supplier.id= " \
          "product.supplier_id"
    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        print(f"The following product are missing suppliers: {record[0]}, The following product are missing suppliers:{record[1]}")
    db.close()
