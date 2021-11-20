import matplotlib.pyplot as plt

def display(x,y):
    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    plt.plot(x,y)
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()

def run():
    print("running")
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    display(x,y)
run()
