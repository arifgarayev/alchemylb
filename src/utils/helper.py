class Helper:
    filter_output = lambda _tuple: ("Busy", "Busy") if "from" in _tuple else _tuple
