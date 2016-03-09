impoprt serial

class Serial_control():
	def __init__(self,device='/dev/ttyAMA0',BAUD=9600):
		try:
			self.client=serial.Serial(device,BAUD,timeout=1)
		except:
			print "init serial error!"

	def send(self,CMD):
		try:
			self.client.write(CMD)
			#self.client.close()
		except:
			return "Serial error! \n  device:/dev/ttyAMA0"
	def read_ser(self):
		n=self.client.inWaiting()
		temp=self.client.read(n)
		self.client.close()
		return temp