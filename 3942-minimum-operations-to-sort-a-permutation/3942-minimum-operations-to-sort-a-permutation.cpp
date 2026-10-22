class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;

        bool increasing = true;
        bool decreasing = true;
        int zero = 0;

        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) zero = i;

            int next = nums[(i + 1) % n];

            if (next != (nums[i] + 1) % n)
                increasing = false;

            if (next != (nums[i] + n - 1) % n)
                decreasing = false;
        }

        if (increasing)
            return min(zero, n - zero + 2);

        if (decreasing)
            return 1 + min(n - 1 - zero, (zero + 1) % n);

        return -1;
    }
};