from collections.abc import Callable
from typing import Self
from .PyactComponent import Component
from ..utils.Consts import TAB_LINE


class PyactNode():
    def __init__(self, base: dict = {'openTag': '', 'content': [], 'closeTag': ''}) -> None:
        
        self.composite = Component(base)
        return
    
    def nodeTagBase(tag:str, singleTag:bool = False) -> Callable:
        
        def nodeSingleTag(**flags) -> PyactNode:
            node = PyactNode({
                'openTag': f"<{tag}{PyactNode.concatFlags(flags=flags)}>",
                'content': [],
                'closeTag': ''
            })
            return node
        
        def nodeTag(content:str = '', **flags) -> PyactNode:
            node = PyactNode({
                'openTag': f"<{tag}{PyactNode.concatFlags(flags=flags)}>",
                'content': [f'{TAB_LINE}{content}'],
                'closeTag': f"</{tag}>"
            })
            return node
        
        if singleTag:
            return nodeSingleTag
        else:
            return nodeTag


    def concatFlags(flags:dict) -> str:
        string_flags:str = ""
        for key, value in flags.items():
            if key == 'className':
                string_flags += f" class={value}"
            string_flags += f" {key}={value}"

        return string_flags


    def indexTemplate(lang: str, title: str) -> Self:
        
        index_html = PyactNode()
        index_html.composite = Component.indexTemplate(lang=lang, title=title)
        return index_html

    
    def inside(self, inner: str | Self) -> Self:
        
        if isinstance(inner, PyactNode):
            self.composite.inside(inner.composite)
        
        elif type(inner) == str:
            self.composite.inside(inner)
        
        return self


    def mount(self) -> str:
        return self.composite.mount()