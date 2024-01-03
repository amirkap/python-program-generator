import unittest
from typing import List

def generate_permutations(nums: List[int]) -> List[List[int]]:
    if len(nums) <= 1:
        return [nums]
    
    result = []
    for i in range(len(nums)):
        remaining = nums[:i] + nums[i+1:]
        for perm in generate_permutations(remaining):
            result.append([nums[i]] + perm)
    
    return result

    
class TestGeneratePermutations(unittest.TestCase):
    def test_generate_permutations(self):
        nums1 = [1, 2, 3]
        expected_output1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(generate_permutations(nums1), expected_output1)
        
        nums2 = [4, 5, 6, 7]
        expected_output2 = [[4, 5, 6, 7], [4, 5, 7, 6], [4, 6, 5, 7], [4, 6, 7, 5], [4, 7, 5, 6], [4, 7, 6, 5], [5, 4, 6, 7], [5, 4, 7, 6], [5, 6, 4, 7], [5, 6, 7, 4], [5, 7, 4, 6], [5, 7, 6, 4], [6, 4, 5, 7], [6, 4, 7, 5], [6, 5, 4, 7], [6, 5, 7, 4], [6, 7, 4, 5], [6, 7, 5, 4], [7, 4, 5, 6], [7, 4, 6, 5], [7, 5, 4, 6], [7, 5, 6, 4], [7, 6, 4, 5], [7, 6, 5, 4]]
        self.assertEqual(generate_permutations(nums2), expected_output2)
        
        nums3 = [0]
        expected_output3 = [[0]]
        self.assertEqual(generate_permutations(nums3), expected_output3)
        
        nums4 = [9, 2, 6]
        expected_output4 = [[9, 2, 6], [9, 6, 2], [2, 9, 6], [2, 6, 9], [6, 9, 2], [6, 2, 9]]
        self.assertEqual(generate_permutations(nums4), expected_output4)
        
        nums5 = [-1, 0, 1]
        expected_output5 = [[-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]]
        self.assertEqual(generate_permutations(nums5), expected_output5)
        

def main():
    unittest.main(argv=[''], exit=False)


if __name__ == '__main__':
    main()