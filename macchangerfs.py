import subprocess

def interfaces(): #List avalible interfaces
	return subprocess.run(["ls", "/sys/class/net"], stdout=subprocess.PIPE).stdout.decode('utf-8').strip().split()

def version(): #Print version
	output = subprocess.run(["macchanger", '-V'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	return output

def show(device=str()): #Print the MAC address
	output = subprocess.run(["macchanger", '-s', device], stdout=subprocess.PIPE).stdout.decode('utf-8')
	return output

def permanent(device=str()): #Reset to original, permanent hardware MAC
	subprocess.run(["ifconfig", device, "down"])
	print(subprocess.run(["macchanger", '-p', device], stdout=subprocess.PIPE).stdout.decode('utf-8'))
	subprocess.run(["ifconfig", device, "up"])

def list(): #Print known vendors
	#macs = [[[nums], [macs], [vendors]], [[nums], [macs], [vendors]]]
	##################Misc MACs#################Wireless MACs#########
	macs = [[[], [], []], [[], [], []]]
	rmacs = [for1.split('\n') for for1 in subprocess.run(["macchanger", '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n\n')]
	rmacs = [rmacs[0][3:], rmacs[1][3:-2]]
	for i in range(len(rmacs)):
		for j in range(len(rmacs[i])):
			for k in range(3):
				macs[i][k].append(rmacs[i][j].split(' - ')[k])
	return macs

def mac(device=str(), mac=str()): #Set specified MAC
	subprocess.run(["ifconfig", device, "down"])
	print(subprocess.run(["macchanger", "-m", mac, device], stdout=subprocess.PIPE).stdout.decode('utf-8'))
	subprocess.run(["ifconfig", device, "up"])

def random(device=str(), bia=bool()): #Set fully random MAC
	subprocess.run(["ifconfig", device, "down"])
	print(subprocess.run(["macchanger", "-rb" if bia else "-r", device], stdout=subprocess.PIPE).stdout.decode('utf-8'))
	subprocess.run(["ifconfig", device, "up"])

def ending(device=str()): #Don't change the vendor bytes(random)
	subprocess.run(["ifconfig", device, "down"])
	print(subprocess.run(["macchanger", "-e", device], stdout=subprocess.PIPE).stdout.decode('utf-8'))
	subprocess.run(["ifconfig", device, "up"])

def another(device=str()): #Set random vendor MAC of the same kind
	subprocess.run(["ifconfig", device, "down"])
	print(subprocess.run(["macchanger", "-a", device], stdout=subprocess.PIPE).stdout.decode('utf-8'))
	subprocess.run(["ifconfig", device, "up"])

def Any(device=str()): #Set random vendor MAC of any kind
	subprocess.run(["ifconfig", device, "down"])
	print(subprocess.run(["macchanger", "-A", device], stdout=subprocess.PIPE).stdout.decode('utf-8'))
	subprocess.run(["ifconfig", device, "up"])