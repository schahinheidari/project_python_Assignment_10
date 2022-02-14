import Actors, Clip, Documentary, Film, Media, Series

class main():
    def __init__(self):
        self.listOfFilm = []
        file = open('database.txt', 'r')
        data = file.read().lower().split('\n')

        for i in range(len(data)):
            movieInfo = data[i].split(',')
            if movieInfo[0] == "clip":
                self.listOfFilm.append(Clip(movieInfo))
            elif movieInfo[0] == "documentary":
                self.listOfFilm.append(Documentary(movieInfo))
            elif movieInfo[0] == "film":
                self.listOfFilm.append(Film(movieInfo))
            elif movieInfo[0] == "series":
                self.listOfFilm.append(Series(movieInfo))
            file.close()
        self.ShowMenu()
    
    def ShowMenu(self):
        print("1- SHOW MOVIE LIST\n2- ADD FILM\n3- EDIT FILM\n4-DELETE FILM\n5- DOWNLOAD FILM\n6- SEARCH BY DURATION\n7- SAVE AND EXIT")

        choice = int(input("please choose a number: "))

        if choice == 1:
            self.ShowMovieList()
        elif choice == 2:
            self.AddFilm()
        elif choice == 3:
            self.EditFilm()
        elif choice == 4:
            self.DeleteFilm()
        elif choice == 5:
            self.DownloadFilm()
        elif choice == 6:
            self.SearchInList()
        elif choice == 7:
            self.SaveAndExit()
        else:
            print("wrong number")
    
    def ShowMovieList(self):
        for i in self.listOfFilm:
            i.showInfo()

    def AddFilm(self):
        name = input("Please enter new name: ")
        director = input("Please enter new director: ")
        IMDBscore = input("Please enter new IMDB: ")
        url = input("Please enter new Url: ")
        duration = input("Please enter new duration: ")
        dateRelease = input("Please enter new date of Release: ")
        cast = input("Please enter new actor and split with (/): ")
        category =input("Please enter the category (film/series/clip/documentary): ")

        if category == 'series':
            genres = input("Please enter new genres: ")
            season = input("Please enter new season: ")
            episode = input("Please enter new episode: ")
            movieInfo = [category,name,director,IMDBscore,url,duration,dateRelease,genres,cast,season,episode]

        elif category == 'film':
            genres = input("Please enter new genres: ")
            movieInfo = [category,name,director,IMDBscore,url,duration,dateRelease,genres,cast]
            self.movielist.append(Film(movieInfo)) 

        #elif category == 'series':
        #    self.movielist.append(Series(movieInfo))

        elif category == 'clip':
            theme = input("Please enter new theme: ")
            movieInfo = [category,name,director,IMDBscore,url,duration,dateRelease,theme,cast]
            self.movielist.append(Clip(movieInfo))

        elif category == 'documentary':
            type = input("Please enter new type: ")
            movieInfo = [category,name,director,IMDBscore,url,duration,dateRelease,type,cast]
            self.movielist.append(Documentary(movieInfo))

        else:
            print("This type of category doesn't exist!")
        
        self.ShowMovieList()
        self.ShowMenu()

    def EditFilm(self):
        choice = input("Please enter name of the movie that you want to edit: ")
        for i in self.listOfFilm:
            if choice == i.name:
                if i.category == "film":
                    i.edit_film()
                elif i.category == "series":
                    i.edit_series()
                elif i.category == "clip":
                    i.edit_clip()
                elif i.category == "documentary":
                    i.edit_documentary()

    def DeleteFilm(self):
        choice = input("Please enter name of the movie that you want to delete: ")
        for i in self.listOfFilm:
            if choice == i.name:
                self.listOfFilm.remove(i)
                print("The movie was successfully deleted")
        self.ShowMenu()


    def DownloadFilm(self):
        choice = input("Please enter name of the movie that you want to download: ")
        for i in self.listOfFilm:
            if choice == i.name:
                i.download()
                print("The movie was successfully downloaded")
            else:
                print("this movie doesn\'t exist")
        self.ShowMenu()

    def SearchInList(self):
        choice = int(input("Please enter  the name of media: "))
        for i in self.listOfFilm:
            if i.name == choice :
                i.showInfo()

    def SearchByDuration(self):
        choiceA = int(input("Please enter first duration: "))
        choiceB = int(input("Please enter second duration: "))
        for i in self.listOfFilm:
            if choiceA <= int(i.duration) <= choiceB:
                i.showInfo()


    def SaveAndExit(self):
        file =open('database.txt', 'w')
        for i in self.listOfFilm:
            if i.category == "series":
                file.write((i.category)+','+(i.name)+','+(i.director)+','+(i.IMDBscore)+','+(i.url)+','+(i.duration)+','+(i.dateRelease)+','+(i.genres)+','+(i.cast)+','+(i.season)+','+(i.episode))
            else:
                file.write((i.category)+','+(i.name)+','+(i.director)+','+(i.IMDBscore)+','+(i.url)+','+(i.duration)+','(i.dateRelease)+','+(i.genres)+','+(i.cast))
            if i != self.listOfFilm[-1]:
                file.write('\n')
                

        file.close()
        print("Database updated succssefully")
        exit() 





