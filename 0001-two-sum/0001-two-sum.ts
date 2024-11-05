function twoSum(nums: number[], target: number): number[] {
    const dict: {[key: string]: number} = {};

    for (let i = 0; i< nums.length; i++) {
        if (target - nums[i] in dict) {
            return [dict[target - nums[i]], i];
        }
        dict[nums[i]] = i;
    }
    return [];

};