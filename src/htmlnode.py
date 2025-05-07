

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

        pass

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return_string = ""
        for entry in self.props:
            return_string += f" {entry}=\"{self.props[entry]}\""
        return return_string
    
    def __repr__(self):
        return_string = ""
        return_string += ("=========HTMLNode Status=========") + "\n"
        return_string += ("") + "\n"
        return_string += (f"tag = {self.tag}") + "\n"
        return_string += (f"value = {self.value}") + "\n"
        if self.children != None:
            return_string += (f"children = {self.children}") + "\n"
        if self.props != None:
            return_string += (f"props = {self.props}") + "\n"
        return_string += ("") + "\n"
        return_string += ("=================================") + "\n"
        return return_string

class LeafNode(HTMLNode):

    def __init__(self,tag,value,children,props):
        super().__init__(tag,value,children,props)
        self.children = []
    
    def to_html(self):
        if self.value == None:
            raise ValueError ("all leaf nodes must have a value")
        if self.tag == None: return self.value
        return super().to_html()
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def __repr__(self):
        return super().__repr__()
        

