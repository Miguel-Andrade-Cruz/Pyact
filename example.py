from HTMLTags.HtmlBasics import HtmlBasics
from HTMLTags.Semantics import Semantics
from HTMLTags.Inputs import Inputs

def loginForm():
    
	form = Inputs().form(
        action='/login', method='post'
    ).inside(
        inner=Inputs().input(
            type='text', placeholder='Digite seu email'
		)
	).inside(
        inner=Inputs().input(
			type='password', placeholder='Digite sua senha'
        )
	).inside(
        inner=Inputs().button(
            type='submit', content='Entrar'
		)
	)
    
	return form


def containerForm():

	container = Semantics().div(
		className='container'
	).inside(
		inner=loginForm()
	)

	return container


def app():
	html = HtmlBasics().html5template(
		doctype='html', lang='pt-br'
	).inside(
		of='body',
		inner=containerForm()
	)

	return html.mount()

print(app())