# pylint: disable=missing-docstring
class Box:
    def __init__(self,label) -> None:
        self.items = []
        self.label = label
    def add_item(self,item):
        self.items.append(item)
    def __repr__(self) -> str:
        data = f"{self.label}:"
        return f"[{data} {','.join([str(x) for x in self.items])}]"
    def retrieve_all_items(self):
        return self.items
    