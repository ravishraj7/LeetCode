int countCommas(int n) {
    long long total = 0;
    long long low = 1, high = 9;
    int d = 1;
    while (low <= (long long)n) {
        long long upper = high < n ? high : n;
        long long count = upper - low + 1;
        total += count * ((long long)(d - 1) / 3);
        low = high + 1;
        high = high * 10 + 9;
        d++;
    }
    return (int)total;
}