import json

# write classes


def main():
    """ Read the movies from the file """
    movies = []
    with open('data\movies.json', 'r', encoding='utf-8') as f:
        movies_str = f.read()
        movies_json = json.loads(movies_str)
        for movie_json in movies_json:
            movie_title = movie_json['title']
            movie_year = movie_json['year']
            # Create a new movie object

            # set cast and genres
            
            if 'extract' in movie_json:
                movie_description = movie_json['extract']
                # set description to extract
                
            # append movie object to movies list
            
    print(len(movies))


if __name__ == 'main':
    main()