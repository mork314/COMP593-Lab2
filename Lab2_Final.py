def main():

    
    about_me = {'full_name': 'Mark Noble', 
                'student_id': 10292665, 
                'pizza_toppings': ['CHEESE', 'PEPPERONI', 'BACON'], 
                'movies': [
                {'title': 'The Lord of the Rings: The Two Towers', 'genre': 'Fantasy'}, 
                {'title': 'G-Force', 'genre':'Action'}
                ]
                }

    about_me['movies'].append({'title': 'Star Wars Episode VI: Return of the Jedi', 'genre': 'Action'})
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('PEPPERS', 'SAUSAGE'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    student_id = about_me['student_id']
    full_name_split = full_name.split(' ')
    first_name = full_name_split[0]
    print(f'My name is {full_name}, but you can call me Sir {first_name}')
    print(f'My student ID is {student_id}')
    return
    
def add_pizza_toppings(about_me, toppings):
    for topping in toppings:
           about_me['pizza_toppings'].append(topping)
    about_me['pizza_toppings'].sort()
    for i in range(len(about_me['pizza_toppings'])):
        about_me['pizza_toppings'][i] = about_me['pizza_toppings'][i].lower()
    return

def print_pizza_toppings(about_me):
    print('My favourite pizza toppings are:')
    for topping in about_me['pizza_toppings']:
        print(f'-{topping}')
    return

def print_movie_genres(about_me):
    movie_list = about_me['movies']
    genre_list = []
    for movie in movie_list:
        genre_list.append(movie['genre'])
    thing_to_print ='I like to watch '
    #adds each genre in the list to the string, and adds an 'and' in front
    #if it's the last value in the list
    for i in range(len(genre_list)):
        if i != len(genre_list)-1:
            thing_to_print += f'{genre_list[i]}, '
        else:
            thing_to_print += f'and {genre_list[i]} '
    thing_to_print += 'movies'
    print(thing_to_print)
    return 

def print_movie_titles(movie_list):
    title_list = []
    for movie in movie_list:
        title_list.append(movie['title'].title())
    thing_to_print ='Some of my favourite movies are '
    #adds each title in the list to the string, and adds an 'and' in front
    #if it's the last value in the list
    for i in range(len(title_list)):
        if i != len(title_list)-1:
            thing_to_print += f'{title_list[i]}, '
        else:
            thing_to_print += f'and {title_list[i]}'
    thing_to_print += '!'
    print(thing_to_print)
    return
    
if __name__ == '__main__':
    main()