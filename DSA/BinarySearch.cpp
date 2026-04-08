# include <bits/stdc++.h>

using namespace std;

int binarySearch(vector<int>& nums, int target) {
    int left=0, right=nums.size()-1;
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target) {
            return mid;
        } else if(nums[left] <= nums[mid]) {
            if(nums[left] <= target && nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else if(nums[right] >= nums[mid]) {
            if(nums[right] >= target && nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
}

int main() {
    vector<int> nums = {6,7,8,1,3,4};
    int target = 1;
    cout << target << "\n";
    cout << binarySearch(nums, target);
    return 0;
}