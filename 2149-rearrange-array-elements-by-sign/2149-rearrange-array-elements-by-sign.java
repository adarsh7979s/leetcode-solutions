class Solution {

    public int[] rearrangeArray(int[] nums) {

        int[] result = new int[nums.length];

        int posIndex = 0; // even index
        int negIndex = 1; // odd index

        for (int i = 0; i < nums.length; i++) {

            if (nums[i] > 0) {
                result[posIndex] = nums[i];
                posIndex = posIndex + 2;
            } else {
                result[negIndex] = nums[i];
                negIndex = negIndex + 2;
            }
        }

        return result;
    }
}
