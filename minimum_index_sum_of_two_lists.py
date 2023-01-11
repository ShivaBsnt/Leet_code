class Solution(object):
    def findRestaurant(self, list1, list2):
        commons = list(set(list1).intersection(set(list2)))
        pair = dict()
        min_val = None
        for common in commons:
            # getting index value
            i1 = list1.index(common)
            i2 = list2.index(common)
            
            # this condition is alwayas met at first
            if min_val is None:
                min_val = i1+i2
                pair[i1+i2] = [common]
                
            # appending value if dict already has a key
            elif pair.get(i1+i2):
                pair[i1+i2].append(common)
            
            # adding new key value pair to dict
            else:
                pair[i1+i2]=[common]
            
            # condition to track min_value
            if min_val > i1+i2:
                min_val = i1+i2

        return pair[min_val]
        