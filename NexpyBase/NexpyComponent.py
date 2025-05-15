from typing import Self

class Component:


    def __init__(self, base: dict) -> None:
        self.openTag = base['openTag']
        self.content = base['content']
        self.closeTag = base['closeTag']


    def inside(self, inner: str | Self) -> None:
        self.content.append(inner)


    def mount(self) -> str:
        html = self.openTag

        for item in self.content:
            if isinstance(item, Component):
                html += item.mount()
            elif type(item) == str:
                html += item

        html += self.closeTag

        return html