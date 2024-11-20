from abc import abstractmethod, ABC
from typing import List
class GUIComponent(ABC):

    @abstractmethod
    def render(self):
        pass


class Button(GUIComponent):

    def render(self):
        print("Rendering Button")


class Label(GUIComponent):

    def render(self):
        print("Rendering Label")

class Panel (GUIComponent):

    components: List[GUIComponent]

    def __init__(self):
        self.components = []

    def add(self, component: GUIComponent):
        self.components.append(component)

    def render(self):
        print("Rendering Panel")
        [component.render() for component in self.components]

def main():
    button1 = Button()

    label1 = Label()

    panel =   Panel()

    panel.add(button1)

    panel.add(label1)

    panel.render()

main()