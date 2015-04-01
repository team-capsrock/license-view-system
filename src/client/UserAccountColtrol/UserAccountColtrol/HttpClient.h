#ifndef LVS_HTTP_CLIENT_H_
#define LVS_HTTP_CLIENT_H_

#include <cpprest/http_client.h>

using namespace web;
using namespace web::http;
using namespace web::http::client;

using namespace utility;

class HttpClient
{
public:
	//Accessor for inbuf and outbuf
	string_t get_outbuf() { return _outbuf; }
	void set_inbuf(string_t input) { _inbuf = input; }

	/* For http request ( it may be use for just send user id/pw 
	 *						and receive program definition.) 
	 * You must set _inbuf before use this function.
	 */
	bool httpRequset(void);
	
private:
	string_t _inbuf, _outbuf;
	http_client *_client;

public:
	inline static HttpClient* getInstance()
	{
		if (instance == nullptr)
		{
			instance = new HttpClient;

			uri conn(L"ec2-52-68-13-153.ap-northeast-1.compute.amazonaws.com");
			instance->_client = new http_client(conn);
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