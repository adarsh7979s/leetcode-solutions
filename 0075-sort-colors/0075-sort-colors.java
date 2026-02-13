class Solution {
    public void sortColors(int[] nums) {

        int low = 0;
        int mid = 0;
        int high = nums.length - 1;

        while (mid <= high) {

            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low = low + 1;
                mid = mid + 1;
            }
            else if (nums[mid] == 1) {
                mid = mid + 1;
            }
            else {
                swap(nums, mid, high);
                high = high - 1;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
