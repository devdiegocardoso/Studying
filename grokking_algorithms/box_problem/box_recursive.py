# pylint: disable=missing-docstring

from box import Box

def recursive_search(main_box,value):
    found = False
    for element in main_box.retrieve_all_items():
        if isinstance(element,Box):
            found = recursive_search(element,value)
            if found:
                break
        elif element.upper() == value.upper():
            return True
    return found
