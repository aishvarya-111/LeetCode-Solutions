
#define MAX(a, b) ((a > b)? a: b)
int find_max(int* nums, int numsSize){
    
    int max = INT_MIN;
    for(int i=0; i < numsSize; i++)
        if (nums[i] > max) max = nums[i];
    return max;
}

int lengthOfLIS(int* nums, int numsSize){
    
    int size[numsSize];
    size[0] = 1;
    
    for(int i=1; i < numsSize; i++){
        size[i] = 1;
        for(int j=0; j < i; j++){
            if (nums[i] > nums[j]) size[i] = MAX(size[j] + 1, size[i]);
        }
    }
    
    return find_max(size, numsSize);

}