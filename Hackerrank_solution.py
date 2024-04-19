


#Question 1:

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int diagonalDifference(vector<vector<int>> arr) {
    int primary_sum = 0;
    int secondary_sum = 0;
    int n = arr.size(); // Assuming arr is a square matrix

    // Calculate the sum of the primary and secondary diagonals
    for (int i = 0; i < n; i++) {
        primary_sum += arr[i][i];
        secondary_sum += arr[i][n - i - 1];
    }

    // Return the absolute difference between the sums
    return abs(primary_sum - secondary_sum);
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), [](unsigned char ch) {
            return !isspace(ch);
        })
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
            return !isspace(ch);
        }).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<vector<int>> arr(n);

    for (int i = 0; i < n; i++) {
        arr[i].resize(n);

        string arr_row_temp_temp;
        getline(cin, arr_row_temp_temp);

        vector<string> arr_row_temp = split(rtrim(arr_row_temp_temp));

        for (int j = 0; j < n; j++) {
            int arr_row_item = stoi(arr_row_temp[j]);

            arr[i][j] = arr_row_item;
        }
    }

    int result = diagonalDifference(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}




#Question 2:

def rotateLeft(d, arr):
    for i in range(d):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        arr[len(arr)-1]=temp    
    return arr  




#Question 3:

import math
import os
import random
import re
import sys


# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.


def counterGame(n):
    answer= ["Louise","Richard"]
    count = 0
    summer = n
    while summer!=1:
        modulus = summer - 2**(math.log(summer)//math.log(2))
        if modulus!=0:
            summer = modulus
        else:
            summer = summer/2
        if summer!=1:
            count+=1
    return answer[count%2]                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()




#Question 4:
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    format_ = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, format_)
    t2 = datetime.strptime(t2, format_)
    return str(int(abs((t1-t2).total_seconds()))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()




