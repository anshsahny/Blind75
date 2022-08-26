// Hashset
// Time: O(n^2)
// Space: O(n)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> answer;
        
        for (int i = 0; i < nums.size() && nums[i] <= 0; i++) {
            if (i == 0 || nums[i-1] != nums[i]) {
                twoSum(nums, i, answer);
            }
        }
        
        return answer;
    }
    
    void twoSum(vector<int>& nums, int i, vector<vector<int>>& answer) {
        unordered_set<int> visited;
        for (int j = i + 1; j < nums.size(); j++) {
            int complement = -nums[i] - nums[j];
            if (visited.count(complement)) {
                answer.push_back({nums[i], complement, nums[j]});
                while (j + 1 < nums.size() && nums[j] == nums[j+1])
                    j++;
            }
            visited.insert(nums[j]);
        }
    }
};