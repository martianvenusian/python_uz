def print_fuc(name):
    print(name)

# str_name = "Husan"
# print_fuc(str_name)


def print_fuc2(name1, name2):
    print(name1)
    print(name2)


# str_name = "Husan"
# print_fuc2(str_name, "Akbar")


def math_fuc(a, b):
    c = a + b
    print(c)


# math_fuc(1, 2)
# math_fuc(3, 4)


def return_fuc(a, b):
    c = a + b
    return c


# result = return_fuc(3, 3)
# print(result)

def sa_sb_sc(a, b):
    return a*a + b*b


# Keyword Arguments
#print_fuc2(name2="Akbar", name1='Husan')

# Default Values


def print_fuc3(name1, name2='Akbar'):
    print(name1)
    print(name2)


print_fuc3('Husan')
print_fuc3(name1='Husan')

print_fuc3('Husan', "Hasan")
print_fuc3('Husan', name2="Hasan")
print_fuc3(name1='Husan', name2="Hasan")
print_fuc3(name2="Hasan", name1='Husan')

# print_fuc3() # Error
