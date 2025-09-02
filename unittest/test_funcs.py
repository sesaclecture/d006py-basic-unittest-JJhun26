from funcs import is_even, calculate_average, max_list, min_list 

def test_is_even():
    assert True == is_even(10)
    assert False == is_even(25)
    assert True == is_even(3434)

def test_calculate_average():
    assert 3 == calculate_average([1,2,3,4,5])
    assert 0 == calculate_average([-2,-1,0,1,2])

def test_max_list():
    assert 10 == max_list([0,2,4,6,8,10])
    assert 10.1 == max_list([-3.5, 1, 10.1, 2, 9, 8.5])

def test_min_list():
    assert -15 == min_list([-10, -9, 1, -15, 11])
    assert 5 == min_list([30, 62, 12, 5, 32])

