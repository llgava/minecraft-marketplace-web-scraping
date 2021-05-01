import json

def writeJsonFile(path, filename, data):
  filePathNameExt = './' + path + '/' + filename + '.json'
  with open(filePathNameExt, 'w') as fp:
      json.dump(data, fp)
