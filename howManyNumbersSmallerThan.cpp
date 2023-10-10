class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> result ;
        int val;
        
        for (int i =  0; i < nums.size(); i++){
            val  = 0;
            for (int j = 0; j < nums.size(); j++){
                if(nums[i]>nums[j] && j!=i){
                    val++;
                }
            }
            result.push_back(val);
        }
        return result;
    } 
    
};
