import youtube_dl
from tkinter import Tk, Label, Button, Text

class app_gui:
    print("running")

    def __init__(self):
        self.master = Tk()
        self.master.title("Youtube Downloader")

        self.master.label = Label(self.master, text="Enter a youtube link to download!")
        self.master.label.pack()

        self.master.link = Text(self.master, height=1)
        self.master.link.pack()

        self.master.labelstatus = Label(self.master, text="waiting")

        self.master.downloadButton = Button(self.master,
            text="Download",
            command=lambda : self.downloadFunction(self.master.link, self.master.labelstatus))
        self.master.downloadButton.pack()

        self.master.resetButton = Button(self.master,
            text="Reset",
            command = lambda : self.reset(self.master.link, self.master.labelstatus))
        self.master.resetButton.pack()
        self.master.labelstatus.pack()

        #run
        self.master.mainloop()

    #download function
    def downloadFunction(self, textbox, label):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '/home/benjamin/Music/%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            youtube_link = None
            try:
                if (textbox.compare("end-1c", "==", "1.0")):
                    pass
                else:
                    youtube_link = textbox.get("1.0", "end");
                    print("running");
                    print(youtube_link)
                ydl.download([youtube_link])
            except:
                pass

        label.config(text="completed")

    def reset(self, text, label):
        #reset textbox
        text.delete("1.0", "end")

        #reset labels
        label.config(text="waiting")

if __name__ == '__main__':
    app_gui()
