package s0001_two_sum;

public class SolutionTest {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] expected1 = {0, 1};
        runTest(solution.twoSum(nums1, target1), expected1, "Test Case 1");

        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        int[] expected2 = {1, 2};
        runTest(solution.twoSum(nums2, target2), expected2, "Test Case 2");

        int[] nums3 = {3, 3};
        int target3 = 6;
        int[] expected3 = {0, 1};
        runTest(solution.twoSum(nums3, target3), expected3, "Test Case 3");
    
        runTest(solution.twoSum_HashMap(nums1, target1), expected1, "Test Case 1, Hashmap");
        runTest(solution.twoSum_HashMap(nums2, target2), expected2, "Test Case 2, Hashmap");
        runTest(solution.twoSum_HashMap(nums3, target3), expected3, "Test Case 3, Hashmap");

  }

    private static void runTest(int[] result, int[] expected, String testCase) {
        if (result[0] == expected[0] && result[1] == expected[1]) {
            System.out.println(testCase + " passed.");
        } else {
            System.out.println(testCase + " failed.");
            System.out.println("Expected: [" + expected[0] + ", " + expected[1] + "]");
            System.out.println("Got:      [" + result[0] + ", " + result[1] + "]");
        }
    }
}
