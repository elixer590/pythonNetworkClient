# this module will be used to convert a dictionary to or from ascii encoding
# what do I need to know?
# diction will look like this
#key - port number
#value: xy data tuple

def encode(dictionary):
    data = ""
    for key in dictionary.keys():
        data += str(key) + "//"
        data += dictionary[key]
        data += "||"
    return data

def decode(encodedData):
    decodedDict = {}
    entries = encodedData.split('||')
    for entry in entries:
        info = entry.split('//')
        if info == ['']:
            continue
        info[1] = info[1].strip('()')
        temp = info[1].split(',')
        info[1] = (int(temp[0]), int(temp[1]))
        decodedDict[int(info[0])] = info[1]
    return decodedDict



if __name__ == "__main__":
    test = {52504: '(0, 0)', 1337: '(0,0)'}
    print("test value is:")
    print(test)
    print("encoded test value is:")
    encoded = encode(test)
    print(encoded)
    print("decoded test value is:")
    decoded = decode(encoded)
    print(decoded)
