class Solution {
    public int removeElement(int[] nums, int val) {
        Arrays.sort(nums);
        int n=nums.length-1;
        int count=0;
        for(int i=0;i<n+1;i++)
        {
           
            if(nums[i]==val)
            {
                 if(nums[i]==nums[n]){
                break;
                }
             nums[i]=nums[i]^nums[n];
             nums[n]=nums[i]^nums[n];
             nums[i]=nums[i]^nums[n];
             n-=1;
            }

        }
        for(int j=0;j<n+1;j++)
        {
            if(nums[j]==val)
            break;
            count+=1;
        }
        return count;
    }

}