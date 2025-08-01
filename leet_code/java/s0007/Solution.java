public class Solution {
    public int reverse(int x) {
        int reversed = 0;
        while (x != 0){
            try {
                int digit = x % 10;
                reversed = Math.multiplyExact(reversed, 10);
                reversed = Math.addExact(reversed, digit);
                x /= 10;
            } catch (ArithmeticException e){
                return 0;
            }
        }
        return reversed;
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

    public static void main(String[] args) {
        Solution solution = new Solution();

        int input1 = 123;
        int expected1 = 321;
        runTest(solution.reverse(input1), expected1, "Test Case 1");

        int input2 = -123;
        int expected2 = -321;
        runTest(solution.reverse(input2), expected2, "Test Case 2");

        int input3 = 120;
        int expected3 = 21;
        runTest(solution.reverse(input3), expected3, "Test Case 3");

        int input4 = 1534236469;
        int expected4 = 0;
        runTest(solution.reverse(input4), expected4, "Test Case 4");

        int input5 = -2147483412;
        int expected5 = -2143847412;
        runTest(solution.reverse(input5), expected5, "Test Case 5");

    }
};
