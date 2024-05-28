# PROGRAMS TO PRINT PATTERNS IN PYTHON 
#1  *******


def hlinepattern():

    length = int(input("Enter the Number of stars in a row: "))

    for i in range(0,length):

        print("*", end="")


hlinepattern()