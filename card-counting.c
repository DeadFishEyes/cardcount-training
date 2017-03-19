// made by Mauri Vanoro... for practicing blackjack


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void delay(int x);



int main()
{
	
	int set[5] = {0, 1, -1};
	int num, tn, f;
	int sec, a, b, c,d, e,interv;
	char s;
	int temp[5], sum = 0;
	srand(time(NULL));

	printf("#############################\n");
	printf("#                           #\n");
	printf("#                           #\n");
	printf("#      Cardu Countingu      #\n");
	printf("#        Mauri Vanoro       #\n");
	printf("#                           #\n");
	printf("#############################\n");

	start:
	printf("\nTime? >>> ");
	scanf("%d", &sec);
	printf("\nRounds? >>> ");
	scanf("%d", &interv);
	printf("\nTotal Numbers? >>> ");
	scanf("%d", &tn);
	printf("\n-------------------------------------\n\n");


	b = sec;
	sec = sec * 1000;
	c = 1;
	while(b > 0){

		for(a = 1; a<= interv; a++){

				printf("\n\t[");
				temp[1] = set[rand() % 3];
				printf("%d", temp[1]);

			for(d = 2; d <= tn; d++){

				temp[d] = set[rand() % 3];
				printf("\t%d", temp[d]);
			}

			printf("]");

			delay(sec);
			for(e = 1; e <= tn; e++){
				sum = sum + temp[e];
			}
			printf("\t\t:: %d", sum);
			sum = 0;
		}
		--b;
		sec = b * 1000;
		printf("\n-------------------------------------\n\n");

	}
	goto start;
	

	return 0;
}


void delay(int x)
{
	
	int i=0,j=0;
    for(i=0;i<x;i++){
   		for(j=0;j<200000;j++){
   	 	}
	}
}