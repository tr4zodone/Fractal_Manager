#!/usr/bin/python3

class Node:
    children = []
    siblings = []
    
    links = {}
    to_dos = {}

    description = ""
    size = 0

    def __init__(self, title, level=0):
        self.title = str(title)
        self.level = level

    def spawn(self, title, level=0):
        """creates a new, child node"""
        level = self.level + 1
        spawn = Node(title=title, level=level)
        self.children.append(spawn)
        self.size += 1

    def add_link(self, link, title):
        """adds a link resource"""
        self.links[title] = link

    def add_action(self, description, done=False):
        """adds a to-do item"""
        self.to_dos[description] = done

    def update_description(self, description):
        """updates node's description"""
        self.description = description

    def __repr__(self):
        """returns the node's name along with its level"""
        return "{}_{}".format(self.title, self.level)

    def __str__(self):
        return self.title

def siblinfgy(Node1, Node2):
    """connects two Nodes as siblings"""
    Node1.siblings.append(Node2)
    Node2.siblings.append(Node1)
