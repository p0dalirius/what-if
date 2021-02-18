#include <stdlib.h>
#include <stdio.h>

int main(int argc, char const *argv[]) {
    printf("=============== Infinite memory allocator - v1.0.1 ===============\n");
    long long int k = 0;
    while (1) {
        // Creates the zone in memory
        char * mem = malloc(1000000);
        k += 1;
        // Use the zone to prevent bypass by optimization
        mem[0]     = '\0';
        printf("\r[LOG] Allocated %lld", k);
    }
    return 0;
}
