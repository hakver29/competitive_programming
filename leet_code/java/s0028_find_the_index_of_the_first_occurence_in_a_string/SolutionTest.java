package s0028_find_the_index_of_the_first_occurence_in_a_string;

public class SolutionTest {
    public static void main(String[] args) {
        Solution solution = new Solution();

        String haystack1 = "sadbutsad";
        String needle1 = "sad";
        int output1 = 0;
        runTest(solution.strStr(haystack1, needle1), output1, "Test Case 1");

        String haystack2 = "leetcode";
        String needle2 = "leeto";
        int output2 = -1;
        runTest(solution.strStr(haystack2, needle2), output2, "Test Case 1");
    }

    private static void runTest(int result, int expected, String testCase) {
        if (result == expected) {
            System.out.println(testCase + " passed.");
        } else {
            System.out.println(testCase + " failed.");
            System.out.println("Expected: [" + expected + "]");
            System.out.println("Got:      [" + result + "]");
        }
    }
}
