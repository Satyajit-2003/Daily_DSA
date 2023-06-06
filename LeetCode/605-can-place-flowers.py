class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
      key = 0
      while key < len(flowerbed) and n:
        if flowerbed[key] == 1:
          key += 2
        elif key == len(flowerbed) - 1:
          if flowerbed[key] == 0 and flowerbed[key - 1] == 0:
            flowerbed[key] = 1
            n -= 1
          key += 1
        elif key == 0:
          if flowerbed[key] == 0 and flowerbed[key + 1] == 0:
            flowerbed[key] = 1
            n -= 1
          key += 1
        else:
          if flowerbed[key] == 0 and flowerbed[key - 1] == 0 and flowerbed[key + 1] == 0:
            flowerbed[key] = 1
            n -= 1
          key += 1
        
      if not n:
        return True 
      return False


if __name__ == '__main__':
    s = Solution()  
    print(s.canPlaceFlowers([1,0,0,0,1], 1)) # True
    print(s.canPlaceFlowers([1,0,0,0,1], 2)) # False
    print(s.canPlaceFlowers([0,0,1,0,1], 1)) # True
    print(s.canPlaceFlowers([0,0,1,0,1], 2)) # False
    print(s.canPlaceFlowers([0,0,0,0,1], 2)) # True
    print(s.canPlaceFlowers([0,0,0,0,1], 3)) # False
    print(s.canPlaceFlowers([0,0,0,0,0], 3)) # True

        