package s0300_longest_increasing_subsequence;

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
}