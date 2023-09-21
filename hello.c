#include <stdio.h>

int main() {
  int a = 2;
  int b = 2;
  int c = a + b;

  printf("C says: Hello, World!\n");
  printf("%d + %d = %d\n",a,b,c);

  char* users[] = {"User1", "User2", "User3"};
  int num_users = sizeof(users) / sizeof(users[0]);

  for (int i = 0; i < num_users; i++) {
      printf("%s\n", users[i]);
  }

  return 0; 
}
