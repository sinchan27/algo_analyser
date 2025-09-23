# import time
# import random
# import matplotlib.pyplot as plt
# import sys,json
# results=[]
# # Bubble Sort Function
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # Generate random array of given size
# def generate_array(size):
#     return [random.randint(0, 999) for _ in range(size)]

# # Input sizes for analysis
# input_sizes = [100, 200, 300, 400, 500]
# times = []

# # print(f"{'Input size':<12} {'time taken'}")

# for size in input_sizes:
#     arr = generate_array(size)

#     start = time.perf_counter()
#     bubble_sort(arr)
#     end = time.perf_counter()

#     time_taken = end - start
#     times.append(time_taken)
#     # print(f"{size:<12} {time_taken:.6f}")
#     result={
#         "input":size,
#         "time":round(time_taken,6)
#     }

#     # Display sorted array only for size = 100
#     if size == 100:
#        result["sorted array"]=arr
#        results.append(result)

# print(json.dumps(results))
# sys.stdout.flush()        

# # print("\n=== Code Execution Successful ===")

# # # Plotting the graph
# # plt.plot(input_sizes, times, marker='o', linestyle='-', color='b', label="Bubble Sort")
# # plt.xlabel("Input Size")
# # plt.ylabel("Time Taken (seconds)")
# # plt.title("Bubble Sort Time Analysis")
# # plt.legend()
# # plt.grid(True)
# # plt.show()

import sys, json, random, time, matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = json.loads(sys.argv[1])
        mode = payload.get("mode")
        data = payload.get("data")

        if mode == "array":
            sorted_arr = bubble_sort(data)
            result = {
                "input": data,
                "sorted_array": sorted_arr
            }
            print(json.dumps(result))

        elif mode == "sizes":
            results = []
            for size in data:
                arr = [random.randint(0, 999) for _ in range(size)]
                start = time.perf_counter()
                bubble_sort(arr)
                end = time.perf_counter()

                result = {
                    "input_size": size,
                    "time": round(end - start, 6)
                }
                results.append(result)
            


            input_sizes = [item["input_size"] for item in results]
            times = [item["time"] for item in results]

            plt.plot(input_sizes, times, marker='o', linestyle='-', color='blue')
            plt.title("Bubble Sort: Input Size vs Time")
            plt.xlabel("Input Size")
            plt.ylabel("Time (seconds)")
            plt.grid(True)
            plt.savefig(r"C:\Users\acer\algo-analyser\backend\public\graphs\bubble_sort_analysis.png")
            plt.close()
            print(json.dumps(results, indent=4))

    else:
        print(json.dumps({"error": "No input provided"}))
