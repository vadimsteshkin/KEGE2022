#include <bits/stdc++.h>
using namespace std;
int main(){
    ifstream f("27B.txt");
    long long m,q,s,n,saas,k;
    f>>saas;
    q=0;
    m=0;
    n=1200050;
    k=2000000;
    vector <long long> a(n);
    for (long long i=0;i<n;i++){
        s=0;
        for (long long j=i+1;i<n; j++){
                s+=a[j];
                q++;
                if (s<=k);
                    if (q>m) m=q,q=1;
        }
    }
    cout<<m;
}
