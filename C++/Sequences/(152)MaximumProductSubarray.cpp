// Brute Force
// Time: O(n^2)
// Space: O(1)
class Solution {
public:
    int maxProduct(vector<int>& nums) { 
        int maximum = INT_MIN;
        
        for (int i = 0; i < nums.size(); i++) {
            int product = 1;
            for (int j = i; j < nums.size(); j++) {
                product *= nums[j];
                maximum = max(product, maximum);
            }
        }
        
        return maximum;
    }
};

// Dynamic Programming
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int maxProduct(vector<int>& nums) { 
        int currMax = nums[0];
        int currMin = nums[0];
        int maximum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            int tempMax = max(nums[i], max(currMax*nums[i], currMin*nums[i]));
            currMin = min(nums[i], min(currMax*nums[i], currMin*nums[i]));
            
            currMax = tempMax;
            
            maximum = max(maximum, currMax);
        }
        
        return maximum;
    }
};