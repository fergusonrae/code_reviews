from happiness import get_happiness

def test_get_happiness():

    # Test 1
    set_a = {1}
    set_b = {2}
    integers_to_check = [1]
    assert isinstance(get_happiness(integers_to_check, set_a, set_b), int)
    assert get_happiness(integers_to_check, set_a, set_b) == 1

    # Test 2
    set_a = {2}
    set_b = {1}
    integers_to_check = [1]
    assert get_happiness(integers_to_check, set_a, set_b) == -1

    # Test 3
    set_a = {1, 3, 4}
    set_b = {2, 5}
    integers_to_check = [1]
    assert get_happiness(integers_to_check, set_a, set_b) == 1

    # Test 4
    set_a = {1}
    set_b = {2}
    integers_to_check = [80]
    assert get_happiness(integers_to_check, set_a, set_b) == 0

    # Test 5
    set_a = {1, 80, 4, 3, 99}
    set_b = {2, 5, 34, 42, 12, 14}
    integers_to_check = [80, 5, 2, 12]
    assert get_happiness(integers_to_check, set_a, set_b) == -2

    # Test 5
    set_a = {1, 80, 4, 3, 99}
    set_b = {2, 5, 34, 42, 12, 14}
    integers_to_check = [80, 80, 80, 5, 2, 12]
    assert get_happiness(integers_to_check, set_a, set_b) == 0

    # Test 6
    set_a = {1, 3, 4}
    set_b = {2, 5, 3}
    integers_to_check = [1, 3]
    assert get_happiness(integers_to_check, set_a, set_b) == 0