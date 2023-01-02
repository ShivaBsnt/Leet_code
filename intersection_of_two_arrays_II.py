def intersect(nums1, nums2):
    intersection_list = list(set(nums1).intersection(set(nums2)))
    elem_count_in_list = []

    for elem in intersection_list:
        nums1_count=nums1.count(elem)
        nums2_count=nums2.count(elem)
        if nums1_count < nums2_count:
            count = nums1_count -1
        else:
            count = nums2_count - 1
        elem_count_in_list.append((elem,count))

    for elem in elem_count_in_list:
        for j in range(elem[1]):
            intersection_list.append(elem[0])
    return intersection_list