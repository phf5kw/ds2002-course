import os

os.environ["FAV_WINX"] = "MUSA"
os.environ["FAV_ANIME"] = "Time no Jikan"
os.environ["FAV_DRINK"] = "Honey and milk"

os.environ["FAV_WINX"] = input("What's your favorite winx character?")
os.environ["FAV_ANIME"] = input("What's your favorite anime?")
os.environ["FAV_DRINK"] = input("What's your favorite drink?")

FAV_WINX = os.getenv("FAV_WINX")
FAV_ANIME = os.getenv("FAV_ANIME")
FAV_DRINK = os.getenv("FAV_DRINK")

print(FAV_WINX)
print(FAV_ANIME)
print(FAV_DRINK)
