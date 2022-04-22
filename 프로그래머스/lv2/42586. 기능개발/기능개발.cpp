#include <string>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> result;
    ios::sync_with_stdio(0);
    cin.tie(0);
    for(int i=0;i<progresses.size();i++){
        double speed=speeds[i];
        int day=ceil((100-progresses[i])/speed);
        result.push_back(day);
    }
    int day_compare=result[0];
    int index=0;
    answer.push_back(1);
    for(int i=1;i<result.size();i++){
        if (result[i]<=day_compare){
            answer[index]+=1;
        }
        else{
            day_compare=result[i];
            answer.push_back(1);
            index+=1;
        }
    }
    return answer;
}