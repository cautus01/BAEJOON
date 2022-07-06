#include <iostream>
using namespace std;

int N, M, K;
long long tree[1024 * 1024 * 2];
int tmpN;

void update(int a, long long b) {
	a = a + tmpN - 1;
	tree[a] = b;
	while (a > 1) {
		a = a >> 1;
		tree[a] = tree[a * 2] + tree[a * 2 + 1];
	}
}

long long get_sum(int a, int b) {
	a = a + tmpN - 1;
	b = b + tmpN - 1;
	long long sum = 0;

	while (a <= b) {
		if (a % 2 == 1) sum+=tree[a];
		if (b % 2 == 0)
			sum += tree[b];
		a = (a + 1) / 2;
		b = (b - 1) / 2;
	}
	return sum;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M >> K; // N, M, K 입력받기
	// 1. tree의 크기 구하기
	// leafNode의 최대값 N 1,000,000
	// tree의 크기는 leafNode의 개수*2
	// leafNode의 개수는 반드시 N이 아니다.
	// 왜냐하면 N=6일 때, leafNode의 개수는 8이기 때문이다.
	// tmpN=leafNode의 개수, leafNode의 개수를 따로 나타내는 변수 필요
	for (tmpN = 1;tmpN < N;tmpN *= 2);
	// 2. tree의 값 초기화
	// 2-1. leafNode 값 초기화
	for (int i = 0;i < N;i++) {
		cin >> tree[tmpN + i];
	}
	for (int i = tmpN + N;i < tmpN * 2;i++) tree[i] = 0;
	// 2-2. interval Node 값 초기화;

	for (int i = tmpN - 1;i >= 1;i--) {
		tree[i] = tree[i * 2] + tree[i * 2 + 1];
	}

	for (int q = 0;q < M + K;q++) {
		long long a, b, c;
		cin >> a >> b >> c;

		if (a == 1) {
			// 3. update
			update(b, c);

		}
		else {
			// 4. 구간합 구하기
			cout <<  get_sum(b, c) << "\n";
		}
	}
	return 0;
}