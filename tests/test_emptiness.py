def test_emptiness():
    stack = []
    assert not stack
    stack.append("one")
    assert bool(stack)

    stack.pop()
    assert not stack
