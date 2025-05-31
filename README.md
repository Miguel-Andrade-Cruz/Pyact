# Pyact
A way to python code html pages

Pyact was intended to make server rendering pages easier, allowing you to create
components to make it modular and more fluid to use, just like react does.

# How to use it?
After importing the libraries, you just need to instatiate an object and use the `inside` method to insert another elements, just like below:
```
from Pyact.Inputs import Inputs
from Pyact.HtmlBasics import HtmlBasics
from Pyact.Semantics import Semantics

def button(content=''):
    button = Inputs()

    button.inside(
        HtmlBasics().p(content=content)
    )

    return button
def loginPage():
    div = Semantics.div(

    ).inside(
        HtmlBaiscs().p(content='Enter your email')
        
    ).inside(
        Inputs().input()
        
    ).inside(
        HtmlBaiscs().p(content='Enter your password')

    ).inside(
        Inputs().input()

    ).inside(
        button('Login')
    
    ).inside(
        button('Forgot password?')
    )

    return loginPage


def app():
    app = HtmlBasics().html5template(

    ).inside(
        loginPage
    )

    return app.mount()
```

As you can see from above, Pyact allows you to create separate modules and attach them easely by just returning
the NexpyNode object and calling the function on the `inside` method.

and when constructing the app, you can make the same formula, or return the html string directly with `mount` method.

