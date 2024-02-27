#include "stdio.h"

int foo(){
    return 10;
}
int main(){
    int a=foo();
    printf("%d",a);
    return 0;
}