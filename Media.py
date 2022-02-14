import pytube

"""
This is the root class where there are several functions
"""

class Media():
    def __init__(self,name, director, IMDBscore, url, duration,dateRelease, cast):
        self.name = name
        self.director = director
        self.IMDBscore = IMDBscore
        self.url = url
        self.duration = duration
        self.dateRelease = dateRelease
        self.cast = cast

    def showInfo(self):
        print("Name:", self.name, "\n", "Director:", self.director, "\n", "Score of IMDB:", self.IMDBscore, "\n",
        "URL:", self.url, "\n", "Duration:", self.duration, "\n", "Genres:", "Date of Release:", self.dateRelease, "\n", "Cast:", self.cast
        )

    def download(self):
        youtube = pytube.YouTube(self.url)
        video = youtube.streams.get_highest_resolution()
        print(video.title)
        video.download()
    