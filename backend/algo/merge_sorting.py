import sys, json, random, time, matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = json.loads(sys.argv[1])
        mode = payload.get("mode")
        data = payload.get("data")

        if mode == "array":
            sorted_arr = merge_sort(data)
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
                merge_sort(arr)
                end = time.perf_counter()

                result = {
                    "input_size": size,
                    "time": round(end - start, 6)
                }
                results.append(result)
                input_sizes = [item["input_size"] for item in results]
            times = [item["time"] for item in results]

            plt.plot(input_sizes, times, marker='o', linestyle='-', color='blue')
            plt.title("Merge Sort: Input Size vs Time")
            plt.xlabel("Input Size")
            plt.ylabel("Time (seconds)")
            plt.grid(True)
            plt.savefig(r"C:\Users\acer\algo-analyser\backend\public\graphs\merge_sort.png")
            plt.close()
            print(json.dumps(results, indent=4))

            print(json.dumps(results))
    else:
        print(json.dumps({"error": "No input provided"}))
