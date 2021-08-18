from f5.bigip import ManagementRoot
from f5.utils.responses.handlers import Stats
import sys

args=sys.argv
host_ip = args[1]
username = args[2]
password = args[3]
poolname= args[4]
mgmt = ManagementRoot(host_ip, username, password, token=True)
my_pool = mgmt.tm.ltm.pools.pool.load(name=poolname)
poolstat=Stats(my_pool.stats.load())
print("teeeeeee"+str(poolstat.stat.activeMemberCnt.value))
