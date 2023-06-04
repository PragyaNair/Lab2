"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
         'name': 'Pragya Nair',
        'student ID': 10291386,
        'pizza topping': [
            'Onion',
            'Tomato',
            'Green pepper'
        ],
        'movies': [
            # Change this to a movie you like
            {
                'title': 'Fractured',
                'genre': 'sci-fi'
            },
            {
               'title': 'Fast and Furious 10',
                'genre': 'adventure'  
            }
            
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # Change to pizza toppings you like
    add_pizza_toppings(about_me, ['mushroom', 'black olives'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # Change to a movie you like
    add_movie(about_me, 'Fall', 'Thriller')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    #Complete function body per Step 3
    full_name = my_info['name']
    first_name = full_name.split()[0]
    student_id = my_info['student ID']
    # Print sentence containing name
    print(f"Hi my name is {full_name}, but you can call me {first_name}.")
    # Print sentence containing student ID
    print(f"Student ID number is: {student_id}.")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    #  Complete function body per Step 4
    print("\nMy favorite pizza toppings are:")
    for pizza_topping in my_info['pizza topping']:
        print(f'- {pizza_topping}')

    # Print header "My favourite pizza toppings are:"  ####
    # Print bullet list of favourite pizza toppings
    print()

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # Complete function body per Step 5
    my_info['pizza topping'].extend(list(toppings))

    for i, pizza_topping in enumerate(my_info['pizza topping']):
        my_info['pizza topping'][i] = pizza_topping.lower() 

    my_info['pizza topping'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # Complete function body per Step 6
    new_movie = {
        'title': title,
        'genre': genre
    }
    my_info['movies'].append(new_movie)
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    #Complete function body per Step 7
    genre_names = [new_movie['genre'] for new_movie in my_info['movies']]
    all_genre = ', '.join(genre_names)
    print(f"\nI love watching {all_genre} movies.")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    #Complete function body per Step 8
    title_names = [new_movie['title'] for new_movie in movie_list]
    all_movie = ', '.join(title_names)
    print(f"\nSome of my favorite movies are {all_movie}!")

if __name__ == '__main__':
    main()