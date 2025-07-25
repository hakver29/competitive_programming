#include <iostream>
#include <vector>
#include <cassert>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

void runTest(const vector<int>& nums, int target, const vector<int>& expected, const string& testName) {
    Solution solution;
    vector<int> result = solution.twoSum(const_cast<vector<int>&>(nums), target);
    assert(result == expected && (cout << testName << " passed!" << endl));
}

int main() {
    runTest({2, 7, 11, 15}, 9, {0, 1}, "Test Case 1");
    runTest({3,2,4}, 6, {1, 2}, "Test Case 2");
    runTest({3,3}, 6, {0, 1}, "Test Case 3");

    std::cout << "All test cases passed!" << std::endl;

    return 0;
}
