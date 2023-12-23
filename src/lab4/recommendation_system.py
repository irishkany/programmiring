import random

class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title

class MovieRecommendationSystem:
    def __init__(self, movies_file, watch_history_file):
        self.movies = self.load_movies(movies_file)
        self.watch_history = self.load_watch_history(watch_history_file)

    def load_movies(self, file_path):
        movies = {}
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            for line in file:
                movie_id, title = map(str.strip, line.split(","))
                movies[int(movie_id)] = Movie(int(movie_id), title)
        return movies

    def load_watch_history(self, file_path):
        watch_history = []
        with open(file_path, 'r') as file:
            for line in file:
                watch_history.append(line.strip())
        return watch_history

    def recommend_movie(self, user_movies):
        user_movie_set = set(user_movies)

        eligible_users = []
        for history in self.watch_history:
            history_movies = set(map(int, history.split(",")))
            if len(history_movies.intersection(user_movie_set)) >= len(user_movie_set) / 2:
                eligible_users.append(history_movies)

        if not eligible_users:
            return "Нет рекомендаций"

        watched_movies = set(user_movies)
        recommendation_count = {}
        for user_history in eligible_users:
            for movie_id in user_history - watched_movies:
                recommendation_count[movie_id] = recommendation_count.get(movie_id, 0) + 1

        if not recommendation_count:
            return "Нет рекомендаций"

        max_recommendation_count = max(recommendation_count.values())
        recommended_movies = [movie_id for movie_id, count in recommendation_count.items() if count == max_recommendation_count]
        recommended_movie_id = random.choice(recommended_movies)
        recommended_movie = self.movies.get(recommended_movie_id)

        return recommended_movie.title if recommended_movie else "Нет рекомендаций"

def main():
    MOVIES_FILE = "movies.txt"
    WATCH_HISTORY_FILE = "watch_history.txt"

    system = MovieRecommendationSystem(MOVIES_FILE, WATCH_HISTORY_FILE)

    user_movies = input("Введите идентификаторы фильмов, которые вы уже посмотрели (через запятую): ").split(",")
    recommendation = system.recommend_movie(map(int, user_movies))

    print(recommendation)

if __name__ == "__main__":
    main()
