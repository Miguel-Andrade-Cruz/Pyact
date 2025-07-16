from ..PyactBase.PyactFactory import node_tag_base, index_template_factory

html5template = index_template_factory()

h1 = node_tag_base("h1")
h2 = node_tag_base("h2")
h3 = node_tag_base("h3")
h4 = node_tag_base("h4")
h5 = node_tag_base("h5")
h6 = node_tag_base("h6")

p = node_tag_base("p")

img = node_tag_base("img", singleTag=True)
