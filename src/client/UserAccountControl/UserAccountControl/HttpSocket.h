#ifndef LVS_HTTP_CLIENT_H_
#define LVS_HTTP_CLIENT_H_

#include <iostream>
#include <cpprest/http_client.h>
#include <cpprest/streams.h>

using namespace web;
using namespace web::http;
using namespace web::http::client;

using namespace utility;

class HttpSocket {
public:
  //Accessor for inbuf and outbuf
  string_t get_outbuf() { return outbuf_; }
  void set_inbuf(string_t input) { inbuf_ = input; }

  /* For http request ( it may be use for just send user id/pw
   *						and receive program definition.)
   * You must set _inbuf before use this function.
   */
  bool httpRequset(void);

private:
  string_t inbuf_, outbuf_;
  http_client *client_;

public:
  inline static HttpSocket* getInstance(string_t conn_uri) {
    if (instance == nullptr) {
      instance = new HttpSocket;

      uri conn(conn_uri);
      
      instance->client_ = new http_client(conn);
    }

    return instance;
  }

protected:
  HttpClient() {}
  ~HttpClient() {}

private:
  static HttpClient *instance;
};

#endif