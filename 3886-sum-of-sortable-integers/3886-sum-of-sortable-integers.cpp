#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;
using ll = long long;

class Solution {
private:
    ull splitmix64(ull x) {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }

public:
    int sortableIntegers(vector<int>& nums) {
        int n = nums.size();

        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());

        int maxValue = *max_element(nums.begin(), nums.end());

        vector<ull> weight1(maxValue + 1);
        vector<ull> weight2(maxValue + 1);

        for (int value = 1; value <= maxValue; value++) {
            weight1[value] = splitmix64(value);
            weight2[value] = splitmix64(value + 123456789ULL);
        }

        vector<ull> numsHash1(n + 1, 0);
        vector<ull> numsHash2(n + 1, 0);
        vector<ull> sortedHash1(n + 1, 0);
        vector<ull> sortedHash2(n + 1, 0);

        for (int i = 0; i < n; i++) {
            numsHash1[i + 1] =
                numsHash1[i] + weight1[nums[i]];

            numsHash2[i + 1] =
                numsHash2[i] + weight2[nums[i]];

            sortedHash1[i + 1] =
                sortedHash1[i] + weight1[sortedNums[i]];

            sortedHash2[i + 1] =
                sortedHash2[i] + weight2[sortedNums[i]];
        }

        // badPrefix[i] counts descents among:
        // nums[0] > nums[1], ..., nums[i - 1] > nums[i]
        vector<int> badPrefix(n, 0);

        for (int i = 0; i + 1 < n; i++) {
            badPrefix[i + 1] =
                badPrefix[i] + (nums[i] > nums[i + 1]);
        }

        ll answer = 0;

        for (int k = 1; k <= n; k++) {
            if (n % k != 0) {
                continue;
            }

            bool sortable = true;

            for (int left = 0; left < n; left += k) {
                int right = left + k;

                // Check whether this block has the same multiset
                // as the corresponding sorted block.
                ull blockHash1 =
                    numsHash1[right] - numsHash1[left];

                ull blockHash2 =
                    numsHash2[right] - numsHash2[left];

                ull targetHash1 =
                    sortedHash1[right] - sortedHash1[left];

                ull targetHash2 =
                    sortedHash2[right] - sortedHash2[left];

                if (blockHash1 != targetHash1 ||
                    blockHash2 != targetHash2) {
                    sortable = false;
                    break;
                }

                // Count descents inside the block.
                int descents =
                    badPrefix[right - 1] - badPrefix[left];

                // Check circular descent from last to first.
                if (nums[right - 1] > nums[left]) {
                    descents++;
                }

                // A cyclic rotation can be sorted only when
                // the circular sequence has at most one descent.
                if (descents > 1) {
                    sortable = false;
                    break;
                }
            }

            if (sortable) {
                answer += k;
            }
        }

        return static_cast<int>(answer);
    }
};