class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        mid = len(l)//2
        if(len(l)%2==1):

            return(l[mid])

        else:
            return((l[mid-1] + l[mid])/2)


# Follow me on instagram my insta id is - @codewithsomesh
