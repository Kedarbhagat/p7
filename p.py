from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_c_program():
    c_program_code = '''  
#include<sys/types.h> #include<sys/stat.h> #include<stdio.h> #include<fcntl.h> main( int argc,char *argv[3] ) { int fd,i; char buf[2]; fd=open(argv[1],O_RDONLY,0777); if(fd==-argc) { printf("file open error"); } else { while((i=read(fd,buf,1))>0) { printf("%c",buf[0]); } close(fd); } }


#include <stdio.h> #include <stdlib.h> #include <fcntl.h> #include <errno.h> #include <unistd.h> #define BUFF_SIZE 1024 int main(int argc, char* argv[]) { int srcFD, destFD, nbread, nbwrite; char buff[BUFF_SIZE]; if(argc != 3) { printf("\nUsage: cpcmd source_file destination_file\n"); exit(EXIT_FAILURE); } srcFD = open(argv[1], O_RDONLY); if(srcFD == -1) { printf("\nError opening file %s errno = %d\n", argv[1], errno); exit(EXIT_FAILURE); } destFD = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH); if(destFD == -1) { printf("\nError opening file %s errno = %d\n", argv[2], errno); exit(EXIT_FAILURE); } while((nbread = read(srcFD, buff, BUFF_SIZE)) > 0) { if(write(destFD, buff, nbread) != nbread) { printf("\nError in writing data to %s\n", argv[2]); exit(EXIT_FAILURE); } } if(nbread == -1) printf("\nError in reading data from %s\n", argv[1]); if(close(srcFD) == -1) printf("\nError in closing file %s\n", argv[1]); if(close(destFD) == -1) printf("\nError in closing file %s\n", argv[2]); exit(EXIT_SUCCESS);}


#include <stdio.h> #include<unistd.h> int main(int argc, char *argv[]) { if(argc!=3) { printf("usage: %s <src_file><dest_file>\n",argv[0]); Return 0; } if(link(argv[1],argv[2])==-1) { printf("link error\n"); return 1; } printf("files linked\n"); printf("Inode number of linked files\n"); char str[100]; sprint(str,"ls –i %s %s \n",argv[1],argv[2]); system(str); return 0; }


#include <stdio.h> #include <sys/types.h> #include <fcntl.h> #include <stdlib.h> int main(int argc, char *argv[]) { int accmode, val; if (argc != 2) { fprintf(stderr, "usage: %s <description>", argv[0]); exit(1); } val = fcntl(atoi(argv[1]), F_GETFL, 0); if (val < 0) { perror("fcntl error for fd"); exit(1); } accmode = val & O_ACCMODE; if (accmode == O_RDONLY) printf("read only"); else if (accmode == O_WRONLY) printf("Write only"); else if (accmode == O_RDWR) printf("read write"); else { fprintf(stderr, "unknown access mode"); exit(1); } if (val & O_APPEND) printf(", append"); if (val & O_NONBLOCK) printf(", nonblocking"); if (val & O_SYNC) printf(", synchronous write"); putchar('\n'); exit(0); }


#include<stdlib.h> #include<unistd.h> #include<sys/types.h> #include<sys/stat.h> #include<fcntl.h> #include<stdio.h> int main(int argc, char **argv) { int fd, nfd; if (argc < 2) { printf("usage: %s pathname\n", argv[0]); exit(1); } if ((fd = open(argv[1], O_WRONLY)) < 0) { perror("Problem in opening the file"); exit(1); } if ((nfd = fcntl(fd, F_DUPFD, 0)) == -1) { perror("Problem in duplicating fd"); exit(1); } printf("Fd %d duplicated with %d\n", fd, nfd); close(fd); close(nfd); return 0; }


#include<stdio.h> #include<sys/types.h> #include<sys/stat.h> #include<time.h> #include<stdlib.h> int main(int argc, char *argv[]) { struct stat sb; if(argc != 2) { fprintf(stderr,"usage: %s <pathname>\n", argv[0]); exit(EXIT_FAILURE); } if(stat(argv[1], &sb) == -1) { perror("stat"); exit(EXIT_FAILURE); } printf("file type: "); switch(sb.st_mode & S_IFMT) { case S_IFBLK: printf("block device file\n"); break; case S_IFCHR: printf("character device file\n"); break; case S_IFDIR: printf("directory\n"); break; case S_IFIFO: printf("FIFO/pipe\n"); break; case S_IFLNK: printf("symlink\n"); break; case S_IFREG: printf("regular file\n"); break; case S_IFSOCK: printf("socket\n"); break; default: printf("regular file\n"); break; } printf("Inode number: %ld\n", (long) sb.st_ino); printf("Mode: %lo(octal)\n", (unsigned long) sb.st_mode); printf("Blocks allocated: %lld\n", (long long) sb.st_blocks); exit(EXIT_SUCCESS); }


#include<stdio.h> #include<stdlib.h> int main() { FILE *fp; char ch; int num; long length; printf("Enter the value of num:"); scanf("%d", &num); fp = fopen("file.txt", "r"); if (fp == NULL) { puts("Cannot open this file"); exit(1); } fseek(fp, -1, SEEK_END); length = ftell(fp); fseek(fp, (length - num), SEEK_SET); do { ch = fgetc(fp); putchar(ch); } while (ch != EOF); fclose(fp); return (0); }


#include<stdio.h> #include<sys/types.h> #include<sys/stat.h> #include<time.h> #include<stdlib.h> int main(int argc, char *argv[]) { struct stat sb; if(argc != 2) { fprintf(stderr,"usage: %s <pathname>\n", argv[0]); exit(EXIT_FAILURE); } if(stat(argv[1], &sb) == -1) { perror("stat"); exit(EXIT_FAILURE); } printf("file type: "); switch(sb.st_mode & S_IFMT) { case S_IFBLK: printf("block device file\n"); break; case S_IFCHR: printf("character device file\n"); break; case S_IFDIR: printf("directory\n"); break; case S_IFIFO: printf("FIFO/pipe\n"); break; case S_IFLNK: printf("symlink\n"); break; case S_IFREG: printf("regular file\n"); break; case S_IFSOCK: printf("socket\n"); break; default: printf("regular file\n"); break; } printf("Inode number: %ld\n", (long) sb.st_ino); printf("Mode: %lo(octal)\n", (unsigned long) sb.st_mode); printf("Blocks allocated: %lld\n", (long long) sb.st_blocks); exit(EXIT_SUCCESS); }

'''

    return render_template_string('<pre>{{ code }}</pre>', code=c_program_code)

