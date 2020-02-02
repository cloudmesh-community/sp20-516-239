# sp20-516-239 E.Cloudmesh.Common.1

from cloudmesh.common.util import banner
banner("This is my banner")

from cloudmesh.common.util import HEADING
HEADING("Spring 2020 Cloud Computing Class")
print("Demonstration of heading")

from cloudmesh.common.debug import VERBOSE
m = {"first_name": "Sara"}
VERBOSE(m)
