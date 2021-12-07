#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <unistd.h>

using namespace std;

/*
项目背景：在ubuntu 16.04下利用mosquitto实现mqtt协议的本地回环，发送端每隔一分钟输出hello!到客户端
发送端与客户端均在终端上输出时间戳
运行于发送端，Ctrl + C终端死循环 
*/

int main()
{	
	cout << "testing every 1 minute"<<endl;
	int i = 1;

	while (1)
	{
		//get date and time according to the system
    	time_t now = time(0);

    	//change 'now' into string
		char* time_now = ctime(&now);

		cout << "test No." << i << " " << time_now;
		
		/*std::cout is row-buffering
		  using 'endl' or 'cout.flush()' can make it output immediately*/
		cout.flush();
		
		char pub[100];
		sprintf(pub, "mosquitto_pub -t 'temp' -m 'hello! %s'", time_now);
		system(pub);
		
		i++;
		sleep(60);  
		/*60 seconds. Requiring header 'unistd.h'
		  Sleep(60000) in windows systems, requiring header 'windows.h'*/
	}

	return 0;
}
