lower_limit = 35.9
upper_limit = 40.377

shop_dict = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

m_shops = []  # Create an empty list to store the matching shop names

# Iterate over the key-value pairs in the shop_dict
for key, value in shop_dict.items():
    if lower_limit <= value <= upper_limit:  # Add the shop name to the m_shops list if the price falls within the desired range
        m_shops.append(key)
# Join the shop names in m_shops using a comma and space to create a single string
shops_str = ", ".join(m_shops)
print(shops_str)
