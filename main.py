import requests
import urllib
import ctypes
import winreg
import os

api_key = "INSERT_YOU_NASA_API_KEY - see readme"
api_endpoint = "https://api.nasa.gov/planetary/apod?api_key=INSERT_YOU_NASA_API_KEY - see readme"
nasa_response = requests.get(api_endpoint) #prendo la risposta dal sito nasa che è un json
nasa_dict = nasa_response.json()  #e lo trasformo in un dizionario

#da qui accedo ai valori del dizionario in modo diretto, so come si chiamano i valori perchè sono scritti
#nella documentazione della nasa.Così ho tutti i valori che mi servono nelle relative variabili
titolo = nasa_dict["title"]
data = nasa_dict["date"]
spiegazione = nasa_dict["explanation"]
url = nasa_dict["hdurl"]

#scarico l'immagine in locale
urllib.request.urlretrieve(url,"NASA_apod.png")

#imposto come sfondo
# Set the path of the wallpaper image
wallpaper_path = wallpaper_path = os.path.abspath("NASA_apod.png")

# Costanti
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 1
SPIF_SENDWININICHANGE = 2

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "6")  # 6 = Fit
winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")   # No tile
winreg.CloseKey(key)

# Applica lo sfondo
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, wallpaper_path,
    SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
)