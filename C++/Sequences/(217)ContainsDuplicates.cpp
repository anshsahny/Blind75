// List to hold all viewed values
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        vector<int> values;
        
        for (int i = 0; i < nums.size(); i++) {
            if (find(values.begin(), values.end(), nums[i]) != values.end())
                return true;
            values.push_back(nums[i]);
        }
        
        return false;
    }
};

// Sorting original array to see which number repeats
// Time: O(nlogn)
// Space: O(1)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i+1])
                return true;
        }
        
        return false;
    }
};