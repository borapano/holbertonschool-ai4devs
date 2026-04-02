import csv
from collections import defaultdict
from math import sqrt

class MovieRecommender:
    def __init__(self, ratings_file: str):
        self.user_ratings = defaultdict(dict)
        self._load_ratings(ratings_file)

    def _load_ratings(self, ratings_file):
        with open(ratings_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = int(row['user_id'])
                movie_id = int(row['movie_id'])
                rating = float(row['rating'])
                self.user_ratings[user_id][movie_id] = rating

    def _similarity(self, user1, user2):
        # Cosine similarity between two users
        common_movies = set(self.user_ratings[user1]).intersection(self.user_ratings[user2])
        if not common_movies:
            return 0
        sum1 = sum(self.user_ratings[user1][m] * self.user_ratings[user2][m] for m in common_movies)
        sum1_sqrt = sqrt(sum(self.user_ratings[user1][m]**2 for m in common_movies) *
                         sum(self.user_ratings[user2][m]**2 for m in common_movies))
        return sum1 / sum1_sqrt if sum1_sqrt != 0 else 0

    def recommend(self, target_user_id, N=5):
        if target_user_id not in self.user_ratings:
            return []

        scores = defaultdict(float)
        similarity_sums = defaultdict(float)

        for other_user in self.user_ratings:
            if other_user == target_user_id:
                continue
            sim = self._similarity(target_user_id, other_user)
            if sim <= 0:
                continue
            for movie_id, rating in self.user_ratings[other_user].items():
                if movie_id not in self.user_ratings[target_user_id]:
                    scores[movie_id] += sim * rating
                    similarity_sums[movie_id] += sim

        predicted_ratings = [(m, scores[m]/similarity_sums[m]) for m in scores if similarity_sums[m] > 0]
        predicted_ratings.sort(key=lambda x: x[1], reverse=True)
        return [{"movie_id": m, "predicted_rating": r} for m, r in predicted_ratings[:N]]