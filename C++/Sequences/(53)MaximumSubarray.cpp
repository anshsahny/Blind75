// Brute Force
// Time: O(n^2)
// Space: O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maximum = INT_MIN;
        
        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int j = i; j < nums.size(); j++) {
                sum += nums[j];
                maximum = max(sum, maximum);
            }
        }
        
        return maximum;
    }
};

// Dynamic Programming, Kadane's Algorithm
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        int maximum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            sum = max(nums[i], sum + nums[i]);
            maximum = max(sum, maximum);
        }
        
        return maximum;
    }
};