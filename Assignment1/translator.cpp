#include <stdio.h>
#include <string.h>
#define LINE_LEN     128

int main(){
char fileOrig[32] = "32-bit.asm";
char fileRepl[32] = "translated-64-bit.asm";

char *find[] = {"pushl", "ebp","movl", "subl","cfi_def_cfa 4, 4","cfi_def_cfa_register 5"};
char *replace[] = { "pushq","rbp","movq","subq","cfi_def_cfa 7, 8","cfi_def_cfa_register 6"};

char buffer[LINE_LEN+2];
char *buff_ptr, *find_ptr;
FILE *fp1, *fp2;
int buff_int;


fp1 = fopen(fileOrig,"r");
fp2 = fopen(fileRepl,"w");
buff_int=(int)buffer;
int i=0;
for(i=0;i<4;i++){
size_t find_len = strlen(find[i]);
while(fgets(buffer,LINE_LEN+2,fp1)){
    buff_ptr = buffer;
    while ((find_ptr = strstr(buff_ptr,find[i]))){
        while(buff_ptr < find_ptr)
            fputc((int)*buff_ptr++,fp2);
        fputs(replace[i],fp2);
        buff_ptr += find_len;
    }
    fputs(buff_ptr,fp2);
}
}
fclose(fp2);
fclose(fp1);
return 0;
}
