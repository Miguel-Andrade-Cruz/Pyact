from Nexpy.HtmlBasics import HtmlBasics
from Nexpy.Semantics import Semantics
from Nexpy.Inputs import Inputs

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

	return container.mount()


def app():
	html = HtmlBasics().html5template(
		doctype='html', lang='pt-br'
	).inside(
		containerForm()
	)

	return html.mount()

print(app())