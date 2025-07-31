class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1, j = b.length() - 1;
        int carry = 0;
        StringBuilder result = new StringBuilder();
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) {
                sum += a.charAt(i) - '0';
            }
            if (j >= 0) {
                sum += b.charAt(j) - '0';
            }
            if (sum == 0 || sum == 1) {
                result.append(sum);
                carry = 0;
            }
            else if (sum == 2) {
                result.append("0");
                carry = 1;
            }
            else {
                result.append("1");
                carry = 1;
            }
            i--;
            j--;
        }
        if (carry == 1) {
            result.append("1");
        }
        return result.reverse().toString();
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
}
