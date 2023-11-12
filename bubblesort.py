import multiprocessing
import time

def bubble_sort(arr, node_id):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Node {node_id}: Step {i + 1} - {arr}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Node {node_id}: Sorted array: {arr}")
    print(f"Node {node_id}: Time taken: {elapsed_time} seconds")

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    processes = []

    for i in range(2):  # specify the number of processes as required
        p = multiprocessing.Process(target=bubble_sort, args=(arr, i))
        processes.append(p)
        p.start()

    for process in processes:
      process.join()