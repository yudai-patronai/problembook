#include <stdio.h>
#include <string.h>

int main(){
    unsigned long base;
    scanf("%lu", &base);
    char type[15];
    scanf("%s", type);

    if (strcmp(type, "ulint") == 0){
        printf("%lu", base);
    }
    
    if (strcmp(type, "lint") == 0){
        long int target =  * (long int *) &base;
        printf("%ld", target);
    }

    if (strcmp(type, "sint") == 0){
        short int *target =  (short int *) &base;
        for (int i = 0; i<(sizeof(long int)/sizeof(short int)); printf("%hd ", target[i++]));
    }
    
    if (strcmp(type, "usint") == 0){
        unsigned short int *target =  (unsigned short int *) &base;
        for (int i = 0; i<(sizeof(long int)/sizeof(unsigned short int)); printf("%hu ", target[i++]));
    }
    
    if (strcmp(type, "schar") == 0){
        char *target =  (char *) &base;
        for (int i = 0; i<(sizeof(long int)/sizeof(char)); printf("%c ", target[i++]));
    }
    
    if (strcmp(type, "dchar") == 0){
        short int *target =  (short int *) &base;
        for (int i = 0; i<(sizeof(long int)/sizeof(char)); printf("%hhd ", target[i++]));
    }
    
    if (strcmp(type, "uchar") == 0){
        short int *target =  (short int *) &base;
        for (int i = 0; i<(sizeof(long int)/sizeof(char)); printf("%hhu ", target[i++]));
    }
    
    if (strcmp(type, "float") == 0){
        float target =  * (float *) &base;
        printf("%f", target);
    }
    return 0;
}
