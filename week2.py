#question 1
def calculate(min,max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)

calculate(1, 3)
calculate(4, 8)





#question 2
def avg(data):
    
    dic=data["employees"]
    sum=0
    for n in dic:
        x=(n["salary"])
        sum=sum+x
    print(sum/len(dic))
       
avg({
    "count":3,
    "employees":[
    {
    "name":"John",
    "salary":30000
    },
    {
    "name":"Bob",
    "salary":60000
    },
    {
    "name":"Jenny",
    "salary":50000
    }
    ]
})

#question 3
def maxProduct(nums):

    a=nums[0]; b=nums[1]
    n=len(nums)
    
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i]*nums[j]> a*b):
                a=nums[i];b=nums[j]

    print(a*b)
            
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


#question 4
def twoSum(nums, target):
    n=len(nums)
    
    for i in range(0,n):
       for j in range(i+1,n):
            if (nums[i]+nums[j]==target):
                return[i,j]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#question 5
'''def maxZeros(nums):
    answer = 0 
    maxZeros= 0
    n=len(nums)
    for k in range(0 , n+1):
        numZeros = 0
        value = a
        while value:
            if value % k ==0:
                numZeros += 1
            value //= k 
        if numZeros > maxZeros:
            maxZeros = numZeros
            answer= k
    return answer

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
'''





