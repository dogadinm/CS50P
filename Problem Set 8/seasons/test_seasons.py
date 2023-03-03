from seasons import min_life

def test():
    assert min_life(2023, 1, 22) == "one thousand, four hundred forty"
    assert min_life(22, 1, 2023) == "Invalid date"