from ..utils.Consts import NEW_LINE, TAB_LINE
from ..PyactBase.PyactNode import PyactNode


class Inputs(PyactNode):


    def form(self, action = '#', method = 'post') -> PyactNode:
        
        formElement = PyactNode({
            'openTag': f"<form method=\"{method}\" action=\"{action}\">{NEW_LINE}",
            'content': [],
            'closeTag': f"</form>{NEW_LINE}"
        })

        return formElement


    def input(self, type='', className = '', id='', placeholder='', content='') -> PyactNode:
        
        inputElement = PyactNode({
            'openTag': f"<input class=\"{className}\" id=\"{id}\" placeholder=\"{placeholder}\">{NEW_LINE}",
            'content': [content],
            'closeTag': f"</input>{NEW_LINE}"
        })

        return inputElement


    def button(self, type='', className = '', id='', content='') -> PyactNode:
        
        buttonElement = PyactNode({
            'openTag': f"<button class=\"{className}\" id=\"{id}\" type=\"{type}\">{NEW_LINE}",
            'content': [content],
            'closeTag': f"</button>{NEW_LINE}"
        })

        return buttonElement

