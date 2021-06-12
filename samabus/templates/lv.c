#include<stdio.h>
#include<stdlib.h>
int main(){
    int n[]={11,14,21,4,-1,24,14,20,-1,5,0,19,14,20},i;
    for(int j=0;j<14;j++){
        if(n[j]==-1)
         printf(" ");
        else{
            i=0;
            for(char c='a';c<='z';c++)
                if(i++==n[j]){
                    printf("%c",c);
                    break;
                }
        }
    }
    printf("\n");
    return 0;
}