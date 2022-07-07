#include <iostream>
using namespace std;

int n, k;
int arr[1005];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> k;
	int j;
	int count=0;
	arr[1] = 1;
	arr[0] = 1;

	for (int i = 2;i < n + 1;i++) {
		if (arr[i] == 0) {
			arr[i]=1;
			count += 1;
			//cout << count << " " << i << "\n";
			if (count == k) {
				cout << i << "\n";
				break;
			}
			j = 2;
			while (i * j <= n) {
				if (arr[i * j] == 0) {
					arr[i * j] = 1;
					count++;
					if (count == k) {
						cout<< i * j << "\n";
						break;
					}
					//cout << count << " " << i*j << "\n";
					if (count==k)
						cout<< i * j << "\n";
				}
				j += 1;
			}
		}
	}
}