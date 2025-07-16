from .PyactNode import PyactNode
from typing import Callable
from ..utils.Consts import HTML5_OPEN, HTML5_CLOSE

def concat_flags(flags: dict) -> str:
    string_flags: str = ""
    for key, value in flags.items():
        if key == "className":
            string_flags += f" class={value}"
        string_flags += f" {key}={value}"

    return string_flags



def index_template_factory() -> Callable:

    def index_template(lang:str, title:str, inside:list) -> PyactNode:
        
        html5_open_replaced = HTML5_OPEN\
            .replace('{%title%}', title)\
            .replace('{%lang%}', lang)

        node = PyactNode(
            open_tag=html5_open_replaced,
            inside=inside,
            close_tag=HTML5_CLOSE
        )
        return node

    return index_template

def node_tag_base(tag: str, singleTag: bool = False) -> Callable:

    def node_single_tag(**flags) -> PyactNode:
        node = PyactNode(
            open_tag=f"<{tag}{concat_flags(flags=flags)}>",
            single_tag=True
        )
        return node

    def node_tag(inside: list = [""], **flags) -> PyactNode:
        node = PyactNode(
            open_tag=f"<{tag}{concat_flags(flags=flags)}>",
            inside=inside,
            close_tag=f"</{tag}>",
        )
        return node

    if singleTag:
        return node_single_tag
    else:
        return node_tag
