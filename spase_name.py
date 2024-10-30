calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    return tuple((len(string), string.upper(), string.lower()))


def is_contains(string: str, list_tp_search: list):
    count_calls()
    for i in list_tp_search:
        if i.lower() == string.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)