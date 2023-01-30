def main():

    
    about_me = {'full_name': 'Mark Noble', 'student_id': 10292665, 
    'pizza_toppings': ['CHEESE', 'PEPPERONI', 'BACON'], 'movies': [{
    'title': 'The Lord of the Rings: The Two Towers', 'genre': 'Action'}, 
    {'title': 'G-Force', 'genre':'Action'}]}

    #adds a movie to the 'movies' list in the dictionary
    about_me['movies'].append({'title': 'Star Wars Episode VI: Return of the Jedi'})
   
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    student_id = about_me['student_id']
    full_name_split = full_name.split(' ')
    first_name = full_name_split[0]
    print(f'My name is {full_name}, but you can call me Sir {first_name}')
    print(f'My student ID is {student_id}')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].append(toppings)
    
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()