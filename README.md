MACChanger its the first software writed on python that im gonna leave here.

The objective of this software its make you anonymous when you are doing a ARP poisoning attack or just connect to network so when you are inside of the network the real MAC of youre Network Card is gonna be spoofed by one that you gonna make with this software.

###REQUERIMENTS###

Python --> sudo apt install python3 -y

git --> sudo apt install git -y 


Fake MAC addreses that can you use on the program:
----------------------------------------------------------------------------------------------------
Examples: 

# 00:11:D3:66:00:12
# d2:c2:f2:a2:00:88
# 5e:00:a1:b4:f8:c2
# d8:00:f2:a6:1d:c4
----------------------------------------------------------------------------------------------------
There more fake address that you can use but i leave writted this addresses like a fast testing.

The rules to make a fake MAC address are respecting the hexadecimal characters...

So just with the next characters you can try to make a fake MAC address and spoof the real one...
----------------------------------------------------------------------------------------------------
0 --> 1| 
1 --> 2|
2 --> 3| 
3 --> 4| 
4 --> 5| 
5 --> 6| 
6 --> 7| 
7 --> 8| 
8 --> 9| 
9 --> 10| 
A --> 11| 
B --> 12| 
C --> 13| 
D --> 14| 
E --> 15| 
F --> 16|
----------------------------------------------------------------------------------------------------

Guide of commands

git clone https://github.com/Ebooslilhacker/MACChanger.git

cd MACChanger

python3 MAC_Spoofer.py 
