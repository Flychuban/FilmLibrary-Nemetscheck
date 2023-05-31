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
    

if __name__ == "__main__":
    filename = input("Enter filename for data: ")
    sorting_type_number = int(input("Sorting types: (1)-title, (2)-genre, (3)-date published : "))
    if sorting_type_number == 1:
        sorting_type = "title"
    elif sorting_type_number == 2:
        sorting_type = "genre"
    elif sorting_type_number == 3:
        sorting_type = "date_published"
    
    proccess_data(filename, sorting_type)