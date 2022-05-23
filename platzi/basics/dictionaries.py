def main():
    my_dictionary = {'key1': 1, 'key2': 2, 'key3': 3}
    print(my_dictionary['key1'])
    print(my_dictionary['key2'])
    print(my_dictionary['key3'])

    countries_poblation = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }
    print(countries_poblation['Argentina'])

    for country in countries_poblation.keys():
        print(country)

    for country in countries_poblation.values():
        print(country)

    for country, poblation in countries_poblation.items():
        print(f'{country} has {poblation} people')


if __name__ == '__main__':
    main()
