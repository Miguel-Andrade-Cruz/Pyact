from HTMLTags.HtmlBasics import HtmlBasics
from HTMLTags.Semantics import Semantics
from HTMLTags.Inputs import Inputs

def loginForm():
    
	form = Inputs().form(
        action='/login', method='post'
    ).inside(
        Inputs().input(
            type='text', placeholder='Digite seu email'
		)
	).inside(
        Inputs().input(
			type='password', placeholder='Digite sua senha'
        )
	).inside(
        Inputs().button(
            type='submit', content='Entrar'
		)
	)
    
	return form


def containerForm():

	container = Semantics().div(
		className='container'
	).inside(
		loginForm()
	)

	return container


def app():
	html = HtmlBasics().html5template(
		doctype='html', lang='pt-br'
	).inside(
		containerForm()
	)

	return html.mount()

print(app())