def sort_games(games, sorting_option):
    if sorting_option == "Name (A-Z)":
        return sorted(games, key=lambda x: x["name"].lower())

    elif sorting_option == "Name (Z-A)":
        return sorted(games, key=lambda x: x["name"].lower(), reverse=True)

    elif sorting_option == "Release Date (New)":
        return sorted(games, key=lambda x: x.get("release_date", "1970-01-01"), reverse=True)

    elif sorting_option == "Release Date (Old)":
        return sorted(games, key=lambda x: x.get("release_date", "1970-01-01"))

    elif sorting_option == "Rating (High)":
        return sorted(games, key=lambda x: x.get("rating", 0), reverse=True)

    elif sorting_option == "Rating (Low)":
        return sorted(games, key=lambda x: x.get("rating", 0))

    return games
