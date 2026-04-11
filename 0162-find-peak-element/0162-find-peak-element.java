class Solution {
    public int findPeakElement(int[] nums) {
        int low =0;
        int high =nums.length-1;
        int idx=-1;

       while(low<=high){
        int mid=(low + high)/2;
        if(mid==nums.length-1 || nums[mid] > nums[mid+1]){
            idx =mid;
            high = mid-1;
        }else{
            low = mid +1;
        }
       }
       return idx;
    }
}