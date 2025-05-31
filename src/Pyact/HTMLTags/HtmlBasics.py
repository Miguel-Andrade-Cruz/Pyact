from ..utils.Consts import NEW_LINE
from ..PyactBase.PyactNode import PyactNode



class HtmlBasics(PyactNode):


	def html5template(self, title: str = 'en', lang: str = 'Document') -> PyactNode:
    
		html5templateElement =PyactNode().indexTemplate(lang=lang, title=title)
		return html5templateElement


	def p(self, className: str = '',id: str = '', content='') -> PyactNode:
		
		pElement =PyactNode({
			'openTag': f"<p class=\"{className}\" id=\"{id}\">{NEW_LINE}",
			'content': [content],
			'closeTag': f"</p>{NEW_LINE}"
		})

		return pElement
