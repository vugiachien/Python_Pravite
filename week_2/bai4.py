#a

def count_bits(a):
    if a < 0:
        return count_bits(-a) + 1

    if a == 0:
        return 1

    return 0



#b
for attribute in dir(a):
    print(attribute)
