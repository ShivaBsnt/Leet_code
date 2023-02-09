class Solution(object):
    def isBoomerang(self, points):
        Y0 = points[0][1]
        Y1 = points[1][1]
        Y2 = points[2][1]
        X0 = points[0][0]
        X1 = points[1][0]
        X2 = points[2][0]

        return (X2-X1)* (Y1-Y0) != (Y2-Y1)*(X1-X0)
