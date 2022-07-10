#include <iostream>
#include <queue>
using namespace std;

int n,mid,m;
int a, b; // A와 B의 크기, 0으로 초기화

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	// A는 중간값을 기준으로 중간값보다 작은 수의 집합
	// B는 중간값을 기준으로 중간값보다 큰 수의 집합
	priority_queue<int> A; // 최대힙
	priority_queue< int, vector<int>, greater<int>> B; // 최소힙

	A.push(-10001); // 초기화(비교를 위해)
	B.push(10001); // 초기화(비교를 위해)

	cin >> n; // 정수의 개수 입력
	cin >> m; // 정수 입력
	mid = m; // 중간값 결정
	cout << mid << "\n"; // 중간값 출력
	for (int i = 1;i < n;i++) { // n-1번 반복
		cin >> m;
		if (m >= mid) { // 입력된 정수 값이 mid값과 같거나 크다면
			B.push(m); // B에 넣는다.
			b++; // b의 size 증가
		}
		else {
			A.push(m); // 입력된 정수 값이 mid값보다 작다면
			a++; // a의 size 증가
		}

		// A에서 원소를 꺼내야 하는 경우는 A집합의 원소의 수가 B보다 많아졌을 때
		// A집합에서 가장 큰 수가 나오게 해야 한다.
		// 시간복잡도 logn
		if (a > b) {
			B.push(mid);
			mid = A.top();A.pop();
			a--;b++;
		}
		// B에서 원소를 꺼내야 하는 경우는 B집합의 원소의 수가 A보다 2개 차이날 때
		// B집합에서 가장 작은 수가 나오게 해야 한다.
		// 시간복잡도 logn
		else if (a < b - 1) {
			A.push(mid);
			mid = B.top();B.pop();
			a++;b--;
		}
		cout << mid << "\n"; // 결과적으로 시간복잡도 n log n, 0.1초만에 수행할 수 있다.
	}
}