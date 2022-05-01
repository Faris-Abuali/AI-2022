from Node import Node

binary_tree = Node( 
            value=None, #Values for non-terminal nodes are not yet known
            children=[
                Node(
                    value=None,
                    children=[
                        Node(
                            value=None,
                            children=[
                                Node(
                                    value=None,
                                    children=[Node(value=50), Node(value=70)]
                                ),
                                Node(
                                    value=None,
                                    children=[Node(value=60), Node(value=90)]
                                ),
                            ]
                        ),
                        Node(
                            value=None,
                            children=[
                                Node(
                                    value=None,
                                    children=[Node(value=10), Node(value=50)]
                                ),
                                Node(
                                    value=None,
                                    children=[Node(value=60), Node(value=70)]
                                ),
                            ]
                        ),
                    ]
                ),
                Node(
                    value=None,
                    children=[
                        Node(
                            value=None,
                            children=[
                                Node(
                                    value=None,
                                    children=[Node(value=80), Node(value=90)]
                                ),
                                Node(
                                    value=None,
                                    children=[Node(value=20), Node(value=30)]
                                ),
                            ]
                        ),
                        Node(
                            value=None,
                            children=[
                                Node(
                                    value=None,
                                    children=[Node(value=40), Node(value=23)]
                                ),
                                Node(
                                    value=None,
                                    children=[Node(value=40), Node(value=30)]
                                ),
                            ]
                        ),
                    ]
                ),
            ]
)



# remember: Only the terminal nodes have known values. Non-terminal nodes values are still None (Unknown yet)
ternary_tree = Node(
    value=None,
    children=[
        Node(
            value=None,
            children=[Node(value=9), Node(value=8), Node(value=7)]
        ),
        Node(
            value=None,
            children=[Node(value=6), Node(value=5), Node(value=4)]
        ),
        Node(
            value=None,
            children=[
                Node(value=3),
                Node(value=2),
                Node(value=1)
            ]
        ),
    ]
)


tree_prune_example = Node(
    value=None,
    children=[
        Node(
            value=None,
            children=[
                Node(
                    value=None,
                    children=[Node(value=50), Node(value=40)]
                ),
                Node(
                    value=None,
                    children=[Node(value=70), Node(value=10), Node(value=60)]
                )
            ]
        ),
        Node(
            value=None,
            children=[
                Node(
                    value=None,
                    children=[Node(value=30)]
                ),
                Node(
                    value=None,
                    children=[Node(value=50), Node(value=90)]
                )
            ]
        ),
        Node(
            value=None,
            children=[
                Node(
                    value=None,
                    children=[Node(value=20)]
                ),
                Node(
                    value=None,
                    children=[Node(value=90), Node(value=70), Node(value=60)]
                )
            ]
        )
    ]
)

tree_prune_slides_example = Node(
    value=None,
    children=[
        Node(
            value=None,
            children=[
                Node(
                    value=None,
                    children=[Node(value=3), Node(value=4), Node(value=2)]
                ),
                Node(
                    value=None,
                    children=[Node(value=7), Node(value=2), Node(value=3)]
                ),
            ]           
        ),
        Node(
            value=None,
            children=[
                Node(
                    value=None,
                    children=[Node(value=2), Node(value=3), Node(value=1)]
                ),
                Node(
                    value=None,
                    children=[Node(value=4), Node(value=5), Node(value=3)]
                ),
            ]           
        ),
        Node(
            value=None,
            children=[
                Node(
                    value=None,
                    children=[Node(value=3), Node(value=3), Node(value=2)]
                ),
                Node(
                    value=None,
                    children=[Node(value=8), Node(value=4), Node(value=5)]
                ),
            ]           
        ),
    ]
)