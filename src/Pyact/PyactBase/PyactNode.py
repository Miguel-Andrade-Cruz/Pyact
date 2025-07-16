from ..utils.Consts import TAB_LINE, NEW_LINE


class PyactNode():
    def __init__(self, open_tag, close_tag = '', inside = [''], single_tag:bool = False) -> None:
        
        self.open_tag = open_tag
        self.inside = inside
        self.close_tag = close_tag
        self.single_tag = single_tag

        return



    def __call__(self) -> str:
        return self.mount()



    def mount(self, tab_count:int = 0) -> str:        

        html = TAB_LINE*tab_count + self.open_tag + NEW_LINE
        
        if self.single_tag:
            return html


        for item in self.inside:
            
            if isinstance(item, PyactNode):
                html += item.mount(tab_count + 1)
                
 
            elif type(item) is str:
                html += TAB_LINE*(tab_count+1) + item + NEW_LINE
        
        html += TAB_LINE*tab_count + self.close_tag + NEW_LINE

        return html
        