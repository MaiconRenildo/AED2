import random

def generate_nums():
    return random.sample(range(1000000),k=1000000)

def write_nums(nums, filename):
    with open(filename+'.txt','w') as f:
    for num in nums:  
        f.write('{},'.format(num))
