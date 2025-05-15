from typing import Self
from NexpyBase.NexpyComponent import Component

class NexpyNode():
    
    
    def __init__(self, base: dict = {'openTag': '', 'content': [], 'closeTag': ''}) -> None:
        self.composite = Component(base)

    
    def inside(self, inner: str | Self) -> Self:
        if isinstance(inner, NexpyNode):
            self.composite.inside(inner.composite)
        
        elif type(inner) == str:
            self.composite.inside(inner)
        
        return self


    def mount(self) -> str:
        return self.composite.mount()