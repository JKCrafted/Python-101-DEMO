import os, hashlib, shutil

items = os.listdir()
md5Hashes = []

for item in items:
    print(item)
    if not os.path.isdir(item) and item != os.path.basename(__file__):
        md5 = str(hashlib.md5(open(item,'rb').read()).hexdigest())
        if md5 not in md5Hashes:
            md5Hashes.append(md5)
        else:
            if not os.path.exists("Dupe/"):
                os.mkdir("Dupe/")
            shutil.move(item, "Dupe/"+item)
        