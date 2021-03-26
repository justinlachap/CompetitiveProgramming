// solution https://codeforces.com/problemset/problem/987/A

#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main()
{
	map<string, string> thanos;
	vector<string> input;
	vector<string> output;

	thanos["purple"] = "Power";
	thanos["green"] = "Time";
	thanos["blue"] = "Space";
	thanos["orange"] = "Soul";
	thanos["red"] = "Reality";
	thanos["yellow"] = "Mind";

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		input.push_back(s);
	}

	for (auto s : thanos)
	{
		bool b = false;
		for (string q : input)
		{
			if (q == s.first)
			{
				b = true;
				break;
			}
		}
		if (!b)
			output.push_back(s.second);
	}

	cout << 6 - n << endl;
	for (string s : output)
		cout << s << endl;
	return 0;
}

