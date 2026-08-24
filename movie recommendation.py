movies = {
    "action": [
        "Avengers: Endgame",
        "John Wick",
        "Mission Impossible",
        "Top Gun: Maverick"
    ],

    "comedy": [
        "3 Idiots",
        "Hera Pheri",
        "Welcome",
        "Hangover"
    ],

    "horror": [
        "The Conjuring",
        "Insidious",
        "IT",
        "A Quiet Place"
    ],

    "romance": [
        "Jab We Met",
        "Yeh Jawaani Hai Deewani",
        "La La Land",
        "The Notebook"
    ],

    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Martian",
        "Dune"
    ]
}


def show_genres():
    print("\nAvailable Genres:")
    for genre in movies:
        print("-", genre.title())


def recommend_movies():
    show_genres()

    genre = input("\nEnter your favourite genre: ").lower()

    if genre in movies:
        print(f"\n🎬 Movies recommended for you:")

        for i, movie in enumerate(movies[genre], 1):
            print(f"{i}. {movie}")

    else:
        print("❌ Sorry, this genre is not available.")


while True:

    print("\n==============================")
    print("     MOVIE RECOMMENDATION")
    print("==============================")

    print("1. Get Recommendations")
    print("2. Show All Genres")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        recommend_movies()

    elif choice == "2":
        show_genres()

    elif choice == "3":
        print("Thanks for using Movie Recommendation System 🎬")
        break

    else:
        print("❌ Invalid choice!")