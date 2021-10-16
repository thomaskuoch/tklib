def pytest_addoption(parser):
    parser.addoption(
        "--issue",
        action="store",
        nargs="*",
        default=None,
        help="Select only tests marked with issue number (i.e. '#1234')",
    )


def pytest_collection_modifyitems(config, items):
    # Filter tests if flag issue is provided
    filter = config.getoption("--issue")
    if filter:
        selected_items = []
        deselected_items = []
        for item in items:
            mark = item.get_closest_marker("issue")
            if mark and mark.args and mark.args[0] in filter:
                selected_items.append(item)
            else:
                deselected_items.append(item)
        config.hook.pytest_deselected(items=deselected_items)
        items[:] = selected_items
