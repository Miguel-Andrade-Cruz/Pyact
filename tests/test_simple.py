import unittest

from Pyact.HTMLTags.HtmlBasics import HtmlBasics
from Pyact.HTMLTags.Inputs import Inputs
from Pyact.HTMLTags.Semantics import Semantics

class TestSimple(unittest.TestCase):
    def test_components(self):
        

        app = Semantics().div().inside(
            Inputs().button().inside(
                HtmlBasics().p(content='Click me')
            )
        ).mount()
        self.assertTrue(app, """<div>
<button>Click me</button>
</div>
"""
        )

    def test_htmltemplate(self):
        app = HtmlBasics().html5template(title='Login page')

        app.inside(
            Inputs().button(content='Click me')
        ).mount()

        self.assertTrue(app, """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body>
<button>Click me</button>
</body>
</html>
"""
        )

if __name__ == '__main__':
    unittest.main()