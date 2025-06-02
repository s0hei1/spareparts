from operator import itemgetter

ls = [('Soheil', 1), ('Mohsen', 2), ('Hossein', 3)]

getItem = itemgetter(0)

for i in ls:
    print(getItem(i))