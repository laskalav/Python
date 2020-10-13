catalog = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(catalog) % 2:
    last_symbol = catalog[-1]
    catalog = catalog[:-1]
    catalog[::2], catalog[1::2] = catalog[1::2], catalog[::2]
    catalog.append(last_symbol)
else:
    catalog[::2], catalog[1::2] = catalog[1::2], catalog[::2]

print(catalog)
