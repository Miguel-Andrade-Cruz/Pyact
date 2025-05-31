from typing import Self

class Component:


    def __init__(self, base: dict) -> None:
        self.openTag = base['openTag']
        self.content = base['content']
        self.closeTag = base['closeTag']

    def indexTemplate(lang: str, title: str) -> Self:
        template_open = f"""
<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
"""
        template_close = """
</body>
</html>
"""

        main_component = Component({'openTag': template_open, 'content': [], 'closeTag': template_close})
        return main_component


    def inside(self, inner: str | Self) -> None:
            self.content.append(inner)


    def mount(self) -> str:
        html = self.openTag

        for item in self.content:
            if isinstance(item, Component):
                html += item.mount()
            elif type(item) == str:
                html += item

        html += self.closeTag

        return html