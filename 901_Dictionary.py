dict = {}  # Create an empty dictionary
dict['one'] = "1 - hello,world"  # Create a value with a key of 'one'
dict[2] = "2 - 嘿嘿"  # Create a value with a key of 2
# print(dict)  # see the result


surface_tar = {'TP': [0.01, 0.025, 0.05, 0.1, 0.2],
               'TN': [0.2, 0.5, 1.0, 1.5, 2.0]}
print(surface_tar['TP'])  # Output the value with a key of 'TP' # list
print(surface_tar['TP'][0])  # Output a value
print(surface_tar.keys())  # Output all keys
print(surface_tar.values())  # Output all values
