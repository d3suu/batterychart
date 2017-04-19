from pylab import *
from subprocess import check_output
import time
import sys

try:
	nameoffile = sys.argv[1] # name of chart and output file
except:
	print 'Usage: {} <name_of_chart> '.format(sys.argv[0])
	print 'Example: {} chart'.format(sys.argv[0])
	print 'Example will save chart to chart.png in current catalog'
	print 'd3s.batterychart by d3s 2017'
	sys.exit()
	
samplingtime = 20 # in seconds
batteryend = '20' # in percents

def getpercent():
	output = check_output('acpi')
	percent = output.index('%')
	return output[percent-2:percent]

def gettime():
	output = time.time()
	return int(output)
	
def drawchart(OX, OY):
	title("d3s.batterychart - {}".format(nameoffile))
	xlabel('Time [s]')
	ylabel('Battery [%]')
	plot(OX, OY)
	savefig("{}.png".format(nameoffile))
	
	
timestart = gettime()
OX = [0]
OY = [0]

while 1:
	bat = getpercent()
	if bat == '00':
		bat = 100
	elif bat == batteryend:
		sys.exit()
	timeb = gettime() - timestart
	OX += [timeb]
	OY += [bat]
	print "Time: {}s | Battery: {}%".format(timeb, bat)
	drawchart(OX, OY)
	time.sleep(samplingtime)
