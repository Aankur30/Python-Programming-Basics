#include<iostream>
using namespace std;

int main(){
    int n=0;
cout<<"enter the number you want to print "<<endl;

cin>>n;

for(int i=0;i<n;i++){
    for(int j=0;j<i+1;j++)
    {
        cout<<j+1<<" "<<endl;
    }
    cout<<endl;
}
    
    return 0;
}