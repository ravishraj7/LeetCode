bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    bool rows[9][9] = {false};
    bool cols[9][9] = {false};
    bool boxes[9][9] = {false};

    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            char ch = board[r][c];
            if (ch == '.') continue;

            int num = ch - '1';  
            int boxIdx = (r / 3) * 3 + (c / 3);

            if (rows[r][num] || cols[c][num] || boxes[boxIdx][num]) {
                return false;
            }

            rows[r][num] = true;
            cols[c][num] = true;
            boxes[boxIdx][num] = true;
        }
    }

    return true;
}