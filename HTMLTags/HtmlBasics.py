from Utils.Consts import NEW_LINE, TAB_LINE
from NexpyBase.NexpyNode import NexpyNode

class HtmlBasics(NexpyNode):


	def html5template(self, title: str = 'en', lang: str = 'Document') -> NexpyNode:
    
		html5templateElement = NexpyNode().indexTemplate(lang=lang, title=title)
		return html5templateElement


	def p(self, className: str = '',id: str = '', content='') -> NexpyNode:
		
		pElement = NexpyNode({
			'openTag': f"<p class=\"{className}\" id=\"{id}\">{NEW_LINE}",
			'content': [content],
			'closeTag': f"</p>{NEW_LINE}"
		})

		return pElement


	def meta(self, name: str = '', content_flag: str='', content: str='', charset: str = '') -> NexpyNode:

		metaElement = NexpyNode({
			'openTag': f"<meta name=\"{name}\" content=\"{content_flag}\" charset=\"{charset}\">",
			'content': [content],
			'closeTag': f"</meta>{NEW_LINE}"
		})

		return metaElement		