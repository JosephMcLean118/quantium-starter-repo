from app import app


# test if header appears with correct text
def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

def test_visualization(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink-morsel-graph", timeout=10)


def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-input", timeout=10)


