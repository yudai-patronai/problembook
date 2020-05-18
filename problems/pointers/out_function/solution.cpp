
void print_no_space(char* text)
{
	for(; *text != '\0'; ++text){
		if (*text != ' '){
			if (*text >= 'A' and *text <= 'Z') {
				*text -= 'A';
				*text += 'a';
			}
			printf("%c", *text);
		}
	}
}
