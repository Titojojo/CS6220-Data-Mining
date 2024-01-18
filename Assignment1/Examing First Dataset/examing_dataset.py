import os
from collections import defaultdict


def process_data(directory_path):
    """
    Process movie ratiing data and store parsed data in user_dataset
    user_dataset is a hashmap, key: user id, value: list of (movie id, rating) pairs
    Meanwhile, calculate the count of records and the range of year
    """
    # Initialization
    movie_id, movie_count = 0, 0
    min_year, max_year = float('inf'), float('-inf')
    user_dataset = defaultdict(list)

    for filename in os.listdir(directory_path):
        full_path = os.path.join(directory_path, filename)
        with open(full_path, 'r') as file:
            for line in file:
                # Meet a new movie id, update movie id
                if ':' in line:
                    movie_id += 1
                    continue
                # Meet a piece of movie rating record, parse data
                items = line.strip().split(',')
                customer_id, rating, year = int(items[0]), int(items[1]), int(items[2].split('-')[0])
                # Add customer id, (movie id, rating) pair to dataset
                user_dataset[customer_id].append((movie_id, rating))
                # Update record count
                record_count += 1
                # Update lower and upper boundaries of year range
                min_year, max_year = min(min_year, year), max(max_year, year)

    return (record_count, min_year, max_year, user_dataset)


def process_movies(filename):
    """
    Process movie titles data and store parsed data in dataset
    movie_dataset is a hashmap, key: title, value: list of movie ids
    movie_map is a hashmap, key: movie id, value: title
    """
    movie_dataset = defaultdict(list)
    movie_map = {}
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            # Split the line into 3 parts to account for titles that contain commas 
            movie_id, year, title = line.strip().split(',', 2)
            movie_dataset[title.strip()].append(int(movie_id.strip()))
            movie_map[int(movie_id.strip())] = title.strip()

    return (movie_dataset, movie_map)


# Process combined_data_*.txt and movie_titles.csv files
movie_count, min_year, max_year, user_dataset = process_data("netflix_data/combined_data")
movie_dataset, movie_map = process_movies("netflix_data/movie_titles.csv")


# Count number of movie names that refer to 4 different movies.
count = 0
for movie in movie_dataset:
    if len(movie_dataset[movie]) == 4:
        count += 1

# Count number of users rated exactly 200 movies.
# Get the lowest user id.
user_count, min_user_id = 0, float('inf')
for user in user_dataset:
    if len(user_dataset[user]) == 200:
        user_count += 1
        min_user_id = min(min_user_id, user)

# Get the 5-star rating movies of the user
most_liked_movies = []
for record in user_dataset[min_user_id]:
    if record[1] == 5:
        most_liked_movies.append(movie_map[record[0]])


# Question 3
print("Total records of movie ratings in the entire dataset is:", movie_count)
print("Total unique users in the entire dataset is:", len(user_dataset))
print("The range of years that this data is valid over", min_year, "to", max_year)

# Question 4
print("There are", len(movie_dataset), "movies with unique names.")
print(count, "movie names refer to four different movies.")

# Question 5
print(user_count, "users rated exactly 200 movies.")
for movie in most_liked_movies:
    print(movie)