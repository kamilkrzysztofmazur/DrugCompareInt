import requests, sys, webbrowser, bs4

print('Wpisz nazwe leku 1: ')
lek1 = input()
print('Wpisz nazwe leku 2: ')
lek2 = input()
print('Wpisz nazwe choroby: ')
choroba = input()

search = f"{lek1}+{lek2}+{choroba}"
r = requests.get(f"https://scholar.google.com/scholar?hl=pl&as_sdt=0%2C5&q= {search}")
r.raise_for_status()
print(r.url)

#linkOpening =

