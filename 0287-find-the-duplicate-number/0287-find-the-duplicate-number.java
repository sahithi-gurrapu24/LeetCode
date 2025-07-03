class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int j=0;
        for(int i=0;i<nums.length-1;i++){
            j=i+1;
            if (nums[j]-nums[i]==0)
            {
                return nums[i];
            }
        }
           return -1;
    }
 
    
}