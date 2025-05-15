from Utils.Consts import NEW_LINE, TAB_LINE
from NexpyBase.NexpyNode import NexpyNode

class Semantics(NexpyNode):

    def div(self, className='', id='', content='') -> NexpyNode:
        
        divElement = NexpyNode({
            'openTag': f"<div class=\"{className}\" id=\"{id}\">{NEW_LINE + TAB_LINE}",
            'content': [content],
            'closeTag': f"</div>{NEW_LINE}"
        })

        return divElement