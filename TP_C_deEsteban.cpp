#include <iostream> 
#include <time.h>
#define prob_Crossover 0.75
#define prob_Mutacion 0.05
#define N 30 //Cromosomas totales
#define M 30 //Genes totales

void Funcion_Fitness(unsigned long int [10],double ,double *);
bool Ya_esta (unsigned long int,int [10]);
double Funcion_Objetivo(unsigned long int );
void Mostrar_Lista (unsigned long int[10],int[10][M],double,  double *);
void CrossOver(double [],int[10],int [10][M]);
void A_Valor_Decimal(unsigned long int[10],int [10][M]);
double Sumatoria_Funcion_Objetivo(unsigned long int[10]);

int main(){
	
	int poblacion[N][M];
    double Fitness[10];
	int Nueva_Poblacion [10][M];
	double SumatoriaFObj;
	unsigned long int valor_Cromosomas_Elegidos[10];
	int cromosomas_Elegidos[10]; //cromosomas elegidos inicialmente 
	
	srand(time(0));

	for(int i=0; i<N ; i++)
	{
		for(int j=0; j<M ; j++)
			 poblacion[i][j] = rand()%2;
	}
	
	for(int k=0;k<10;k++)
		cromosomas_Elegidos[k]=-1;

	for(int j=0; j<10 ; j++)
	{
		int m=(rand()%M);
		while(Ya_esta(m,cromosomas_Elegidos)==false)
			m = (rand()%M);
		cromosomas_Elegidos[j]=m;
	}
	for(int k=0;k<10;k++){
		for(int j=0;j<M;j++){
			Nueva_Poblacion[k][j] = poblacion[cromosomas_Elegidos[k]][j] ;}
	}
	for(int i=0;i<20;i++){
		printf("\nEJECUCION NUMERO %d \n\n", i);
		A_Valor_Decimal(valor_Cromosomas_Elegidos,Nueva_Poblacion);
		SumatoriaFObj = Sumatoria_Funcion_Objetivo(valor_Cromosomas_Elegidos);
		Funcion_Fitness(valor_Cromosomas_Elegidos,SumatoriaFObj,Fitness);
		Mostrar_Lista(valor_Cromosomas_Elegidos,Nueva_Poblacion,SumatoriaFObj,Fitness);
		CrossOver(Fitness,cromosomas_Elegidos,Nueva_Poblacion);
		system("PAUSE");
		system("CLS");
	}		
	system("PAUSE");
	
	return 0;
}

bool Ya_esta(unsigned long int m,int cromosomas_Elegidos[10])
{
	for(int i=0;i<10; i++)
	{
		if(m==cromosomas_Elegidos[i])
			return false;
	}

	return true;
}

double Funcion_Objetivo(unsigned long int x)
{
	return (x/(pow(2.0,30) - 1 ) );
}

void Mostrar_Lista(unsigned long int valor_Cromosomas_Elegidos[10],int Nueva_Poblacion[10][M] ,double sumatoria,double *Fitness)
{
	
	for(int j=0; j<10 ; j++)
	{
		for(int i=0; i<N ; i++)
				printf( "%d" , Nueva_Poblacion[j][i] );
		printf( "     %d", valor_Cromosomas_Elegidos[j]);
		printf( "        %g", Funcion_Objetivo(valor_Cromosomas_Elegidos[j]));
		printf( "        %g", Fitness[j]);
		printf("\n");
	}
}

void Funcion_Fitness(unsigned long int valor_Cromosomas_Elegidos[10],double sumatoria,double *Fitness)
{
	for(int j=0; j<10 ; j++)
	{
		Fitness[j] = Funcion_Objetivo(valor_Cromosomas_Elegidos[j])/sumatoria;
	}
}

void CrossOver (double Fitness[], int cromosomas_Elegidos[10],  int Nueva_Poblacion[10][M])
{
	int Ruleta [100];
	int j=0;
	while(j<100){
		int y = rand()%10 ;
		int x= Fitness[y] * 100;
		for(int i=0; i<x;i++){
			if(j<100){
				Ruleta[j]=y;
				j=j+1;}
		}
	}
	for(int i=0;i<5;i++)
	{
		printf("\nTiro de ruleta numero: %d \n",i+1);
		int valor1, valor2;
		valor1=rand()%100; 
		valor1=Ruleta[valor1];
		valor2=rand()%100;
		valor2=Ruleta[valor2]; 
		if(rand()%100 / 100.0<prob_Crossover)
		{
			int punto = rand()%M;
			int k=0;
			printf("\nCORTE EN EL PUNTO: %d \n",punto);
			printf("\nPadre 1: ");
			for(j=0;j<30;j++)
			{
				printf("%d",Nueva_Poblacion[valor1][j]);
			}
			printf("\n");
			printf("\nPadre 2: ");
			for(j=0;j<30;j++)
			{
				printf("%d",Nueva_Poblacion[valor2][j]);
			}
			for(k;k<punto;k++)
			{
				Nueva_Poblacion[i*2][k] = Nueva_Poblacion[valor1][k];
				Nueva_Poblacion[i*2+1][k] = Nueva_Poblacion[valor2][k];
			}
			for(k;k<M;k++)
			{
				Nueva_Poblacion[i*2][k] = Nueva_Poblacion[valor2][k];
				Nueva_Poblacion[i*2+1][k] = Nueva_Poblacion[valor1][k];
			}
			
			printf("\n");
			for(int y=0; y<2;y++) //Para los dos hijos
			{
				printf("\n");
				printf("Hijo %d: ",y+1);
				if(rand()%100 / 100.0<prob_Mutacion)
				{
					int gen = rand()%M;
					if(Nueva_Poblacion[i*2+y][gen]==1)
						Nueva_Poblacion[i*2+y][gen] = 0;
					else
						Nueva_Poblacion[i*2+y][gen] = 1;
					
					printf(" Ha mutado en el gen numero: %d \n",gen);
				}
				for(j=0;j<30;j++)
				{
					printf("%d",Nueva_Poblacion[i*2+y][j]);
				}
			
			}
			printf("\n");
		}
		else
			printf("\nNo hubo CrossOver\n\n");
	}
}

void A_Valor_Decimal(unsigned long int valor_Cromosomas_Elegidos[10], int Nueva_Poblacion[10][M])
{
	
	for(int j=0;j<10;j++)
	{
		valor_Cromosomas_Elegidos[j]=0;
		int in =0;
		for(int i=29; i>=0 ; i--){
			valor_Cromosomas_Elegidos[j]= Nueva_Poblacion[j][i]*pow(2.0,in) + valor_Cromosomas_Elegidos[j];
			in++;
		}
	}
}

double Sumatoria_Funcion_Objetivo(unsigned long int valor_Cromosomas_Elegidos[10])
{
	double acumulador=0;
	for(int j=0;j<10;j++)
		acumulador = acumulador + Funcion_Objetivo(valor_Cromosomas_Elegidos[j]) ;

	return acumulador;
}
