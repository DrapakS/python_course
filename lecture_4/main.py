global_variable = 10
global_variable_2 = 111

def f1():
    print("In f1 function:", global_variable)
    local_variable = "ABC"
    global_variable_2 = 222


def f2():
    print("In f2 function:", global_variable)
    global_variable = 20


def f3():
    global global_variable
    print("In f3 function:", global_variable)
    global_variable = 30


def f4():
    print("F4 v1")


def f4():
    print("F4 v2")


#f1()
#print(local_variable)
#print(global_variable_2)
#f2()
#f3()
#print("After f3 function:", global_variable)
#f4()