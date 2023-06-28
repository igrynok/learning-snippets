from typing import Counter
import heapq


# check whether it's possible to rearrange the string so there is no two the same adjacent characters
def reorganize_string(s: str) -> str:
    counter = {}
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    heap = []
    for key in counter.keys():
        heapq.heappush(heap, (-counter[key], key))

    result = ''

    while heap:
        most_freq_letter_count = heapq.heappop(heap)
        if result and result[-1] == most_freq_letter_count[1]:
            return ''
        result += most_freq_letter_count[1]
        if heap:
            next_freq_letter = heapq.heappop(heap)
            result += next_freq_letter[1]
            if -next_freq_letter[0] > 1:
                heapq.heappush(heap, (next_freq_letter[0] + 1, next_freq_letter[1]))
        if -most_freq_letter_count[0] > 1:
            heapq.heappush(heap, (most_freq_letter_count[0] + 1, most_freq_letter_count[1]))

    return result


if __name__ == '__main__':
    s = input()
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i + 1}")
            exit()
    print("Valid")
