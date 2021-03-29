#include<bits/stdc++.h>
using namespace std;
int main(){
    //char s[1000];
    string s;
    int entripy=0;
    //gets(s);
    getline(std::cin,s);
    for(int i=0;i<s.size();i++){
        if(s[i]>=65 && s[i]<=90) entripy+=s[i];
        else if(s[i]>=97 &&s[i]<=122) entripy+=s[i];  
        }
        printf("%d",entripy);
}