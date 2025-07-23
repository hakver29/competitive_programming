package s0067_add_binary;

public class SolutionTest {
    public static void main(String[] args) {
        Solution solution = new Solution();

        String a1 = "11";
        String b1 = "1";
        String output1 = "100";
        runTest(solution.addBinary(a1, b1), output1, "Test Case 1");

        String a2 = "1010";
        String b2 = "1011";
        String output2 = "10101";
        runTest(solution.addBinary(a2, b2), output2, "Test Case 2");
    }

    private static void runTest(String result, String expected, String testCase) {
        if (result.equals(expected)) {
            System.out.println(testCase + " passed.");
        } else {
            System.out.println(testCase + " failed.");
            System.out.println("Expected: [" + expected +"]");
            System.out.println("Got:      [" + result + "]");
        }
    }
}
