from binary_search_two_arrays import countPairs

def test_countPairs(monkeypatch):
    inputs = ['3', '1', '2', '3', '2', '1', '2', '4']
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    assert countPairs(3, [1, 2, 3], 2, [2, 1], 4) == 3