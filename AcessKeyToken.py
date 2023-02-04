import requests


data = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
data = data.json()
print(data)
