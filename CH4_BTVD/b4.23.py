import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')

print("Movies DataFrame:")
print(movies.head())

print("\nRatings DataFrame:")
print(ratings.head())

print("\nTags DataFrame:")
print(tags.head())

#Kiểm tra dữ liệu thiếu trong từng DataFrame:
print("\nMissing values in movies:")
print(movies.isnull().sum())

print("\nMissing values in ratings:")
print(ratings.isnull().sum())

print("\nMissing values in tags:")
print(tags.isnull().sum())

#Xử lý dữ liệu thiếu (ví dụ: loại bỏ các dòng có giá trị thiếu):
movies.dropna(inplace=True)
ratings.dropna(inplace=True)
tags.dropna(inplace=True)

#Lọc các bộ phim không có tên (title) hoặc ID không hợp lệ trong movies:
movies = movies[movies['title'].notnull()]

#Lọc các đánh giá không hợp lệ trong ratings (giữ lại chỉ những đánh giá hợp lệ):
ratings = ratings[(ratings['rating'] >= 0) & (ratings['rating'] <= 5)]

#Gộp movies và ratings theo cột 'movieId':
movie_ratings = pd.merge(ratings, movies, on='movieId')

#Hiển thị 5 dòng đầu của DataFrame đã gộp:
print("\nMerged DataFrame (movie_ratings):")
print(movie_ratings.head())


#Tính trung bình đánh giá cho mỗi bộ phim:
avg_ratings = movie_ratings.groupby('title')['rating'].mean()

#Lọc các bộ phim có đánh giá trung bình lớn hơn 4:
high_rated_movies = avg_ratings[avg_ratings > 4]

#Hiển thị các bộ phim có đánh giá cao:
print("\nHigh rated movies (rating > 4):")
print(high_rated_movies)


#Thống kê số lượng đánh giá theo bộ phim:
rating_counts = movie_ratings.groupby('title')['rating'].count()

#Thống kê đánh giá trung bình của các bộ phim:
average_ratings = movie_ratings.groupby('title')['rating'].mean()

print("\nRating counts for each movie:")
print(rating_counts.head())

print("\nAverage ratings for each movie:")
print(average_ratings.head())


#Chuyển cột timestamp sang định dạng thời gian:
ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')

#Hiển thị 5 dòng đầu sau khi chuyển đổi:
print("\nRatings DataFrame with parsed timestamps:")
print(ratings.head())


###TRỰC QUAN HOÁ DỮ LIỆU:

import matplotlib.pyplot as plt
import seaborn as sns

#Vẽ histogram về phân bố đánh giá của các bộ phim:
plt.figure(figsize=(10, 6))
sns.histplot(ratings['rating'], bins=20, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

#Vẽ biểu đồ về số lượng đánh giá của các bộ phim:
plt.figure(figsize=(10, 6))
rating_counts.head(10).plot(kind='bar')
plt.title('Top 10 Movies by Number of Ratings')
plt.xlabel('Movie')
plt.ylabel('Number of Ratings')
plt.xticks(rotation=90)
plt.show()