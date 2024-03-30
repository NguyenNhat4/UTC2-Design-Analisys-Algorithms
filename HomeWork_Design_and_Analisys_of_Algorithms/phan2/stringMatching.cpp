#include <iostream>
#include <string>

using namespace std;

int stringMatching(string text, string pattern) {
    int n = text.length();
    int m = pattern.length();
    
    int countComparisons = 0;
    
    for (int i = 0; i <= n - m; ++i) {
        int j;
        for (j = 0; j < m; ++j) {
            countComparisons++; 
            if (text[i + j] != pattern[j])
                break;
        }
        if (j == m)
            return i; 
    }
    return -1; 
}

int main() {
    string text = "Hello, how are you?";
    string pattern = "how";
    
    int index = stringMatching(text, pattern);
    
    if (index != -1)
        cout << "Pattern found at index " << index << endl;
    else
        cout << "Pattern not found" << endl;

    return 0;
}

