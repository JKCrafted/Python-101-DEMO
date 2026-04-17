import os, shutil

items = os.listdir()

for item in items:
    print(item)
    if not os.path.isdir(item) and item != os.path.basename(__file__):
        file_type = item.split(".")[-1] # Splits the item name into a list by "." and gets the final part, thus returning the file name
        if file_type not in os.listdir():
            os.mkdir(file_type)
        shutil.move(item, file_type+"/"+item)