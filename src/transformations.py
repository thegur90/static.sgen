from enum import Enum
from textnode import *
from htmlnode import *


def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i",text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img","",props={"src": text_node.url,"alt": text_node.text })
    raise Exception("How did we get here? invalid Enum value?")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes: 
        if True: pass




    return new_nodes