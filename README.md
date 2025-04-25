# NASA APOD Wallpaper Setter 🚀🛰️

This is a tiny Python script that automatically downloads the NASA Astronomy Picture of the Day (APOD) and sets it as your Windows desktop wallpaper.

## 🌌 Features

- Uses NASA's [APOD API](https://api.nasa.gov/) to fetch the latest high-resolution image.
- Downloads and saves the image locally as `NASA_apod.png`.
- Sets the image as your desktop wallpaper using Windows system calls.
- Automatically adjusts wallpaper style to “Fit”.

## 📁 Project Structure

/ (root) ├── main.py # Main script that fetches and sets the wallpaper ├── launch.bat # Windows batch file to run the script easily

## 🛠️ Setup Instructions

1. **Get a NASA API key**:
   - Go to [https://api.nasa.gov](https://api.nasa.gov)
   - Fill out the form to request an API key (it’s instant and free!)
   - You'll get a string your own private key in your mailbox. (don't worry it's NASA not spammers) :D

2. **Edit the script**:
   - Open `main.py`
   - Replace this line at the top of the script:
     ```python
     api_key = "INSERT_YOU_NASA_API_KEY - see readme"
     ```
    and
    - Replace this line:
     ```python
     api_endpoint = "https://api.nasa.gov/planetary/apod?api_key=INSERT_YOU_NASA_API_KEY - see readme"
     ```
     with your actual key

2. **Edit the launch script** (optional): 
   - Open `launch.bat`
   - Replace this line:
     ```python
     cd <insert_your_full_folder_here>
     ```
     with the folder where the actual pyhton script script is. It will be used by windows scheduler to auto-change the wallpaper with the last image if you want to make it automagic

3. **Run the script**:
   - Double-click `launch.bat` (on Windows)
   - Or run `python main.py` from a terminal

## ✅ Requirements

- Python 3.x
- Internet connection
- Windows OS (tested on Windows 10+)

All dependencies are from the standard library (`requests`, `urllib`, `ctypes`, `os`, `winreg`), so no need to install anything extra unless you're using a very stripped-down Python install.

## 📝 Notes

- This script uses the **high-resolution** version of the image (`hdurl`). If you want smaller files or compatibility with lower resolutions, change the URL key to `url` instead of `hdurl`.
- The wallpaper is saved as `NASA_apod.png` in the same folder as the script.
- For consistent daily use, you could schedule this script via Windows Task Scheduler using the bat file for the magic happen with no struggle!

## 👽 License

MIT License. Use it, fork it, tweak it, share it with space-loving friends (and tell me what do you think) 🌠
