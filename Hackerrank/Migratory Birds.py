from collections import Counter

def migratoryBirds(arr):
    # Write your code here
    carr = Counter(arr)
    cdic = dict(carr)
    #print(cdic)
    
    carr_val = list(cdic.values())
    carr_val.sort()
    
    #print(carr_val)
    max = carr_val[-1]
    l = [k for k,v in carr.items() if v==max]
    
    return min(l)
