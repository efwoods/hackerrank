"""A module for testing pdb on the function process_cities."""

def process_cities(filename):
    """reads a file of countries and cities, separated by a comma and 
    prints them out as "capital, country".

    Args:
        filename (csv): The name of the csv file containing the list of 
        countries and their capitals.
    
    Returns:
        None.
    """

    with open(filename, encoding='utf-8', mode='rt') as file:
        for line in file:
            line = line.strip() # strip the whitespace
            if 'quit' in line.lower():
                return
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')

if __name__ == '__main__':
    import sys
    process_cities(sys.argv[1])
