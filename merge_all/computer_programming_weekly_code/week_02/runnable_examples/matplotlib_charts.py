# Week 02: Matplotlib line, bar, and pie charts
# Install dependency: python -m pip install matplotlib
import matplotlib.pyplot as plt

def line_chart():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 4, 10]
    plt.plot(x, y, linestyle="--", marker="o")
    plt.title("Simple Line Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def bar_chart():
    products = ["Product A", "Product B", "Product C"]
    revenue = [45000, 78000, 32000]
    plt.bar(products, revenue)
    plt.ylabel("Revenue ($)")
    plt.title("Product Performance")
    plt.show()

def pie_chart():
    hobbies = ["Gaming", "Reading", "Exercise", "Gardening"]
    hours = [10, 6, 5, 3]
    plt.pie(hours, labels=hobbies, autopct="%1.1f%%")
    plt.title("Weekly Time Spent on Hobbies")
    plt.show()

if __name__ == "__main__":
    line_chart()
    bar_chart()
    pie_chart()
