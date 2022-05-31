
# s1...s4 = size haye abad
# x,y,w,z = index ha
def ndai(s1,s2,s3,s4,x,y,w,z):
    return (x * s2 * s3 * s4) + (y * s3 * s4) + (w * s4) + (z)

# Alef , satri
print("\alef:", ndai(5,10,15,20,2,3,4,6))

# B , sotooni
print("b:", ndai(20,15,10,5,6,4,3,2) * 4 + 1000)
