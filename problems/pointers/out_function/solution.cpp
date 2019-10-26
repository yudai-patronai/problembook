
void print_no_space(char* text)
{
		for(; *text != '\0'; ++text){
				if (*text != ' '){
					printf("%c", *text);
				}
		}
}
