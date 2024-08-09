calls = 0


def calls_count():
    global calls
    calls += 1


def string_info(string):
    calls_count()
    return (len(string), string.upper(), string.lower())



def is_contains(string, list_to_search):
    calls_count()
    new_list = [x.upper() for x in list_to_search]
    if string.upper() in new_list:
        return (True)
    else:
        return (False)




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)