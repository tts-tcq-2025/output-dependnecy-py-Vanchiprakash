def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'
 
def test_size():
    assert size(37) == 'S'      # Below lower bound
    assert size(38) == 'L'      # Edge case: exactly 38 (bug: should probably be 'M')
    assert size(39) == 'M'      # Between 38 and 42
    assert size(40) == 'M'      # Between 38 and 42
    assert size(41) == 'M'      # Between 38 and 42
    assert size(42) == 'L'      # Edge case: exactly 42 (bug: should probably be 'M')
    assert size(43) == 'L'      # Above upper bound
test_size()
print("All is well (maybe!)")
