#include <unistd.h>
#include <stdio.h>

int main(void)
{
	int counter;
	alarm(2);
	for(counter=0; 1; counter++)
		printf("counter=%d ", counter);
	return 0;
}
