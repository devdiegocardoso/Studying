# pylint: disable=missing-docstring
from dataclasses import dataclass

@dataclass
class Node:
    _name: str

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, __value: object) -> bool:
        return __value == self._name if isinstance(__value,Node) else False

    def __repr__(self) -> str:
        return str(self._name)

    def is_my_goal(self, goal):
        return self._name == goal

    @property
    def name(self):
        return self._name
