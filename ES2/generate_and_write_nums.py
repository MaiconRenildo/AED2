import random
nums = random.sample(range(1000000),k=1000000)
with open('ummilhao.txt','w') as f:
    for num in nums:  
        f.write('{},'.format(num))
