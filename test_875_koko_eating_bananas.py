from code_875_koko_eating_bananas import Solution

def test_example_1():
    s = Solution()
    piles = [3,6,7,11]
    hours = 8
    output = 4
    assert s.minEatingSpeed(piles,hours) == output

def test_example_2():
    s = Solution()
    piles = [30,11,23,4,20]
    hours = 5
    output = 30
    assert s.minEatingSpeed(piles,hours) == output

def test_example_3():
    s = Solution()
    piles = [30,11,23,4,20]
    hours = 6
    output = 23
    assert s.minEatingSpeed(piles,hours) == output