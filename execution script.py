import binaryCode as bc
import pyperclip
import time
a = input("encode, decode, or make a key[e/d/m]?\n")
if a == "e":
    bc.encode(input("what text?\n"), input("what key?\n"))
    print("file saved as photo.jpeg.\nRename for extra security.")
elif a == "d":
    print(bc.decode(input("what key?\n"), input("filename?\n")))
    print("that's the code.")
elif a == "m":
    pyperclip.copy(bc.generateKey(False))
    print("key copied to clipboard.")
else:
    print("??? i dont get it")
time.sleep(5)