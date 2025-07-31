class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];
        int n = text1.length();
        int m = text2.length();
        for(int i = 0; i < n; i++) dp[i][0] = 0;

        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++){
                if (text1.charAt(i-1) == text2.charAt(j-1)) {
                    dp[i][j] = 1 + dp[i-1][j-1];
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
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

        String input1text1 = "abcde";
        String input1text2 = "ace";
        int output1 = 3;
        runTest(solution.longestCommonSubsequence(input1text1, input1text2), output1, "Test Case 1");

        String input2text1 = "abc";
        String input2text2 = "abc";
        int output2 = 3;
        runTest(solution.longestCommonSubsequence(input2text1, input2text2), output2, "Test Case 2");

        String input3text1 = "abc";
        String input3text2 = "def";
        int output3 = 0;
        runTest(solution.longestCommonSubsequence(input3text1, input3text2), output3, "Test Case 3");
    }
}
