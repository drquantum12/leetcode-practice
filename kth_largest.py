# finding Kth largest => get largest on root with each heap max down, repeated k-1 times
import heapq
def heapify_down_max(arr, n, i):
    largest=i
    left=2*i + 1
    right=2*i + 2

    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i], arr[largest]=arr[largest], arr[i]
        heapify_down_max(arr, n, largest)

def heap_max(arr, n):
    for _ in range((n//2) - 1, -1, -1):
        heapify_down_max(arr, n, _)

# def find_k_largest(arr, k):
#     n=len(arr)
#     heap_max(arr, n)
#     for i in range(k-1):
#         arr[0], arr[n-1]=arr[n-1], arr[0]
#         print(f"array at {i}: {arr}")
#         n-=1
#         heapify_down_max(arr, n, 0)
#     return arr[0]

def nlargest(arr, k):
    heap = heapq.nlargest(k, arr)
    return heap[-1]

if __name__ == "__main__":
    arr=[3,2,3,1,2,4,5,5,6]
    ans=nlargest(arr, 4)
    print(f"Answer: {ans}")
