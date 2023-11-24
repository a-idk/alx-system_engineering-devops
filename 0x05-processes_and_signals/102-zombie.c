/* Title: zombie.c */

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - function that creates an infinite hanging loop
 * Return: NADA!
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program that creates 5 zombie processes
 * Description: For every zombie process created,
 *		it displays "Zombie process created, PID: ZOMBIE_PID"
 *		When the parent process and the zombies are created,
 *		the infinite_while funciton is called
 * Return: 0 on Success! (Always)
 */

int main(void)
{
	/* variables declaration */
	pid_t zom;  /* zom for zombie process */
	int index = 0;

	while (index < 5)
	{
		zom = fork();
		if (!zom)
			return (0);
		printf("Zombie process created, PID: %d\n", zom)
		index += 1;
	}
	infinite_while();
	return (0);
}
