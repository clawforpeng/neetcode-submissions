class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> sol;

        int m = matrix.size();
        int n = matrix[0].size();

        int top = 0;
        int bottom = m - 1;

        int left = 0;
        int right = n - 1;

        while (top <= bottom and left <= right) {
            for (int c = left; c <= right; c++) {
                sol.push_back(matrix[top][c]);
            }

            for (int r = top + 1; r < bottom; r++) {
                sol.push_back(matrix[r][right]);
            }

            if (top < bottom) {
                for (int c = right; c >= left; c--) {
                    sol.push_back(matrix[bottom][c]);
                }
            }

            if (left < right) {
                for (int r = bottom - 1; r > top; r--) {
                    sol.push_back(matrix[r][left]);
                }
            }

            top++;
            bottom--;
            left++;
            right--;
        }

        return sol;
    }
};
