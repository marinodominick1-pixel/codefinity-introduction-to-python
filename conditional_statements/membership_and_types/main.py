# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120
contains_raw = "raw" in description
print("contains 'raw':", contains_raw)
contains_Imported = "Imported" in description
print("contains 'Imported':", contains_Imported)
price_is_float = type(price) == float
print("Is price a float?:", str (price_is_float).lower())
count_is_int = type(count) == int
print("Is count an integer?:", str(count_is_int).lower()