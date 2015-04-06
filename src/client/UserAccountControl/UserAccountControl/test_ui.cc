#include <iostream>

#include "HttpSocket.h"
#include "UserID.h"
#include "ProgramConnector.h"

int main(void){
  HttpSocket *client = HttpSocket::getInstance(U("127.0.0.1"));
  UserID userid;
  ProgramConnector pconn;

  userid.InputUserInfo(U("ghost242"), U("asdf1234"));

  client->set_inbuf(userid.serialize);

  client->httpRequset();

  pconn.unserialize(client->get_outbuf());

  std::cout << pconn.get_license_type() << " " << pconn.get_end_date() << std::endl;

  return 0;
}