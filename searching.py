import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open("sequential.json","r") as f:
        allowed_key = json.load(f)

    if field not in allowed_key:
        return None

    with open(file_name,"r") as f:
        data = json.load(f)
    return data.get(field)
def binary_search(numbers,target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None
def main():
    sequentional_data = read_data("sequential.json","unordered_numbers")
    print(sequentional_data)


if __name__ == '__main__':
    main()