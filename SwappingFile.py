def swapFileData():    
    file_1 = ("sample1.txt")
    file_2 = ("sample2.txt")
    with open(file_1, "ro") as a:
      data_1 =  a.read()
    with open(file_2, "ro") as b:
      data_2 = b.read()

    with open(file_1, "w") as a:
      a.write(data_2)
    with open(file_2, "w") as b:
      b.write(data_1)
      
swapFileData()