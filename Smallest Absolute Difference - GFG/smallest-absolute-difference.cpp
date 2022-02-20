// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

int kthDiff(int a[], int n, int k);

// Driver code
int main() {
    int t, i;
    int k;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        cin >> k;

        cout << kthDiff(a, n, k) << endl;
    }
    return 0;
}
// } Driver Code Ends


int sliding(int diff,int arr[],int n)
{
     //how many pairs have absolute diff less than or 
     //equal to diff
     
     int j =0;
     int count=0;
     for(int i=1;i<n;i++)
     {   
         while(arr[i]-arr[j]>diff)j++;
          count+=i-j;
     }
    return count;
    
}

int kthDiff(int arr[], int n, int k)
{    
      
      sort(arr,arr+n);
      
      int high = arr[n-1]-arr[0];
      int low =INT_MAX;
      
      for(int i=1;i<n;i++)
      {
          if(arr[i]-arr[i-1]<low)
          low = arr[i]-arr[i-1];
      }
      
      
      while(low<high)
      {
          int mid = (low+high)/2;
          int ans = sliding(mid,arr,n); // mid = 5
          // how many pairs have absolute difference 
          //less than or equal to 5
          if(ans<k)  
          low = mid+1;
          else high = mid;
      }
      
      return low;
}