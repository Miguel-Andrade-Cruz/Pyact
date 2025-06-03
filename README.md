# Pyact
A way to python code html pages

Pyact was intended to make server rendering pages easier, allowing you to create
components to make it modular and more fluid to use, just like react does.

# How to use it?
After importing the libraries, you just need to instatiate an object and use the `inside` method to insert another elements, just like below:
```
import Pyact.Inputs as ipt
from Pyact.HtmlBasics import hlb
from Pyact.Semantics import smt

def Button(content=''):
    button = ipt.input(type=button)

    button.inside(
        hlb.p(content=content)
    )

    return button
def loginPage():
    div = div(
    ).inside(
        hlb.p(content='Enter your email')
        
    ).inside(
        ipt.input(type=text)
        
    ).inside(
        hlb.p(content='Enter your password')

    ).inside(
        ipt.input()

    ).inside(
        Button('Login')
    
    ).inside(
        Button('Forgot password?')
    )

    return loginPage


def app():
    app = hlb.html5template(

    ).inside(
        loginPage
    )

    return app()
```

As you can see from above, Pyact allows you to create separate modules and attach them easely by just returning
the NexpyNode object and calling the function on the `inside` method.

and when constructing the app, you can make the same formula, or return the html string directly with `mount` method.

