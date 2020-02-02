# sp20-516-239 E.Cloudmesh.Common.5

from cloudmesh.common.StopWatch import StopWatch
from time import sleep
print("Starting stopwatch...")
StopWatch.start("test")
sleep(2)
StopWatch.stop("test")
print("It lasted", StopWatch.get("test"), "seconds.")