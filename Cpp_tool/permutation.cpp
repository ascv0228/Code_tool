#include <iostream>
#include <string>

using namespace std;

void Permutation(string s, int first = 0, int end = 0)
{
    if(end == 0)
        end = s.length();
    if(first+1 == end)
        cout << s << endl;
    
    for(int k = first; k < end; k++)
    {
        swap(s[first], s[k]);
        Permutation(s, first+1, end);
        swap(s[first], s[k]);
    }
}

int main()
{
    string s = "abc";
    
    Permutation(s);
}
