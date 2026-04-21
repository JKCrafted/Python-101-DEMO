try:
    new_var = 12 / "Potato"
except TypeError as error:
    print("A type error has occured\n", error)
finally:
    print("Reached the end")


try:
    new_var = 12 / 3
except TypeError as error:
    print("A type error has occured\n", error)
finally:
    print("Reached the end")