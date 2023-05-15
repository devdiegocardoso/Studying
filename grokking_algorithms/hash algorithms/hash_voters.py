# pylint: disable=missing-docstring

voted = {}

def check_voter(name):
    if voted.get(name):
        print(f"You cannot vote, {name}.")
    else:
        voted[name] = True
        print(f"You can vote, {name}.")

check_voter("tom")
check_voter("mike")
check_voter("tom")
