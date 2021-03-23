my_file = open(r'data.txt', "w")  # raw

if my_file.writable():
    my_file.write("Update\n")

    strings = ["Anna\n", "Roma\n"]
    my_file.writelines(strings)
else:
    print("Can not write")

my_file.close()
    
