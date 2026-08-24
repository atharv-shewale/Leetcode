class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> h1 = new HashSet();
        for(int i=0;i<nums.length;i++){
            
            if(!h1.add(nums[i])){
            return true;

        }

        }
        
        
            return false;
        
    }
}