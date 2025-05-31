from ..utils.Consts import NEW_LINE, TAB_LINE
from ..PyactBase.PyactNode import PyactNode

class Semantics(PyactNode):

    def div(self, className='', id='', content='') -> PyactNode:
        
        divElement = PyactNode({
            'openTag': f"<div class=\"{className}\" id=\"{id}\">{NEW_LINE}",
            'content': [content],
            'closeTag': f"</div>{NEW_LINE}"
        })

        return divElement