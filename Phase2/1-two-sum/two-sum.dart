class Solution {
  List<int> twoSum(List<int> nums, int target) {
    var dict = Map<int,int>();
    List<int> result = [];

    for(var i = 0;i < nums.length;i++){
        var complement = target - nums[i];
        if(dict.containsKey(complement)){
            result.add(dict[complement]!);
            result.add(i);
            break;
        }
        dict[nums[i]] = i;

    } 
    return result;
  }
}