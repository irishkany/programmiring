import unittest
from recommendation_system import MovieRecommendationSystem

class TestMovieRecommendationSystem(unittest.TestCase):
    def setUp(self):
        # Здесь можно провести начальную настройку, если необходимо
        pass

    def test_load_movies(self):
        with open("temp_movies.txt", "w", encoding="utf-8-sig") as file:
            file.write("1,Фильм1\n2,Фильм2\n3,Фильм3")

        system = MovieRecommendationSystem("temp_movies.txt", "watch_history.txt")
        movies = system.movies

        self.assertEqual(len(movies), 3)
        self.assertEqual(movies[1].title, "Фильм1")
        self.assertEqual(movies[2].title, "Фильм2")
        self.assertEqual(movies[3].title, "Фильм3")

    def test_recommend_movie(self):
        with open("temp_watch_history.txt", "w") as file:
            file.write("1,2,3\n2,4,5\n3,1,2,4")

        system = MovieRecommendationSystem("temp_movies.txt", "temp_watch_history.txt")
        recommendation = system.recommend_movie([1, 2])

        self.assertIsInstance(recommendation, str)
        self.assertNotEqual(recommendation, "")

    def tearDown(self):
        # Здесь можно провести завершающие действия, если необходимо
        pass

if __name__ == "__main__":
    unittest.main()