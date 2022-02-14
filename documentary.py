from media import Media

class Documentary(Media):
    def __init__(self,name, director, IMDBscore, url, duration, dateRelease, cast, type):
        super.__init__(self,name, director, IMDBscore, url, duration, dateRelease, cast)
        self.type = type


    def showInfo(self):
        return Media.showInfo(self), print("Type:", self.type)

    def editDocument(self):
        self.name = input("Please enter new name: ")
        self.director = input("Please enter new director: ")
        self.IMDBscore = input("Please enter new IMDB: ")
        self.url = input("Please enter new Url: ")
        self.duration = input("Please enter new duration: ")
        self.dateRelease = input("Please enter new date of Release: ")
        self.type = input("Please enter new type: ")
        self.cast = input("Please enter new actor and split with (/): ")