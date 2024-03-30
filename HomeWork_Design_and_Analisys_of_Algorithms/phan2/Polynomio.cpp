#include <iostream>
#include <vector>

using namespace std;

int polynomialEvaluation(vector<int>& coefficients, int x) {
    int result = 0;
    
    int countAssignments = 0;
    int countComparisons = 0;
    
    int n = coefficients.size();
    for (int i = 0; i < n; ++i) {
        countAssignments++; 
        result += coefficients[i] * pow(x, i);
        countComparisons++; 
    }
    
    cout << "Number of assignments: " << countAssignments << endl;
    cout << "Number of comparisons: " << countComparisons << endl;
    
    return result;
}

int main() {
    vector<int> coefficients = {3, 0, 2, 5};
    int x = 2;
    
    int result = polynomialEvaluation(coefficients, x);
    
    cout << "Result of polynomial evaluation: " << result << endl;

    return 0;
}

