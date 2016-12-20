import lib

d = [("string", 15), ("number", 4), ("alphanumeric", 4), ("nric", 0)]
r = lib.RandomGen(100, fields=d)
r.to_json_file(r.output())
