from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                collision = asteroid + stack[-1]
                if collision < 0:
                    stack.pop()
                elif collision >= 0:
                    asteroid = 0
                    if collision == 0:
                        stack.pop()
            if asteroid:
                stack.append(asteroid)

        return stack
    
    asteroids = [5,10,-5]
    asteroidCollision(0, asteroids)