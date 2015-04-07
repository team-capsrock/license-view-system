#include <iostream>

#include "HttpSocket.h"
#include "UserID.h"
#include "ProgramConnector.h"

int main(void){
  HttpSocket client(U("www.google.com"));
  UserID userid;
  ProgramConnector pconn;

  client.httpRequset(U("/")).wait();

  std::wcout << client.get_outbuf() << std::endl;

  system("pause");

  return 0;
}