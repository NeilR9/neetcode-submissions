class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = pointer1 + 1
        while pointer1 < len(numbers) - 1:
            #print(f"Number 1: {numbers[pointer1]}")
            #print(f"Number 2: {numbers[pointer2]}")
            if numbers[pointer1] + numbers[pointer2] == target:
                return [pointer1 + 1, pointer2 + 1]
            else:
                if pointer2 == len(numbers) - 1:
                    pointer1 = pointer1 + 1
                    pointer2 = pointer1 + 1
                else:
                    pointer2 = pointer2 + 1
        return []
