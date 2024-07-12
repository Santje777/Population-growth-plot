import matplotlib.pyplot as plt

years = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030]
paris_population = [8, 9, 10, 11, 11.5, 12, 12, 11.5]
new_york_population = [5, 6, 8, 11, 13, 14, 16, 18.5]
sydney_population = [5, 4, 5, 6, 5, 5.5, 5.8, 6.2]

print(plt.style.available)
plt.style.use('Solarize_Light2')

plt.plot(years, paris_population, label="Paris", color='b', marker='.')
plt.plot(years, new_york_population, label="New York", color='g', marker=".")
plt.plot(years, sydney_population, label="Sydney", color='r', linestyle="--", linewidth=2, marker='.')

plt.grid(True)

plt.title("Population growth")
plt.xlabel('Year')
plt.ylabel("Population (in Million)")
plt.legend()


plt.show()