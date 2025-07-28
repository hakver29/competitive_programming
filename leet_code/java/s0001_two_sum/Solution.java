package s0001_two_sum;

import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] array = new int[2];
        for (int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(i != j && nums[i] + nums[j] == target){
                    array[0] = i;
                    array[1] = j;
                    return array;
                }
            }
        }
        return array;
    }

    public int[] twoSum_HashMap(int[] nums, int target) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int complement = target - num;
            Integer complementIndex = numsMap.get(complement);

            if (complementIndex != null){
                return new int[] {complementIndex, i};
            }
            numsMap.put(num, i);
        }
        
        return new int[]{-1,-1};
    }
}
