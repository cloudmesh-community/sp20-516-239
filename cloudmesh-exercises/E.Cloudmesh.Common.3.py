# sp20-516-239 E.Cloudmesh.Common.3

from cloudmesh.common.FlatDict import FlatDict
store = {
"name": "Walmart",
"employees": {
    "type1": "hourly",
    "type2": "salary"
    }
}
flat = FlatDict(store, sep=".")
print(flat)