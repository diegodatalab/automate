import requests

gol = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-07-26&sortBy=publishedAt&apiKey=9474327083794927ab4c266446ba0fba")

content = gol.json()

print(content)


# 9474327083794927ab4c266446ba0fba