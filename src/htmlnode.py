class HTMLNode:
    def __init__(self, tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        return_value = ""
        for key in self.props:
            return_value += f' {key}="{self.props[key]}"'
        return return_value


    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props) 

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        elif self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_list = ""
        if self.tag is None:
            return ValueError("invalid HTML: no tag")
        elif self.children is None:
            return ValueError("invalid HTML: no children")
        else:
            for node in self.children:
                if isinstance(node, LeafNode):
                    children_list += node.to_html()
                    print(f"This is running when the node is {type(node)} --> {children_list}")
                else:
                    print(f"This is running when the node is {type(node)} --> {node.to_html()}")
                    return node.to_html()
            return f'<{self.tag}{self.props_to_html()}>{children_list}</{self.tag}>'

