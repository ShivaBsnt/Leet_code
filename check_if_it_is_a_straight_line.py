class Solution(object):
    def checkStraightLine(self, coordinates):
        x1 = coordinates[1][0] - coordinates[0][0] # (2-1) =1
        y1 = coordinates[1][1] - coordinates[0][1] # (3-2) = 1
        for i in range(2, len(coordinates)):
            x2 = coordinates[i][0] - coordinates[i-1][0] # (4-3) = 1
            y2 = coordinates[i][1] - coordinates[i-1][1] # (5-4) = 1
            if x1 * y2 != x2*y1: # 1*1 = 1*1
                return False
        return True
