class Solution {
    public int searchInsert(int[] nums, int target) {
        int n=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==target)
            {
                n=i;
                break;
            }
        

            else if(nums[i]>target)
            {
                n=i;
                break;
            }
            else{
                n=nums.length;
            }
        }
        return n;
    }
}