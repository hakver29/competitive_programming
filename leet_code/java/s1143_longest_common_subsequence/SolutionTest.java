package s1143_longest_common_subsequence;

public class SolutionTest {
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

    private static void runTest(int result, int expected, String testCase) {
        if (result == expected) {
            System.out.println(testCase + " passed.");
        } else {
            System.out.println(testCase + " failed.");
            System.out.println("Expected: [" + expected +"]");
            System.out.println("Got:      [" + result + "]");
        }
    }
}
