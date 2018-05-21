# UDP Pinger - Client

from socket import *
import time

# set server to localhost and port 12000
serverName = '127.0.0.1' 
serverPort = 12000
i = 0

# enter a while loop to send 10 pings
while i < 10:
	#create a UDP socket for server
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	# increment ping counter
	i = i + 1
	# create message to send to server
	message = 'Ping ' + str(i)

	try:
		# Consider messaged timed out after 1 second
		clientSocket.settimeout(1)
		# start timer
		start = time.time()
		# attach server name and port to message, send into socket
		clientSocket.sendto(message,(serverName, serverPort))
		# read reponse from socket into string
		response, serverAddress = clientSocket.recvfrom(1024)
		# end timer
		end = time.time()
		# calculate elapsed time in seconds
		total = start - end
		# print out successful ping
		print 'Ping ' + str(i) + ' has returned. RTT: ' + str(-1*total) + 's'
	except timeout:
		# message exceeded timeout limit of 1s, print timeout message
		print 'Ping ' + str(i) + ' has timed out.'
	finally:
		# close socket
		clientSocket.close()
