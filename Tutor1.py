

def salary():
    x = []
    while True:
        salary_input = int(input("Please enter salary "))
        if salary_input == 0:
            break
        else:
            x.append(salary_input)
    print("The maximun salary is: ", max(x))
            

def print_1_5():
    input_ = int(input("Please inter a number: "))
    for _ in range(input_):
        print("1 2 3 4 5")

def pyramid():
    input_ = int(input("Please inter a number: "))
    for j in range(input_):
        x = []
        for i in range(1,j+2):
            x.append(i)
        print(x)


if __name__ == "__main__":
    # salary()
    # print_1_5()
    pyramid()