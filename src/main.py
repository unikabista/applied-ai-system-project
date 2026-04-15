"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Chill Lofi profile
    user_prefs = {"genre": "lofi", "mood": "chill", "energy": 0.2}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n=== Top Recommendations: Chill Lofi ===\n")
    for rec in recommendations:
        song, score, reasons = rec
        print(f"{song['title']} by {song['artist']} | Score: {score:.2f}")
        print("  Reasons:")
        for reason in reasons:
            print(f"    - {reason}")
        print()


if __name__ == "__main__":
    main()
