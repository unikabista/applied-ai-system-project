from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(file_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["danceability"] = float(row["danceability"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("Genre Match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("Mood Match (+1.0)")

    energy_score = 1.0 - abs(user_prefs["energy"] - song["energy"])
    score += energy_score
    reasons.append(f"Energy Similarity (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_results: List[Tuple[Dict, float, List[str]]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_results.append((song, score, reasons))

    # Use sorted() to return a new ordered list without mutating the input songs list.
    ranked_results = sorted(scored_results, key=lambda item: item[1], reverse=True)
    return ranked_results[:k]
