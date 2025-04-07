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
    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None

    with open(file_path,"r") as json_file:
        seq = json.load(json_file)
    return seq[field]
    # 2024
    # with open("sequential.json","r") as f:
    #     allowed_key = json.load(f)

    # 2024
    # if field not in allowed_key:
    #     return None
    #
    # with open(file_name,"r") as f:
    #     data = json.load(f)
    # return data.get(field)


def linear_search(sequence, target):
    """
    Perform linear search on an unsorted sequence to find the target.

    Args:
    - sequence (list): The sequence to search within.
    - target (int): The number to search for.

    Returns:
    - dict: A dictionary containing two keys:
        - 'positions': A list of positions (indices) where the target is found.
        - 'count': The count of occurrences of the target in the sequence.
    """
    seq_dic = {}
    pozice = []
    vyskyt = int
    for i,j in enumerate(sequence):
        if j == target:
            pozice.append(i)
            vyskyt += 1
    seq_dic = {"positions": pozice,"count":vyskyt}
    return seq_dic



    #2024
    # positions = []
    # count = 0
    #
    # for i, num in enumerate(sequence):
    #     if num == target:
    #         positions.append(i)
    #         count += 1
    #
    # return {'positions': positions, 'count': count}


def pattern_search(sequence, pattern):
    """
    Perform pattern search in a DNA sequence to find occurrences of the pattern.

    Args:
    - sequence (str): The DNA sequence to search within.
    - pattern (str): The pattern to search for.

    Returns:
    - set: A set containing the positions (indices) where the pattern is found in the sequence.
    """
    # positions = set()
    # seq_length = len(sequence)
    # pattern_length = len(pattern)
    #
    # for i in range(seq_length - pattern_length + 1):
    #     if sequence[i:i + pattern_length] == pattern:
    #         positions.add(i)
    #
    # return positions

# def binary_search(numbers,target):
#     left, right = 0, len(numbers) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return None
def main():
    file_name = "sequential.json"

    sequential_data = read_data(file_name, field="unordered_numbers")
    # print(sequential_data)

    # 2024
    # sequentional_data = read_data("sequential.json","unordered_numbers")
    # print(sequentional_data)


if __name__ == '__main__':
    main()