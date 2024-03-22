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

    for line in data:
        name, species = line.rstrip().split("|")[:2]

        if search_string in ("All", species):
            villagers.append(name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    villagers_fitness = []
    villagers_nature = []
    villagers_education = []
    villagers_music = []
    villagers_fashion = []
    villagers_play = []

    data = open(filename)

    # one list, within the list, multiple lists of the villagers based on hobby
    # we need to look at the each line in the data file 
    # we need to look at the hobby in position [3]
    # if this hobby is present in position [3]:
    # if, elif, and else statements here 
    # then append the name to that hobby list 

    for line in data: 
        hobby = line.rstrip().split("|")[3]
        name = line.rstrip().split("|")[0]
        
        if hobby == 'Fitness':
            villagers_fitness.append(name)
    
        elif hobby == 'Nature':
            villagers_nature.append(name)
    
        elif hobby == 'Education':
            villagers_education.append(name)
            
        elif hobby == 'Music':
            villagers_music.append(name)
            
        elif hobby == 'Fashion':
            villagers_fashion.append(name)
            
        elif hobby == 'Play':
            villagers_play.append(name)
                 
    return [sorted(villagers_fitness),
            sorted(villagers_nature),
            sorted(villagers_education),
            sorted(villagers_music),
            sorted(villagers_fashion),
            sorted(villagers_play)
    ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).
    Arguments:
        - filename (str): the path to a data file
    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """   

    all_villagers_info = []
    
    data = open(filename)

    for line in data:
        name = line.rstrip().split('|')[0]
        species = line.rstrip().split('|')[1]
        personality = line.rstrip().split('|')[2]
        hobby = line.rstrip().split('|')[3] 
        motto = line.rstrip().split('|')[4] 
        
        all_villagers_info.append(tuple([name, species, personality, hobby, motto]))
        
    return all_villagers_info


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    data = open(filename)
    
    for line in data:
            name = line.rstrip().split("|")[0]
            motto = line.rstrip().split("|")[4]

            if villager_name == name:
                return motto


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    likeminded = set()

    target_personality = None
    for villager_data in all_data(filename):
        name, _, personality = villager_data[:3]

        if name == villager_name:
            target_personality = personality
            break

    if target_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[:3]
            if personality == target_personality:
                likeminded.add(name)

    return likeminded