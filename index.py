from shops import Shop

shop_name = input("Enter shops name: ")

my_shop = Shop(shop_name, 100, ["sword"], 25)

my_shop.details()