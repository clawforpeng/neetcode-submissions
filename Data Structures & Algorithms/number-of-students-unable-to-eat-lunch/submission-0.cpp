class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int sandwitchStart = 0;

        queue<int> studentsQ;

        for (int student: students) {
            studentsQ.push(student);
        }

        int orginalSize = students.size();
        while (!studentsQ.empty()) {
            for (int i = 0; i < orginalSize; i++) {
                int student = studentsQ.front();
                studentsQ.pop();
                if (sandwiches[sandwitchStart] == student) {
                    sandwitchStart++;
                }
                else {
                    studentsQ.push(student);
                }
            }
            if (orginalSize != studentsQ.size()) {
                orginalSize = studentsQ.size();
            }
            else {
                break;
            }
        }

        return studentsQ.size();
    }
};