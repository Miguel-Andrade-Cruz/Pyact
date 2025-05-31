from typing import Self
from .PyactComponent import Component

class PyactNode():
    
    
    def __init__(self, base: dict = {'openTag': '', 'content': [], 'closeTag': ''}) -> None:
        
        self.composite = Component(base)

    
    def indexTemplate(self, lang: str, title: str) -> Self:
        self.composite = Component.indexTemplate(lang=lang, title=title)
        return self

    
    def inside(self, inner: str | Self) -> Self:
        
        if isinstance(inner, PyactNode):
            self.composite.inside(inner.composite)
        
        elif type(inner) == str:
            self.composite.inside(inner)
        
        return self


    def mount(self) -> str:
        return self.composite.mount()