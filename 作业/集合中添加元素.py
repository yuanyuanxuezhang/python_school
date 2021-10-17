S = {128,"SET","Student",547}
T = {"Student","CS","XTU",548}
x = "set"
#********* Begin *********#
if x in S:
    print("True")
else:
    print("False")
S.add(x)
if x in S:
    print("True")
else:
    print("False")


#********* End *********#