import matplotlib.pyplot as plt


def data():
    paths = {}
    print(" what type of line do you like (:, -- or -)?")
    line = input()
    print("what type of color do you want (r, g or b)?")
    color = input()
    print("what type of marker do you want (o, s or ^)?")
    marker = input()
    paths["line"] = line
    paths['color'] = color
    paths['marker'] = marker


def generate():
    print("How many lines would you like to display?")
    num_lines = input()
    for num_line in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['line']}{values['color']}{values['marker']}"
        plt.plot(x, y, format)
    plt.show()


def run():
    print("Drawing...")
    generate()
    print("Done!")


run()
