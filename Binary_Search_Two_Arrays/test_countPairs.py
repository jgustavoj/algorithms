from binary_search_two_arrays import countPairs

# def test_countPairs(monkeypatch):
#     inputs = ['3', '1', '2', '3', '2', '1', '2', '4']
#     monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
#     assert countPairs(int(inputs[0]), [int(x) for x in inputs[1:int(inputs[0])+1]], 
#                       int(inputs[int(inputs[0])+1]), [int(x) for x in inputs[int(inputs[0])+2:-1]], 
#                       int(inputs[-1])) == 3


def test_countPairs():
    n = 3
    a = [1, 2, 3]
    m = 2
    b = [1, 2]
    k = 4

    assert countPairs(n, a, m, b, k) == 3