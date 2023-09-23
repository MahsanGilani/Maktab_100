"""
    class Indenter :
        contex manager
        methods : constructor, enter, exit, indent, print

"""
class Indentor:
    def __init__(self):
        self.indent = -1
    
    def __enter__(self):
        self.indent += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.indent -= 1
        # exit()
        # print(exc_type, exc_value)    
        
    # def indent_func(self):
        
        
    def print_txt(self, text):
        fasele = "    " * self.indent
        print(f"{fasele}{text}")
        

with Indentor() as indent:
    indent.print_txt("Hi")
    with indent:
        indent.print_txt("talk is cheap!")
        with indent:
            indent.print_txt("show me the code")
    indent.print_txt("torvalds")