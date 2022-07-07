#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int n;
int arr[1000001];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	int j;
	int num = 0;
	vector<int> v;

	arr[0] = 1;
	arr[1] = 1;
	for (int i = 2;i < (int)sqrt(1000001) + 1;i++) {
		if (arr[i] == 0) {
			v.push_back(i);
			j = 2;
			while (i * j <= 1000001) {
				arr[i * j] = 1;
				j += 1;
			}
		}
	}
	arr[2] = 1;
	while (1) {
		cin >> num;
		int out = 0;
		int is_True = 0;
		if (num == 0)
			break;
		for (int i = 0;i < v.size();i++) {
			if (v[i] > num) {
				is_True = 1;
				break;
			}
			if (arr[num - v[i]] == 0 && arr[v[i]] == 0) {
				cout << num << " " << "= " << v[i] << " " << "+" << " " << num - v[i] << "\n"; //8 = 3 + 5
				out = 1;
				break;
			}
		}
		if (out == 1)
			continue;
		cout << "Goldbach's conjecture is wrong." << "\n";
	}
	//return 0;
}