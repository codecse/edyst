
// Python:

def diagonal_difference(arr):
    n = len(arr)
    primary_diagonal_sum = sum(arr[i][i] for i in range(n))
    secondary_diagonal_sum = sum(arr[i][n - 1 - i] for i in range(n))

    absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    return absolute_difference

# Example usage:
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = diagonal_difference(matrix)
print(result)


// c++:

#include <iostream>
#include <vector>
using namespace std;

int absDiffOfDiag(vector<vector<int>> &mat){
  int n = mat.size();
  int leftToRightDiagSum = 0;
  int rightToLeftDiagSum = 0;
  for(int i = 0; i < n; i++){
    leftToRightDiagSum += mat[i][i];
    rightToLeftDiagSum += mat[i][n - i - 1];
  }
  int absDiffDiag = abs(leftToRightDiagSum - rightToLeftDiagSum);

  return absDiffDiag;
}

int main() {
  int n;
  cin >> n;
  vector<vector<int>> matrix(n, vector<int>(n));

  for(int i = 0; i < matrix.size(); i++){
    for(int j = 0; j < matrix[i].size(); j++){
      cin >> matrix[i][j];
    }
  }
  int ans = absDiffOfDiag(matrix);
  cout << ans;

  return 0;
}
