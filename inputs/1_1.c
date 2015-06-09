/*
 ============================================================================
 Name        : zad2.c
 Author      : PiotrNiedrygas
 Version     :
 Copyright   : Systemy Operacyjne 2012
 Description : zad2 in C, Ansi-style
 ============================================================================
 */
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#define ABC

void usage() {
	printf("[nazwa][pid_do ktorego przesle][kill/queue][opcjonalnie-dla-queue-ilosc]\n");
}

int main(int argc, char *argv[]) {
	printf("pid = %d\n", (int) getpid());
	int pid;
	int option = 1;
	int val;
	if (argc == 3) {
		if (strcmp(argv[2], "kill") != 0) {
			perror("Bledna opcja\n");
			exit(1);
		} else
			option = 0;
		pid = atoi(argv[1]);
	} else if (argc == 4) {
		if (strcmp(argv[2], "queue") != 0) {
			perror("Bledna opcja\n");
			exit(1);
		}
		val = atoi(argv[3]);
		pid = atoi(argv[1]);
	} else {
		usage();
		exit(1);
	}
    int i = 5;
	if (option == 0) {
		if (kill(pid, SIGUSR1) != 0)
			perror("Blad killa\n");
	} else {
		union sigval value;
		value.sival_int = val;
		sigqueue(pid, SIGUSR1, value);
	}
	return EXIT_SUCCESS;
}











