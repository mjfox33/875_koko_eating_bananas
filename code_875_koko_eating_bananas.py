class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def does_speed_work(speed) -> bool:
            return h >= sum((pile - 1) // speed + 1 for pile in piles)

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if does_speed_work(mid):
                right = mid
            else:
                left = mid + 1
        return left