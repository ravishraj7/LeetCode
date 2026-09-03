#include <stdbool.h>
#include <limits.h>

bool uniformArray(int* nums1, int numsSize) {
    bool hasOdd = false, hasEven = false;
    int minOdd = INT_MAX, minEven = INT_MAX;

    for (int i = 0; i < numsSize; i++) {
        if (nums1[i] % 2 == 0) {
            hasEven = true;
            if (nums1[i] < minEven) minEven = nums1[i];
        } else {
            hasOdd = true;
            if (nums1[i] < minOdd) minOdd = nums1[i];
        }
    }

    bool allEvenOk = !hasOdd;
    bool allOddOk = !hasEven || (hasOdd && minOdd < minEven);

    return allEvenOk || allOddOk;
}