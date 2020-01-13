// Program to find time complexities of functions
// Name : Vikas More
// Roll : 539

#include <stdio.h> 
#include<time.h>

void BigO_of_1() 
{ 
    printf("Hello World \n");  
} 

void BigO_of_n(int n) 
{ 
    int i; 
    for (i = 1; i <= n; i++) 
    { 
        printf("Hello World \n"); 
    } 
} 

void BigO_of_n2(int n)
{
	int i,j;
	for (i = 1; i <=n; i++) 
	{
		for (j = 1; j <=n; j++) 
		{
   			printf("Hello World\n");
		}
	}
}
void main()
{
	double total_time;
	clock_t start, end;
	start = clock();

	//time count starts 
	BigO_of_1();
	end = clock();
	//time count stops 

	total_time = ((double) (end - start)) / CLOCKS_PER_SEC;
	//calulate total time
	printf("\nTime taken is: %f\n\n", total_time);-*
	
	start = clock();

	//time count starts 
	BigO_of_n(3);
	end = clock();
	//time count stops
 
	total_time = ((double) (end - start)) / CLOCKS_PER_SEC;
	//calulate total time
	printf("\nTime taken is: %f\n\n", total_time);

	start = clock();

	//time count starts 
	BigO_of_n2(3);
	end = clock();
	//time count stops 

	total_time = ((double) (end - start)) / CLOCKS_PER_SEC;
	//calulate total time
	printf("\nTime taken is: %f\n\n", total_time);
	
		
}







