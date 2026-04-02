class TestMovieRecommender(unittest.TestCase):

    def setUp(self):
        self.recommender = MovieRecommender("reference/tests/ratings_test.csv")

    def test_small_dataset(self):
        result = self.recommender.recommend(1, N=3)
        self.assertEqual(len(result), 3)

    def test_sparse_dataset(self):
        result = self.recommender.recommend(2, N=5)
        self.assertTrue(len(result) <= 5)

    def test_user_rated_all(self):
        result = self.recommender.recommend(3, N=10)
        self.assertEqual(result, [])

    def test_empty_dataset(self):
        empty_recommender = MovieRecommender("reference/tests/ratings_empty.csv")
        result = empty_recommender.recommend(4, N=3)
        self.assertEqual(result, [])

    def test_tie_scores(self):
        result = self.recommender.recommend(5, N=2)
        self.assertEqual(len(result), 2)

    # Additional tests
    def test_unknown_user(self):
        result = self.recommender.recommend(999, N=3)
        self.assertEqual(result, [])

    def test_single_movie_user(self):
        result = self.recommender.recommend(6, N=1)
        self.assertEqual(len(result), 1)

    def test_N_greater_than_available(self):
        result = self.recommender.recommend(7, N=100)
        self.assertTrue(len(result) <= 100)

    def test_similarity_zero(self):
        result = self.recommender.recommend(8, N=2)
        self.assertTrue(all(r["predicted_rating"] > 0 for r in result))

    def test_large_N(self):
        result = self.recommender.recommend(1, N=50)
        self.assertTrue(len(result) <= 50)

    def test_additional_dataset(self):
        additional_recommender = MovieRecommender("reference/tests/ratings_additional.csv")
        result = additional_recommender.recommend(9, N=2)
        self.assertTrue(len(result) <= 2)