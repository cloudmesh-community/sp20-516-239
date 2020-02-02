# sp20-516-239 E.Cloudmesh.Common.2

from cloudmesh.common.dotdict import dotdict
store = {
"name": "Walmart"
}
store = dotdict(store)
print(store["name"])
