import zipfile

def crack_password(password_list, obj) :
    idx = 0

    with open(password_list, "rb") as file:
        for line in file :
            for word in line.split():
                try :
                    idx += 1
                    obj.extractall(pwd=word)
                    print("password found in line:", idx)
                    print("password is", word.decode())
                    return True
                except :
                    continue
    return False

password_list = "C:\\Users\\acer\\Desktop\\uts\\rockyou.txt"

zip_file = "C:\\Users\\acer\\Desktop\\uts\\111.zip"

obj = zipfile.PyZipFile(zip_file)

cnt = len(list(open(password_list, "rb")))

print("there all total", cnt,"number of password to test")

if crack_password(password_list, obj):False
print("password not found in this file")