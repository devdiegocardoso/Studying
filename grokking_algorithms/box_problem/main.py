# pylint: disable=missing-docstring
from box import Box
from box_linear import linear_search
from box_recursive import recursive_search

if __name__ == '__main__':
    box1 = Box("Box 1")
    box1.add_item("Dinheiro")
    box1.add_item("Lenco")
    box2 = Box("Box 2")
    box2.add_item("Carteira")
    box1.add_item(box2)
    box3 = Box("Box 3")
    box3.add_item("Cigarro")
    box3.add_item("Chave")
    box1.add_item(box3)
    box4 = Box("Box 4")
    box2.add_item(box4)
    box1.add_item("Jogo")
    box5 = Box("Box 5")
    box5.add_item("esmalte")
    box4.add_item(box5)
    box4.add_item("Chinelo")

    print(box1)
    print("Found" if linear_search(box1,"chaveiro") else "Not found")
    print("Found" if recursive_search(box1,"chinelo") else "Not found")
