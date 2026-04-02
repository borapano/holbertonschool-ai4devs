# Cross-Language Specification - Movie Recommendation Engine

## Algorithm
Generate personalized movie recommendations using collaborative filtering:
- Identify users with similar rating patterns to the target user.
- Compute similarity-weighted scores for movies the target user has not rated.
- Return the top N movies sorted by predicted rating.

## Inputs
- `user_ratings.csv`: CSV file with columns `user_id, movie_id, rating`
- `target_user_id`: ID of the user to generate recommendations for
- `N`: Number of recommendations to return

## Outputs
- JSON array of recommended movies with predicted ratings, e.g.:
```json
[
  {"movie_id": 102, "predicted_rating": 4.7},
  {"movie_id": 57, "predicted_rating": 4.5}
]

## Edge Cases
- Target user has no prior ratings
- Requested N exceeds the number of unseen movies
- Sparse rating data with few similar users
- Multiple movies have identical predicted scores
- Target user has already rated all movies

## Test Cases
- `ratings_small.csv`, target_user_id=1, N=3 → Returns 3 unseen movies with top predicted ratings
- `ratings_sparse.csv`, target_user_id=2, N=5 → Returns ≤5 movies due to sparse data
- `ratings_full.csv`, target_user_id=3, N=10 → User has rated all movies → Returns empty list
- `ratings_empty.csv`, target_user_id=4, N=3 → No ratings in dataset → Returns empty list
- `ratings_tie.csv`, target_user_id=5, N=2 → Two movies with identical predicted ratings → Both included