function minimumOneBitOperations(n: number): number {
    let solution: number = 0;
    while (n){
        solution ^= n;
        n >>= 1
    }
    return solution;
};
