class NumArray {
    prefixSum: number[] = [];

    constructor(nums: number[]) {
        this.prefixSum =[ ...[0], ...nums];
        this.initializePrefixSum();
    }
    
    private initializePrefixSum(){
        for(let i = 1; i < this.prefixSum.length; i++){
            this.prefixSum[i] += this.prefixSum[i - 1];
        }
    }

    sumRange(left: number, right: number): number {
        return this.prefixSum[right + 1] - this.prefixSum[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
