#include <stdio.h>
#include <unistd.h>


int main(int argc, char *argv[]) {
    int i;
    int j;

    char *python[]={"python3",NULL};
    char *script[]={"schedSim.py",NULL};
    char *args[argc+2];
    args[0] = python[0];
    args[1] = script[0];
    args[argc+1] = NULL;

    for (i = 1; i < argc; i++)
    {
        args[i+1] = argv[i];
    }

    execvp(args[0], args);
    return 0;
}