use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            let complement = target - num;

            if let Some(&complement_index) = map.get(&complement) {
                return vec![complement_index, i as i32];
            }

            map.insert(*num, i as i32);
        }

        unreachable!("Should always find a solution based on problem constraints.");
    }
}

// Unit tests for the solution.
#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_example_1() {
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let expected1 = vec![0, 1];
        let expected2 = vec![1, 0];
        let result = Solution::two_sum(nums, target);
        let mut sorted_result = result.clone();
        sorted_result.sort_unstable();
        assert!(sorted_result == expected1 || sorted_result == expected2);
    }

    #[test]
    fn test_example_2() {
        let nums = vec![3, 2, 4];
        let target = 6;
        let expected1 = vec![1, 2];
        let expected2 = vec![2, 1];
        let result = Solution::two_sum(nums, target);
        let mut sorted_result = result.clone();
        sorted_result.sort_unstable();
        assert!(sorted_result == expected1 || sorted_result == expected2);
    }

    #[test]
    fn test_example_3() {
        let nums = vec![3, 3];
        let target = 6;
        let expected1 = vec![0, 1];
        let expected2 = vec![1, 0];
        let result = Solution::two_sum(nums, target);
        let mut sorted_result = result.clone();
        sorted_result.sort_unstable();
        assert!(sorted_result == expected1 || sorted_result == expected2);
    }
}
