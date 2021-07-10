#A MOVIE COLLECTION APP
#Hint: Requirement :
# user story- add new movie to collection, list movie collection you have (they wont define database,, find movie collection
#implementation: decide where to store the code, decide what data we want to store,show user menu and let them pick an option; implement each requirement in turn as a seperate function; stop when they want to


#STORE MOVIES IN PYTHON LIST: A. SINCE NO DATABASE, WE WILL USE PYTHON LIST

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = [] #movies list were we are going to store our movies

def add_movie():
    #dictionary #asking the data that application needs
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    #appending this as a list
    movies.append ( {
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():          #to show the list of movies we will iterate/or use a loop over the list that will give us a dictionary for each element in the list
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you're looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)

user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
  }

def menu():
        selection = input(MENU_PROMPT)
        #menu
        while selection != 'q':
            if selection in user_options:
                selected_function = user_options[selection]
                selected_function()
            else:
                print("Unknown command. Please try again.")

            selection = input(MENU_PROMPT)


menu()
