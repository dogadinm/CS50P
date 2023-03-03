from twttr import shorten

def test():
    assert shorten('hi') == 'h'
    assert shorten('Misha') == 'Msh'
    assert shorten('CS50') == 'CS50'
    assert shorten(',-=') == ',-='
    assert shorten('TwItter') == 'Twttr'