# This is a shell script used to ping a series of computers on a network.
# Assumes Classfull IP Addressing.

for i in {1..30} # Change sample size of pings here
do
 # Pick a host to ping.
 firstNum=$(($RANDOM%256))
 secondNum=$(($RANDOM%256))

 # Ping 1 time, timeout after 2 seconds. Output results to file.
 echo IP Address $i is: 129.100.$firstNum.$secondNum >> ipAddressList.txt 
 echo ------------------------------
 echo IP Address Test Number: $i
 echo ------------------------------
 ping -c1 -w2 129.100.$firstNum.$secondNum
 echo ------------------------------
 printf "\n\n"
done