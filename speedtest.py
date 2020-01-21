import pickle
import pandas as pd
from datetime import datetime

class FileNotExist(Exception):
	pass

class Results:

	def __init__(self, path):
		self.path = path
		self.results = []
		try:
			with open(self.path, "r") as f:
				content = pd.read_csv(f)
		except FileNotFoundError:
			raise FileNotExist("\nFile \"%s\" does not exist" % os.path.basename(self.path))
		header_convert = {
			"IP_ADDRESS": "ip",
			"TEST_DATE": "time",
			"TIME_ZONE": "time_zone",
			"DOWNLOAD_MEGABITS": "download",
			"UPLOAD_MEGABITS": "upload",
			"LATENCY_MS": "latency",
			"SERVER_NAME": "server",
			"DISTANCE_KILOMETERS": "server_distance",
			"CONNECTION_MODE": "mode",
		}
		for index, row in content.iterrows():
			data = {}
			for header in content:
				if header_convert[header] == "time":
					try:
						row[header] = datetime.strptime(row[header], "%m/%d/%Y %I:%M AM")
					except ValueError:
						row[header] = datetime.strptime(row[header], "%m/%d/%Y %I:%M PM")
				elif header_convert[header] == "mode":
					row[header] = row[header].capitalize()
				data[header_convert[header]] = row[header]
			self.results.append(data)

	def Save(self, path="data.pickle"):
		with open(path, "wb") as f:
			pickle.dump(self, f)

	def Load(self, path="data.pickle"):
		with open(path, "rb") as f:
			return pickle.load(f)

	def __getitem__(self, key):
		return self.results[key]

	def __missing__(self, key):
		pass

	def __repr__(self):
		preview = ""
		preview_format = "Ip:\t\t\t%s\nDownload Speed:\t\t%s\nUpload Speed:\t\t%s\n\n"
		if len(self.results) > 6:
			for result in self.results[:3]:
				preview += preview_format % (result["ip"], result["download"], result["upload"])
			preview += "......................................\n......................................\n......................................\n\n"
			for result in self.results[-3:]:
				preview += preview_format % (result["ip"], result["download"], result["upload"])
		else:
			for result in self.results:
				preview += str(result) + "\n"
		return preview[:-2]

	def __str__(self):
		return self.__repr__()

	def __list__(self):
		return self.results

	def __len__(self):
		return len(self.results)

	def __iter__(self):
		return iter(self.results)
