 int longestCommonSubsequence(string text1, string text2) {
        int row = text1.length
        int col = text2.length
        int Table[row+1][col+1];
        int res = 0;
        for(int i = 0; i<=col ; i++){
            Table[0][i] = 0;
        }
        for(int i = 0; i<=row ; i++){
            Table[i][0] = 0;
        }

        for(int i = 1; i <= row; i++){
            for(int j = 1; j <= col; j++){
             if(text1[i-1] == text2[j-1]){
                Table[i][j] = Table[i-1][j-1] + 1;
             }  else{
                Table[i][j] = max(Table[i-1][j], Table[i][j-1])
             }
            }
        }
        return Table[row][col];
    }