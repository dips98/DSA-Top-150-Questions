/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n = nums.length;
    let prod = 1;
    let zeroCount = 0;
    let res = []
    for (i = 0; i < n; i++) {
        if (nums[i] != 0) {
            prod = prod * nums[i];
        } else {
            zeroCount++;
        }

    }
    for (i = 0; i < n; i++) {
        if (zeroCount === 0) {
            res[i] = prod / nums[i];
        } else if (zeroCount === 1) {
            res[i] = nums[i] == 0 ? prod : 0;
        } else {
            res[i] = 0;
        }
    }
    return res;

};