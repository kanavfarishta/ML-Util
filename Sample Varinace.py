data = [1,2,3,4,......nᵗʰ data]

mean = 0
length = len(daat)

# 1st time O(n) iteration 
for i in data:
    mean += i

#Now we have the mean with us 
mean = mean/length

# 2nd time O(n) iteration  
sampleVariance = 0
for i in data:
    sampleVariance += (i - mean)**2 # squaring the power

sampleVariance = sampleVariance/length -1

