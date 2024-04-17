# @todo Run tests from *all* Python files, not just 'test*.py'. Then remove these imports.
# Impossible right now because opinion.config.prod is not importable without several environment variables set.
from ..router import ParseIncludeTestCase
from ..django import AuthenticationTestCase
from .attributes import AtomicAttributesTestCase
from .batching import BatchingTestCase
from .dependencies import DependenciesTestCase
from .empty import EmptyTestCase
from .polymorphism import OptionalRelationshipTestCase
from .relationships import RelationshipsTestCase


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
