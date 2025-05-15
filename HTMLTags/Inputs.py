from Utils.Consts import NEW_LINE, TAB_LINE
from NexpyBase.NexpyNode import NexpyNode


class Inputs(NexpyNode):


    def form(self, action = '#', method = 'post') -> NexpyNode:
        
        formElement = NexpyNode({
            'openTag': f"<form method=\"{method}\" action=\"{action}\">{NEW_LINE + TAB_LINE}",
            'content': [],
            'closeTag': f"</form>{NEW_LINE}"
        })

        return formElement


    def input(self, type, className = '', id='', placeholder='', content='') -> NexpyNode:
        
        inputElement = NexpyNode({
            'openTag': f"<input class=\"{className}\" id=\"{id}\" placeholder=\"{placeholder}\">{NEW_LINE + TAB_LINE}",
            'content': [content],
            'closeTag': f"</input>{NEW_LINE}"
        })

        return inputElement


    def button(self, type, className = '', id='', content='') -> NexpyNode:
        
        buttonElement = NexpyNode({
            'openTag': f"<button class=\"{className}\" id=\"{id}\" type=\"{type}\">{NEW_LINE + TAB_LINE}",
            'content': [content],
            'closeTag': f"</button>{NEW_LINE}"
        })

        return buttonElement

