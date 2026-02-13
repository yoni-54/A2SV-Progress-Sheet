class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newMatrix = []
        for row in image:
            flipped = row[::-1]
            inverted = [1-x for x in flipped]
            newMatrix.append(inverted)
        return newMatrix