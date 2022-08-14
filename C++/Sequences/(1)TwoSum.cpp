// Brute Force Method
// Time: O(n^2)
// Space: O(1)
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

// Two-pass Hash Table
// Time: O(n)
// Space: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;

        for (int i = 0; i < nums.size(); i++) {            
            indices[nums[i]] = i;
        }
        
        for (int i = 0; i < nums.size(); i++) {            
            if (indices[target - nums[i]] && indices[target - nums[i]] != i)
                return {indices[target - nums[i]], i};
        }
        
        return {};
    }
};

// One-pass Hash Table
// Time: O(n)
// Space: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;

        for (int i = 0; i < nums.size(); i++) {            
            if (indices.find(target - nums[i]) != indices.end())
                return {indices[target - nums[i]], i};
            indices[nums[i]] = i;
        }
        
        return {};
    }
};