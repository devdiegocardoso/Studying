# pylint: disable=missing-docstring

def find_biggest_block(height,width):
    return height - (height - width) if height > width else width - (width - height)

def divide_block(height,width):
    biggest_block = find_biggest_block(height,width)
    return (height-biggest_block, width) if height > width else (height, width - biggest_block)

def recursive_block(height,width):
    if height % width == 0 or width % height == 0:
        return min(height, width)
    return recursive_block(*divide_block(height,width))
