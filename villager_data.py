"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()

    data = open(filename)
    
    for line in data: 
        species = line.rstrip().split("|")[1]
        unique_species.add(species)
    
    return sorted(unique_species)

# for line in data:
#     data_no_whitespace = line.rstrip()
#     print("the data with no whitespace")
#     print(data_no_whitespace)
#     list_of_items_from_line = data_no_whitespace.split('|')
#     print("the list made from the line of data")
#     print(list_of_items_from_line)
#     species = list_of_items_from_line[1]

print(all_species('villagers.csv'))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    data = open(filename)

    # we need to have a condition to get all the villagers based on species 
    # stripping and spliting 
    # append the list of names of the villagers to "villagers" 

    if search_string == "All":
        for line in data: 
            name = line.rstrip().split("|")[0]
            villagers.append(name)
    else: 
        for line in data: 
            name = line.rstrip().split("|")[0]
            species = line.rstrip().split("|")[1]
            if species == search_string:
                villagers.append(name)
            
    return sorted(villagers)

print(get_villagers_by_species('villagers.csv', "Bear"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    Villagers_Fitness = []
    Villagers_Nature = []
    Villagers_Education = []
    Villagers_Music = []
    Villagers_Fashion = []
    Villagers_Play = []

    data = open(filename)

    # one list, within the list, multiple lists of the villagers based on hobby
    # we need to look at the each line in the data file 
    # we need to look at the hobby in position [3]
    # if this hobby is present in position [3]:
    # if, elif, and else statements here 
    # then append the name to that hobby list 

    Villagers_Fitness.insert(0, "Fitness: ")
    Villagers_Nature.insert(0, "Nature: ")
    Villagers_Education.insert(0, "Education: ")
    Villagers_Music.insert(0, "Music: ")
    Villagers_Fashion.insert(0, "Fashion: ")
    Villagers_Play.insert(0, "Play: ")

    for line in data: 
        hobby = line.rstrip().split("|")[3]
        name = line.rstrip().split("|")[0]
        
        if hobby == 'Fitness':
            Villagers_Fitness.append(name)
    
        elif hobby == 'Nature':
            Villagers_Nature.append(name)
    
        elif hobby == 'Education':
            Villagers_Education.append(name)
            
        elif hobby == 'Music':
            Villagers_Music.append(name)
            
        elif hobby == 'Fashion':
            Villagers_Fashion.append(name)
            
        elif hobby == 'Play':
            Villagers_Play.append(name)

    All_Villagers = [Villagers_Fitness, Villagers_Nature, Villagers_Education, Villagers_Music, Villagers_Fashion, Villagers_Play]
                 
    return sorted([All_Villagers])

print(all_names_by_hobby('villagers.csv'))


# def all_data(filename):
#     """Return all the data in a file.

#     Each line in the file is a tuple of (name, species, personality, hobby,
#     saying).

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[tuple[str]]: a list of tuples containing strings
#     """

#     all_data = []

#     # TODO: replace this with your code

#     return all_data


# def find_motto(filename, villager_name):
#     """Return the villager's motto.

#     Return None if you're not able to find a villager with the
#     given name.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name

#     Return:
#         - str: the villager's motto or None
#     """

#     # TODO: replace this with your code


# def find_likeminded_villagers(filename, villager_name):
#     """Return a set of villagers with the same personality as the given villager.

#     Arguments:
#         - filename (str): the path to a data file
#         - villager_name (str): a villager's name
    
#     Return:
#         - set[str]: a set of names

#     For example:
#         >>> find_likeminded_villagers('villagers.csv', 'Wendy')
#         {'Bella', ..., 'Carmen'}
#     """

#     # TODO: replace this with your code
