# Youtube Downloader
A python app that takes youtube video links and downloads the mp3 to /home/benjamin/Music  
@author Benjamin Ahn  

### Technologies
Python 3.6  
Tkinter  
Youtube-dl  
ffmpeg  

### Launch
Must install Tkinter and ffmpeg
sudo apt-get install python3-tk  
sudo apt-get install ffmpeg

### Table of Contents
* Youtube-dl
* App GUI
* Installing on Linux Desktop

### Youtube-dl
Several files are to support the Youtube-dl, which is the primary method of converting youtube links to mp3's  

### App GUI
The app_gui.py file holds the code to launch the Tkinter GUI and methods to download links

### Installing on Linux Desktop
pyinstaller was used to package the application. The program executable for linux is under ./dist/main. Click to launch  

### Credits
@author Benjamin Ahn  
@version 1.0 basic, downloads a link
@version 1.1 reset button will clear textbox and reset status label
