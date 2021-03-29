#include<bits/stdc++.h>
using namespace std;
int tree[100][2]; // tree[left,right]
void printInorder(int node)
{
    if (node == -1)
        return;
    printInorder(tree[node][0]);
    cout << node<< " ";
    printInorder(tree[node][1]);
}
void printPostorder(int node)
{
    if (node == -1)
        return;
    printPostorder(tree[node][0]);
    printPostorder(tree[node][1]);
    cout << node << " ";
}
void printPreorder(int node)
{
    if (node == -1)
        return;
    cout << node << " ";
    printPreorder(tree[node][0]);
    printPreorder(tree[node][1]);
}
int main(){
	memset(tree, -1, sizeof(tree));
	freopen("in.txt","r",stdin);
	int n,d,l,r;
	int root=-1;
	cin>>n;  ///number of node
	for(int i=0;i<n;i++){
		cin>>d>>l>>r;  ///data  left  right
		tree[d][0]=l;
		tree[d][1]=r;
		if(root==-1) root=d;
	}
	cout<<"In order:"<<endl;
	printInorder(root);
	cout<<"\n\npost order:"<<endl;
	printPostorder(root);
	cout<<"\n\npre order:"<<endl;
	printPreorder(root);
}
