#include <iostream>
#include <conio.h>
#include <thread>
#include <condition_variable>
#include <mutex>
#include <chrono>
#include <vector>

using namespace std;

mutex mx;
condition_variable cv;


class GoBackN
{
private:
	vector<int> Window;

	vector<int> Shared_Channel;
	vector<int> ACK_Buffer;

	int Wc; // Window_Counter
	int Ws; // Window_Size
	int Sn; // Sequence_Number
	int Sb;
	int Sm;
	int Rn;

	int Error_Rate;
	int Error_Rate_Ack;

public:
	GoBackN();
	~GoBackN();
	void Sender();
	void Receiver();

	void Sliding_Window();
	void Sending_Window();
	void Shifiting_Window();


};

GoBackN::GoBackN()
{
	cout << " Please enter Window Size : ";
	cin >> Ws;
	cout << " Please enter Error Rate : ";
	cin >> Error_Rate;
	cout << " Please enter Error Rate for Ack : ";
	cin >> Error_Rate_Ack;

	Wc = 0;
	Sn = Ws + 1;
	Sb = 1;
	Sm = Ws;
	Rn = 1;

	//initiating Window
	for (int i = Sb; i < Sn; i++)
	{
		Window.push_back(i);
	}
	
	thread _receiver_th(&GoBackN::Receiver, this);
	thread _Sender_th(&GoBackN::Sender, this);
	
	

	_Sender_th.join();
	_receiver_th.join();
	
}

GoBackN::~GoBackN()
{
}


void GoBackN::Sliding_Window()
{
	int fault;
	int Err_Ac;	
	{
		Err_Ac = (rand() % ((100 - 0) + 1)) + 0;
		if (Err_Ac <= Error_Rate)
		{
			fault = (Window.back() * 10) + Window.back();
			Shared_Channel.push_back(fault);
			printf("\n 1) Sender :  Sends %d to Receiver ! <We have fault here> ", fault);
			printf("\n");
		}
		else
		{
			Shared_Channel.push_back(Window.back());
			printf("\n 1) Sender :  Sends %d to Receiver ! ", Window.back());
			printf("\n");
		}
	}

	
}

void GoBackN::Sending_Window()
{
	int fault;
	int Err_Ac;

	//srand((unsigned int)time(0));

	for (int i = 0; i < Window.size(); i++)
	{
		Err_Ac = (rand() % ((100 - 0) + 1)) + 0;
		if (Err_Ac <= Error_Rate)
		{
			fault = (Window[i] * 10) + Window[i];
			Shared_Channel.push_back(fault);
			printf("\n 1) Sender :  Sends %d to Receiver ! ==> (Window Sending %d )  <We have fault hear> ", fault, Wc);

		}
		else
		{
			Shared_Channel.push_back(Window[i]);
			printf("\n 1) Sender :  Sends %d to Receiver !  ==> (Window Sending %d )", Window[i], Wc);
		}

	}	
	Wc++;
	printf("\n");
}

void GoBackN::Shifiting_Window()
{
	int tmp;
	for (int i = 0; i <  Window.size(); i++)
	{
		tmp = Window[i];
		tmp = tmp + 1;
		if (tmp > Sn)
		{
			tmp = tmp - Sn;
		}
		Window[i] = tmp;
	}

}

void GoBackN::Receiver()
{
	int Receive;
	int fault;
	int Err_Ac;
	while (true)
	{
		{
			lock_guard<mutex> lk(mx);
			if (Shared_Channel.empty() != true)
			{
				Receive = Shared_Channel.front();
				if (Receive == Rn)
				{
					printf("\n 2) Receiver :  Receives %d from Sender ! \n", Receive);

					Rn = Rn + 1;
					if (Rn > Sn)
					{
						Rn = 1;
					}
					{
						Err_Ac = (rand() % ((100 - 0) + 1)) + 0;
						if (Err_Ac <= Error_Rate_Ack)
						{
							fault = (Rn * 10) + Rn;
							ACK_Buffer.push_back(fault);
						}
						else
						{
							ACK_Buffer.push_back(Rn);
						}
					}
					Shared_Channel.erase(Shared_Channel.begin());
				}
				else
				{
					
					printf("\n 2) Receiver :  Receives fault or did not receive anything from Sender ! \n");
					for (int i = 0; i < Shared_Channel.size(); i++)
					{
						printf("   2) Receiver :  ==>   Rejects fault packet %d received from Sender ! \n", Shared_Channel[i]);
					}
					printf("\n ");
					Shared_Channel.clear();
					
					
				}
			}
		}		
		cv.notify_all();
		//this_thread::sleep_for(std::chrono::seconds(2));
	}
}

void GoBackN::Sender()
{
	bool _Sliding_Window = false;
	int ACK_Receive;

	srand((unsigned int)time(0));
	while (true)
	{

		{
			lock_guard<mutex> lk(mx);
			if (_Sliding_Window == true)
			{
				Sliding_Window();
			}
			else
			{
				Sending_Window();
			}
		}
		cv.notify_all();

		this_thread::sleep_for(std::chrono::seconds(4));


		{
			lock_guard<mutex> lk(mx);
			if (ACK_Buffer.empty() != true)
			{
				if (ACK_Buffer.front() == Window[1])
				{
					printf("\n 1) Sender :  Receive ACk-%d from receiver!", ACK_Buffer.front());
					Shifiting_Window();
					_Sliding_Window = true;
					ACK_Buffer.erase(ACK_Buffer.begin());
				}
				else
				{
					_Sliding_Window = false;
					printf("\n 1) Sender :  Receive fault ACk-%d & Sending previous window to receiver!", ACK_Buffer.front());
					ACK_Buffer.clear();

				}
				
			}
			else
			{
				printf("\n 1) Sender :  Did not receive any ACk & Sending previous window to receiver!");
				ACK_Buffer.clear();
				_Sliding_Window = false;
			}
		}
		cv.notify_all();
		
	}
}


int main()
{
	GoBackN MY_GoBackN;
	
	_getch();
	return 0;
}