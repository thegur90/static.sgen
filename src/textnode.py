from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal"
    BOLD_TEXT = "Bold"
    ITALIC_TEXT = "Italic"
    LINK = "Link"
    IMAGE = "Image"


class TextNode():

    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.url == other.url:
            if self.text_type == other.text_type:
                return (self.text == other.text)
        return False
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")