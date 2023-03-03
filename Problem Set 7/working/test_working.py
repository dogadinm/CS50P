import pytest
from working import convert

def test():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    with pytest.raises(ValueError):
        convert("9:61 AM to 12:90 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("09:00 - 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 8 PM")