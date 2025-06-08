#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2){
        printf("CULPA: Usage: scriptorium <script_path>\n");
        return 1;
    }

    char* scriptoriumHome = getenv("SCRIPTORIUM_HOME");

    if(!scriptoriumHome){
        printf("CULPA: No SCRIPTORIUM_HOME environment variable set.\n");
        return 1;
    }

    char command[512];

    snprintf(command, sizeof(command), "%s\\venv\\Scripts\\python %s\\main.py %s", scriptoriumHome, scriptoriumHome, argv[1]);
    int result = system(command);

    return result;
}