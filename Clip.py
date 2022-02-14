import Media
class Clip(Media):
    def __init__(self,name, director, IMDBscore, url, duration,dateRelease, cast, theme):
        super.__init__(self,name, director, IMDBscore, url, duration,dateRelease, cast)
        self.theme = theme


    def showInfo(self):
        return Media.showInfo(self)
    
    def editClip(self):
        self.name = input("Please enter new name: ")
        self.director = input("Please enter new director: ")
        self.IMDBscore = input("Please enter new IMDB: ")
        self.url = input("Please enter new Url: ")
        self.duration = input("Please enter new duration: ")
        self.dateRelease = input("Please enter new date of Release: ")
        self.theme = input("Please enter new theme: ")
        self.cast = input("Please enter new actor and split with (/): ")
        