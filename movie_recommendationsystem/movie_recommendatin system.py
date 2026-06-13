movies = {
    "Telugu": {
        "Action": [("RRR", 8.8), ("Salaar", 8.2), ("Pushpa", 7.9)],
        "Comedy": [("Jathi Ratnalu", 8.3), ("DJ Tillu", 8.1), ("MAD", 8.0)],
        "Thriller": [("Hit", 8.0), ("Goodachari", 8.5), ("Kshanam", 8.3)],
        "Drama": [("Jersey", 8.6), ("Sita Ramam", 8.7), ("Mahanati", 8.8)],
        "Horror": [("Virupaksha", 8.3), ("Masooda", 8.0), ("Pindam", 7.8)]
    },

    "Hindi": {
        "Action": [("Jawan", 7.5), ("Pathaan", 7.2), ("War", 7.8)],
        "Comedy": [("3 Idiots", 8.4), ("Munna Bhai MBBS", 8.1), ("Bhool Bhulaiyaa 2", 6.8)],
        "Thriller": [("Drishyam 2", 8.3), ("Andhadhun", 8.2), ("Kahaani", 8.1)],
        "Drama": [("Dangal", 8.4), ("Taare Zameen Par", 8.3), ("12th Fail", 9.0)],
        "Horror": [("Stree", 7.5), ("Tumbbad", 8.2), ("Bhoot", 6.7)]
    },

    "Tamil": {
        "Action": [("Leo", 7.8), ("Vikram", 8.4), ("Kaithi", 8.5)],
        "Comedy": [("Doctor", 7.5), ("Boss Engira Bhaskaran", 7.8), ("OK OK", 7.0)],
        "Thriller": [("Ratsasan", 8.3), ("Thadam", 8.1), ("Dhuruvangal Pathinaaru", 8.2)],
        "Drama": [("96", 8.5), ("Soorarai Pottru", 8.7), ("Asuran", 8.4)],
        "Horror": [("Demonte Colony", 7.5), ("Maya", 7.6), ("Pizza", 8.0)]
    },

    "Malayalam": {
        "Action": [("Aavesham", 8.0), ("Lucifer", 7.5), ("Bheeshma Parvam", 8.0)],
        "Comedy": [("Premalu", 8.3), ("Romancham", 8.0), ("Jan-e-Man", 7.8)],
        "Thriller": [("Drishyam", 8.6), ("Anjaam Pathiraa", 8.0), ("Mumbai Police", 7.9)],
        "Drama": [("Home", 8.7), ("2018", 8.4), ("The Great Indian Kitchen", 8.3)],
        "Horror": [("Bramayugam", 8.1), ("Ezra", 7.0), ("Bhoothakaalam", 7.8)]
    }
}

print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

username = input("\nEnter your name: ")
print(f"\nWelcome {username}!  Let's explore movies!")

while True:

    print("\nAvailable Languages:")
    for lang in movies:
        print("-", lang)

    language = input("\nChoose Language: ").title()

    if language in movies:

        print("\nAvailable Genres:")
        for genre in movies[language]:
            print("-", genre)

        genre = input("\nChoose Genre: ").title()

        if genre in movies[language]:

            movie_list = movies[language][genre]

            print(f"\nTop {genre} Movies in {language}:\n")

            for i, (movie, rating) in enumerate(movie_list, start=1):
                print(f"{i}. {movie}  {rating}")

            print(f"\nTotal Movies Found: {len(movie_list)}")

            print("\nRecommended Movies For You:\n")

            for movie, rating in movie_list:
                print(f"{movie}  {rating}")

        else:
            print("Invalid Genre!")

    else:
        print("Invalid Language!")

    again = input("\nDo you want another recommendation? (yes/no): ").lower()

    if again != "yes":
        print(f"\nThank you {username}! Enjoy your movies and have a great day! ")
        break
