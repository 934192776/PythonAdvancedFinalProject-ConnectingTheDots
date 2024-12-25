import csv
import matplotlib.pyplot as plt

filename = 'data.csv'

population_per_continent = {}

with open(filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    continent = line['continent']
    year = int(line['year'])
    population = int(line['population'])

    if continent not in population_per_continent:
      population_per_continent[continent] = {'population': [], 'years': []}

    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['years'].append(year)

for continent in population_per_continent:
  years = population_per_continent[continent]['years']
  population = population_per_continent[continent]['population']
  plt.plot(years, population, label=continent, marker="o")


plt.title("Internet Population per continent")
plt.xlabel("Year")
plt.ylabel("Internet users")
plt.grid(True)
plt.legend()

plt.show()