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
  HttpSocket() {}
  HttpSocket(string_t conn_dns) { 
    uri_builder conn_uri;
    conn_uri.set_host(conn_dns);
    conn_uri.set_port(80);

    client_ = new http_client(conn_uri.to_uri()); 
  }
  ~HttpSocket() { delete client_; }

  //Accessor for inbuf and outbuf
  string_t get_outbuf() { return outbuf_; }
  void set_inbuf(string_t input) { inbuf_ = input; }

  /* For http request ( it may be use for just send user id/pw
   *						and receive program definition.)
   * You must set _inbuf before use this function.
   */
  pplx::task<void> httpRequset(string_t req_uri);

private:
  string_t inbuf_, outbuf_;
  http_client *client_;
};

#endif