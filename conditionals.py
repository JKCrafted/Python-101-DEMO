list_1 = ["hello", "World"]


if "Hello" in list_1:
    print("Hello is in list_1")
elif "Hello".lower() in list_1:
    print("Hello.lower() is in list_1")
else:
    print("Hello and Hello.lower() are not in list_1")

if "World" in list_1:
    print("World is in list_1")
else:
    print("World is not in list_1")


if "Potato" in list_1:
    print("Potato is in list_1")
elif "Potato".lower() in list_1:
    print("Potato.lower() is in list_1")
else:
    print("Potato and Potato.lower() are not in list_1")


string_1 = "Ciao mondo"

if "Ciao" in string_1:
    print("Ciao is in string_1")
else:
    print("Ciao is not in string_1")

if "Mondo" in string_1:
    print("Mondo is in string_1")
elif "Mondo".lower() in string_1:
    print("Mondo.lower() is in string_1")
else:
    print("Mondo and Mondo.lower() are not in string_1")
