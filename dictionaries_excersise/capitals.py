countries = input().split(", ")
capitals = input().split(", ")

capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}
for county, capital in capital_by_country.items():
    print(f'{county} -> {capital}')

# capital_by_country = {f'{countries[idx]}: {capitals[idx]}' for idx in range(len(countries))}
# print('\n'.join(capital_by_country))
#capital_by_country = {}
#for idx in range(len(countries)):
#   country = countries[idx]
#   capital = capitals[idx]
#   capital_by_country[country] = capital
#print(dict(zip(countryes,capitals)))