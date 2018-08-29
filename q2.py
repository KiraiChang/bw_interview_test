def extend_list(val, l=[]):
    # default param will be reused when not assign
    l.append(val)
    return l

def test_extend_list():
    # 1
    assert extend_list(1) == [1]
    # 2
    assert extend_list(2, []) == [2]
    # 3
    assert extend_list(3) == [1,3]

if __name__ == '__main__':
    # this is for confirm will run on cmd
    test_extend_list()