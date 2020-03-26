import os
import heapq
import asyncio

num_of_files = list()

def in_file_sort(list): 
    if len(list) > 1: 
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]
        i = j = k = 0
        in_file_sort(L)
        in_file_sort(R)
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def k_way_merge(*lists):
    return heapq.merge(*lists)

async def input_handler(filename):
  with open(filename) as file:
      num_of_file = list()
      for line in file:
        num_of_file.append(int(line.strip("\n"),10))
      in_file_sort(num_of_file)
      num_of_files.append(num_of_file)
  file.close()

async def main():
    tasks = list()
    dir_path = os.getcwd()
    input_path = os.path.join(dir_path,'input')

    for filename in os.listdir(input_path):
        input_file = input_path + '/' + filename
        # task = asyncio.create_task(input_handler(input_file))
        task = input_handler(input_file)
        tasks.append(task)
    await asyncio.gather(*tasks)

    kwayed = list(k_way_merge(*num_of_files))
    output_path = os.path.join(dir_path, 'output')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    output_file = output_path + '/async_sorted.txt'
    for num in kwayed:
        with open(output_file, 'w+') as file:
            for num in kwayed:
                file.write(str(num) + '\n')
        file.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())