# pylint: disable=missing-docstring

from box import Box

def linear_search(main_box,value):
    pile = [main_box]
    while pile:
        box = pile.pop(0)
        for element in box.retrieve_all_items():
            if isinstance(element,Box):
                pile.append(element)
            elif element.upper() == value.upper():
                return True
    return False
