from media import Media
class Series(Media):
    def __init__(self,name, director, IMDBscore, url, duration,genres,dateRelease, cast, season, episode):
        super.__init__(self,name, director, IMDBscore, url, duration,genres,dateRelease, cast)
        self.genres = genres
        self.season = season
        self.episode = episode


    def showInfo(self):
        return Media.showInfo(self)
    

    def editSeries(self):
        self.name = input("Please enter new name: ")
        self.director = input("Please enter new director: ")
        self.IMDBscore = input("Please enter new IMDB: ")
        self.url = input("Please enter new Url: ")
        self.duration = input("Please enter new duration: ")
        self.dateRelease = input("Please enter new date of Release: ")
        self.genres = input("Please enter new genres: ")
        self.season = input("Please enter new season: ")
        self.episode = input("Please enter new episode: ")
        self.cast = input("Please enter new actor and split with (/): ")