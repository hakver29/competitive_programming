pub struct Solution {}

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        match nums.binary_search(&target) {
            Ok(index) => index as i32,
            Err(index) => index as i32,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test1() {
        let nums = vec![1, 3, 5, 6];
        let target = 5;
        let expected = 2;
        assert_eq!(Solution::search_insert(nums, target), expected);
    }

    #[test]
    fn test2() {
        let nums = vec![1, 3, 5, 6];
        let target = 2;
        let expected = 1;
        assert_eq!(Solution::search_insert(nums, target), expected);
    }

    #[test]
    fn test3() {
        let nums = vec![1, 3, 5, 6];
        let target = 7;
        let expected = 4;
        assert_eq!(Solution::search_insert(nums, target), expected);
    }
}
