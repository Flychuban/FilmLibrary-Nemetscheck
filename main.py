from Film import Film

def proccess_data(filename, sorting_type):
    all_films = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            title, genre, date_published, actors = line.split(";")
            actors = actors.split(",")
            film = Film(title, genre, date_published, actors)
            all_films.append(film)
    
    all_films.sort(key=lambda film: getattr(film, sorting_type))
    
    all_films.sort(key=lambda film: film.title == "The Matrix", reverse=True)
    
    with open("all_films_sorted.txt", "w") as f:
        for film in all_films:
            f.write(film.title + ";" + film.genre + ";" + film.date_published + ";" + ",".join(film.actors) + "\n")
    
    print(f"All films successfully sorted by {sorting_type}:")
    
    for film in all_films:
        print(film.title, film.genre, film.date_published, film.actors)
            
    
    



if __name__ == "__main__":
    filename = "all_films.txt"
    sorting_type = 'title'
    proccess_data(filename, sorting_type)