#include "bits/stdc++.h"
using namespace std;

int main(){
	int arr[]={9,4,5,10,2,1,8,7,3,6};
	int n= sizeof(arr)/sizeof(arr[0]);
	for(int i=0;i<n-1;i++)
		for(int j=0;j<n-i-1;j++)
			if(arr[j]>arr[j+1])
			{
				int temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
	cout<<"Sort student"<<endl;
	for(int i=0;i<n;i++)
	cout<< arr[i]<<", ";
return 0;
}