import unittest

from textnode import TextNode, TextType
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = HTMLNode("Test HTML node","42069",["1","1"],{"href": "https://www.google.com","target": "_blank",})
        node4 = LeafNode("Test HTML node","42069",["1","1"],{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)
        
        print (repr(node3))
        print (repr(node4))


if __name__ == "__main__":
    unittest.main()