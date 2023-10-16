def count_sort(arr):
    
    output = [0 for i in range(len(arr))]
    # Create a count array to store count of inidividul
    max_value = max(arr)
    count = [0 for i in range(max_value + 1)]
    ans = [0 for _ in arr]
    for i in arr:
        count[i] += 1
    for i in range(1,max_value + 1):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans, count

arr = [1, 4, 1, 2, 7, 5, 2]
ans, count = count_sort(arr)
print(ans)
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
if (a > b or b > len(count) -1):
    raise Exception("Invalid input")

print((count[b] - count[a])+1)
