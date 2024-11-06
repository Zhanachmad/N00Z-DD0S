import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt-get install nodej-lts")
    os.system("apt-get install npm")
    os.system("npm install os")
    os.system("npm install sys")
    os.system("npm install threading")
   elif c == "1":
    os.system("apt-get install nodej-lts")
    os.system("apt-get install npm")
    os.system("npm install os")
    os.system("npm install sys")
    os.system("npm install threading")
print("Done.")



