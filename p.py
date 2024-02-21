from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_c_program():
    c_program_code = '''
    #include<stdio.h>
    #include<stdlib.h>
    int main()
    {
        FILE *fp;
        char ch;
        int num;
        long length;
        printf("Enter the value of num:");
        scanf("%d", &num);
        fp = fopen("file.txt", "r");
        if (fp == NULL)
        {
            puts("Cannot open this file");
            exit(1);
        }
        fseek(fp, -1, SEEK_END);
        length = ftell(fp);
        fseek(fp, (length - num), SEEK_SET);
        do
        {
            ch = fgetc(fp);
            putchar(ch);
        } while (ch != EOF);
        fclose(fp);
        return (0);
    }
    '''

    return render_template_string('<pre>{{ code }}</pre>', code=c_program_code)

