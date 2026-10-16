# Plot daily temperatures for four weeks
import matplotlib.pyplot as plt

temperatures = [
    [30, 31, 32, 30, 30, 31, 33],
    [29, 30, 31, 32, 31, 30, 29],
    [31, 32, 33, 34, 33, 32, 31],
    [30, 29, 30, 31, 32, 31, 30],
]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for week_number, week in enumerate(temperatures, start=1):
    plt.plot(days, week, marker="o", label=f"Week {week_number}")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.title("Temperature for 4 Weeks")
plt.legend()
plt.tight_layout()
plt.show()
