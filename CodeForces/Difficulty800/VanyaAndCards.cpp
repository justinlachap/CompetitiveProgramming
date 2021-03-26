#include <iostream>
#include <vector>
#include <numeric>
#include <cstdlib>
#include <numeric>
#include <functional>


using namespace std;

int main()
{
	int n(0), x(0);
	cin >> n >> x;
	vector<int> v;
	for (int i = 0; i < n; i++)
	{
		int card;
		cin >> card;
		v.push_back(card);
	}
	int s(0);
	for (auto& e : v)
		s += e;

	if (s == 0)
		cout << 0;
	else if (abs(s) <= x)
		cout << 1;
	else
	{
		if (s % x == 0)
			cout << abs(s) / x;
		else
			cout << abs(s) / x + 1;
	}
	return 0;
}

