#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void){
	for (int i=1;i<5;i++){
	pid_t pid=fork();

	if(pid==0){
	    	wait(NULL);
		char name[30];
        	printf("Enter name:\n ");
	        scanf("%s",name);
		printf("Child process -> %s, \n", name);
	exit(0);
	}
	else{
		printf("Job is done\n");
	}
	}
	return EXIT_SUCCESS;
}
