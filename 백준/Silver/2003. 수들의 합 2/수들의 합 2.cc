#include <iostream>

int n, m;
int arr[10005];
int count;
int inter_sum = 0;

using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;
	int num;
	int end = 0;
	int count=0;
	for (int i = 0;i < n;i++) {
		cin >> num;
		arr[i]= num;
	}
	for (int start = 0;start < n;start++) {
		while (inter_sum < m && end < n) {
			inter_sum += arr[end];
			end++;
		}
		if (inter_sum == m)
			count++;
		inter_sum -= arr[start];
	}
	cout << count;
	return 0;
}