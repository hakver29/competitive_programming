public class SolutionTest {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums1 = { 1, 3, 5, 6 };
        int target1 = 5;
        int output1 = 2;
        runTest(solution.searchInsert(nums1, target1), output1, "Test Case 1");

        int[] nums2 = { 1, 3, 5, 6 };
        int target2 = 2;
        int output2 = 1;
        runTest(solution.searchInsert(nums2, target2), output2, "Test Case 2");

        int[] nums3 = { 1, 3, 5, 6 };
        int target3 = 7;
        int output3 = 4;
        runTest(solution.searchInsert(nums3, target3), output3, "Test Case 3");
    }

    private static void runTest(int result, int expected, String testCase) {
        if (result == expected) {
            System.out.println(testCase + " passed.");
        } else {
            System.out.println(testCase + " failed.");
            System.out.println("Expected: [" + expected + ", " + expected + "]");
            System.out.println("Got:      [" + result + ", " + result + "]");
        }
    }
}
