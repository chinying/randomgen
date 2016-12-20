import string, random, json, time

class RandomGen:

    DEFAULTLEN = 12
    # TODO sync this list
    types = ["string", "number", "alphanumeric", "hex", "name"]

    def __init__(self, cardinality, fields, filetype="json"):
        self.letters = list(string.ascii_letters)
        self.numbers = list(string.digits)
        self.alphanumeric = (self.letters + self.numbers)
        self.hex = list(string.hexdigits)
        self.cardinality = cardinality
        self.fields = fields
        self.func = {
            "string": self.rand_alpha,
            "number": self.rand_numbers,
            "alphanumeric": self.rand_alphanumeric,
            "hex": self.rand_hex,
            "nric": self.rand_nric
        }

    def rand_alpha(self, genlen=DEFAULTLEN):
        return random.sample(self.letters, genlen)
    def rand_numbers(self, genlen=DEFAULTLEN):
        return random.sample(self.numbers, genlen)
    def rand_alphanumeric(self, genlen=DEFAULTLEN):
        return random.sample(self.alphanumeric, genlen)
    def rand_hex(self, genlen=DEFAULTLEN):
        return random.sample(self.hex, genlen)
    def rand_nric(self, genlen=DEFAULTLEN): # checksum wrong, tbd
        return self.custom(["S", "T"], 1) + self.rand_numbers(7) + self.custom(self.letters[26:], 1)
    def custom(self, _list, genlen=DEFAULTLEN):
        return random.sample(_list, genlen)

    def f(self, x):
        return self.func[x]

    def output(self):
        rows = []
        for i in range(self.cardinality):
            row = []
            for (t, v) in self.fields:
                if t in self.func:
                    row.append("".join(self.f(t)(v)))
                    rows.append(row)
        # print(rows)
        d = {"data" : rows}
        return json.dumps(d)

    def to_json_file(self, content):
        downloads = "dl/"
        filename = downloads + str(time.time()).replace(".", "") + ".json"
        fo = open(filename, "w")
        fo.write(content)
        fo.close()
        return downloads + filename
