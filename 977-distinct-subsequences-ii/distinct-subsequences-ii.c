#define MOD 1000000007

int distinctSubseqII(char* s) {
    long long dp[26] = {0};
    long long total = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        int c = s[i] - 'a';
        long long newVal = (total + 1) % MOD;
        total = (total - dp[c] + newVal + MOD) % MOD;
        dp[c] = newVal;
    }

    return (int)total;
}