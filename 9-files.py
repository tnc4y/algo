"""with open("file.txt", 'r') as f:
    data = f.read()
    print(data)"""

"""with open("file.txt", 'r') as f:
    satir = f.readline()
    print(satir)"""

"""with open("file.txt", 'r') as f:
    for satir in f:
        print(satir.strip())"""

"""with open("file.txt", 'r') as f:
    data = f.readlines()
    print(data)"""

with open("file.txt", 'w') as f:
    f.write("Merhaba Dünya!\n")
    f.writelines(["Bu bir satırdır.\n", "Bu da başka bir satırdır.\n"])

with open("file.txt", 'a') as f:
    f.write("Bu bir ek satırdır.\n")