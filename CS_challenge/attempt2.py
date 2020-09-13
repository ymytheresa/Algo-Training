import random

n = 10
array = [random.randint(0,100) for _ in range(n)]
target = 30

# def subset_sum(numbers, target, partial=[]):
#     s = sum(partial)

#     # check if the partial sum is equals to target
#     if s == target: 
#         print "sum(%s)=%s" % (partial, target)
#     if s >= target:
#         return  # if we reach the number why bother to continue

#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i+1:]
#         subset_sum(remaining, target, partial + [n])

# for ans in res:
#     for val in ans:
#         print(array.index(val), end=',')
#     print('\n')

def subset_sum(numbers, target, partial=[], partial_sum=0, initial=True):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n, False)
        
array = [1,2,30,-6,6,3,17,-1,82,23,234]
target = 24
print(array, target)
res = list(subset_sum(array, target))
print(res)