#include <stdio.h>
int main(){
	int n,m;
	scanf("%d %d",&n,&m);
	getchar();
	char table[n][m];
	char line[m+1];
	for(int i=0;i<n;i++){
		gets(line);
		for(int j=0;j<m;j++)
			table[i][j]=line[j];
	}
	//input complete
	for(int i=1;i<n-1;i++){
		for(int j=1;j<m-1;j++){
			int period=0;
			for(int k=i-1;k<=i+1;k++) 
				for(int l=j-1;l<=j+1;l++)
					if((k!=i||l!=j)&&table[k][l]=='.')
						period=1;
			if( period==0)
				for(int k=i-1;k<=i+1;k++) 
					for(int l=j-1;l<=j+1;l++)
						if(k!=i||l!=j)
							table[k][l]='~';
		}
	}
	//paint
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(table[i][j]=='#'){
				printf("NO");
				return 0;
			}
	//output
	printf("YES");
	return 0;
}
