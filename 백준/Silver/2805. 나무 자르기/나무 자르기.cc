#include <iostream>
#include <algorithm>
using namespace std;

int n,m;
int arr[1000005];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int num;
	int start = 0;
	int end = 0;
	int result = 0;

	cin >> n >> m;
	for (int i = 0;i < n;i++) {
		cin >> num;
		arr[i] = num;
		end = max(end, arr[i]);
	}
	while (start <= end) {
		long long total = 0;
		int mid = (int)(start + end) / 2;

		for (int i = 0;i < n;i++) {
			if (arr[i] > mid)
				total += arr[i] - mid;
		}
		if (total < m)
			end = mid - 1;
		else {
			result = mid;
			start = mid + 1;
		}
	}
	cout << result;
}