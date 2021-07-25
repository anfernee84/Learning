def make_request(keys, values):
    slo = {}
    if len(keys) != len (values):
        return slo
    slo = dict(zip(keys, values))
    return(slo)

        








print(make_request([1,2,3,4,5],[6,7,8,9,0]))