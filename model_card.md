# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

This recommender is intended as a classroom demonstration of content-based filtering for students. It suggests top-k songs from a small fixed catalog using user preferences for genre, mood, and energy. It is designed for learning and experimentation, not production deployment.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

### Algorithm Summary

Each song gets a weighted score from three parts:
- Genre match: add +2.0 if song genre equals the user's preferred genre.
- Mood match: add +1.0 if song mood equals the user's preferred mood.
- Energy similarity: add `1.0 - abs(user_energy - song_energy)` so closer energy values score higher.

Songs are ranked by total score in descending order, and the system returns the top-k songs with text reasons that explain which components contributed to the final score.

This model is static: it does not learn from clicks, skips, likes, or listening history over time.

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

### Limitations

- Catalog bias: if certain genres dominate the dataset, recommendations will overexpose those genres.
- Fixed weights: the +2.0 genre bonus can overpower other signals and reduce diversity.
- Static behavior: no online learning, so the model cannot adapt when user preferences change.
- Limited features: ignores lyrics, context (time/activity), and novelty preferences.

Current scoring can create a filter bubble if the catalog is imbalanced (for example, mostly pop songs). Genre gets a strong +2.0 boost, so songs in overrepresented genres dominate top-k more often, even when mood or energy are not a strong fit. Users can get repeatedly exposed to the same style and miss adjacent genres.

Energy similarity is linear: `1.0 - abs(target - song_energy)`. This is easy to reason about, but it can become too punishing near the edges. Example: if target is 0.40 and a song has 0.55 energy, it loses 0.15 immediately even though the song may still feel close in practice. With a small dataset, this can reduce diversity because slightly-off songs drop below exact-genre matches.

Potential mitigation ideas:
- Add a small diversity bonus for underrepresented genres in top-k.
- Cap genre dominance by lowering genre weight in later ranking passes.
- Use a softer energy curve (for example, Gaussian-style similarity) so near misses are penalized less aggressively.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
