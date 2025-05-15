from Utils.Consts import NEW_LINE, TAB_LINE
from NexpyBase.NexpyNode import NexpyNode

class HtmlBasics(NexpyNode):

	def blank(self) -> NexpyNode:

		blankElement = NexpyNode()
		return blankElement


	def html5template(self, doctype: str, lang: str = 'en') -> NexpyNode:
    
		html5templateElement = self.blank(
		).inside(
			f"<! DOCTYPE {doctype}>"
		).inside(
			self.html(lang=lang
			)
			.inside(
				self.head(
				).inside(
					self.meta(charset='UTF-8')
				).inside(
					self.meta(name='viewport', content='width=device-width, initial-scale=1.0')
				)
			).inside(
				self.body()
			)
		)


		return html5templateElement


	def html(self, lang: str='en', content='') -> NexpyNode:

		htmlElement = NexpyNode({
			'openTag': f"<html lang=\"{lang}\">{NEW_LINE}",
			'content': [content],
			'closeTag': f"</html>{NEW_LINE}"
		})

		return htmlElement


	def head(self, content='') -> NexpyNode:
		
		headElement = NexpyNode({
			'openTag': f"<head>{NEW_LINE}",
			'content': [content],
			'closeTag': f"</head>{NEW_LINE}"
		})

		return headElement



	def body(self, className: str = '',id: str='', content='') -> NexpyNode:
		
		bodyElement = NexpyNode({
			'openTag': f"<body class=\"{className}\" id=\"{id}\">{NEW_LINE}",
			'content': [content],
			'closeTag': f"</body>{NEW_LINE}"
		})

		return bodyElement


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