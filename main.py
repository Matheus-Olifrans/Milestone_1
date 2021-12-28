movies = []


def menu():
    option = input('''
                 press 1 to add new movie to colection 
                 press 2 to see your current colection 
                 press 3 to search movies in colection 
                 press q to quit program and lose all data 
                              cmd: ''')
    return option


def add(currentmovies):
    while 1 == 1:
        title = input('''
        what is the movie title:

        ''')
        director = input('''
        what is the movie director
        
        ''')
        year = input('''
        when was the movie made
        
        ''')
        whatdo = input('''
        press c to cancel or r to redo
        press anything else to continue
        once movie has been added it cannot be removed
        
        ''')
        if whatdo == 'c':
            return currentmovies
        elif whatdo == 'r':
            continue
        else:
            break
    new_movie = {
        "title": title,
        "director": director,
        "year": year
    }
    currentmovies.append(new_movie)
    return currentmovies


def see(showmenu):
    for index in range(len(showmenu)):
        print(showmenu[index], " \n ")
    return showmenu


def search(lookmovies):
    searched = input('what movie do you want to search:\n')
    for index in lookmovies:
        if index["title"].lower() == searched.lower():
            print(index)
    return lookmovies


all_functions = {
       '1': add,
       '2': see,
       '3': search,
       'q': exit
    }
while 1 == 1:
    chosen = menu()
    print("\n\n")
    if chosen in all_functions:
        movies = all_functions[chosen](movies)
        print("\n\n")
    else:
        print('invalid command please try again/n/n')
