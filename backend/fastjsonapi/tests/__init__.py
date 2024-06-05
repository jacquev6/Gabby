# class TreeNode(BaseModel):
#     label: str | None = None
#     parent : TreeNode | None = None
#     children : list[TreeNode] = []

# class TreeNodeTestCase(TestMixin, TestCase):
#     class NodeResource:
#         singular_name = "node"
#         plural_name = "nodes"

#         default_page_size = 2

#         Model = TreeNode

#     resources = [NodeResource()]

#     # @todo Test it allows creation without "attributes" and "relationships"
