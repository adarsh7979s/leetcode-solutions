class Solution {
    public int[] rearrangeArray(int[] nums) {
         List<Integer> pos = new ArrayList<>();
         List<Integer> neg = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                pos.add(nums[i]);
            }
            else{
                neg.add(nums[i]);
            }
        }

        int[] result= new int[nums.length];
        int index = 0;

        for(int i=0;i<pos.size();i++){
            result[index]=pos.get(i);
            result[index+1]=neg.get(i);
            index=index+2;
        }
        return result;
    }
}