#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int lowerC(0), upperC(0);
    for (auto letter : s)
        if (isupper(letter))
            upperC += 1;
        else
            lowerC += 1;
    if (lowerC >= upperC)
        transform(s.begin(), s.end(), s.begin(), [](unsigned char c) { return std::tolower(c); });
    else
        transform(s.begin(), s.end(), s.begin(), [](unsigned char c) { return std::toupper(c); });


    cout << s;
}

