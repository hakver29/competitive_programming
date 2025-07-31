import java.util.Arrays;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int max = 1;

        for(int i = 0; i < dp.length; i++){
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    if(dp[i] > max){
                        max = dp[i];
                    }
                }
            }
        }

        return max;
    }

    private static void runTest(int result, int expected, String testCase) {
        if (result == expected) {
            System.out.println(testCase + " passed.");
        } else {
            System.out.println(testCase + " failed.");
            System.out.println("Expected: [" + expected +"]");
            System.out.println("Got:      [" + result + "]");
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] input1 = {10,9,2,5,3,7,101,18};
        int output1 = 4;
        runTest(solution.lengthOfLIS(input1), output1, "Test Case 1");

        int[] input2 = {0,1,0,3,2,3};
        int output2 = 4;
        runTest(solution.lengthOfLIS(input2), output2, "Test Case 2");

        int[] input3 = {7,7,7,7,7,7,7};
        int output3 = 1;
        runTest(solution.lengthOfLIS(input3), output3, "Test Case 3");
    }
}
