from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

# Import callback function
from app import graph, header, filters


# test if header appears with correct text, and if the graph and filters appear
def test_sections():
    assert header.children  == "Pink Morsels Price Trend Over Time"
    assert graph is not None
    assert filters is not None