nums1 = [8, 9, 14, 27, 55]
nums2 = [1, 3, 10, 13, 16, 22, 32]
    
merged = []
        
while len(nums1) != 0 and len(nums2) != 0:
    if nums1[0] <= nums2[0]:
        merged.append(nums1[0])
        del(nums1[0])
    else:
        merged.append(nums2[0])
        del(nums2[0])
            
if len(nums1) + len(nums2) != 0:
    if len(nums1) == 0:
        merged = merged + nums2
    else:
        merged = merged + nums1
        
n = len(merged)
print(merged)

if n % 2:
    print(f"median: {merged[int(((n + 1)/2) - 1)]}")
else:
    print(f"median: {(merged[int(n/2) - 1] + merged[int((n/2))])/2}")