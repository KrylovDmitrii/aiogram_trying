from typing import List, Any


def custom_filter(array: List[Any]) -> bool:
    return sum([item for item in array if isinstance(item, int) and item % 7 == 0]) <= 83


anonymous_filter = lambda message_string: len([letter for letter in message_string if letter == 'я']) >= 23

print(anonymous_filter('Я - последняя буква в алфавите!'))
