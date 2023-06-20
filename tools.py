# import csv
# import json
#
#
# def csv_to_json(csvFilePath, jsonFilePath):
#     jsonArray = []
#
#     # read csv file
#     with open(csvFilePath, encoding='utf-8-sig') as csvf:
#         # load csv file data using csv library's dictionary reader
#         csvReader = csv.DictReader(csvf)
#
#         # convert each csv row into python dict
#         for row in csvReader:
#             # add this python dict to json array
#             jsonArray.append(row)
#
#     # convert python jsonArray to JSON String and write to file
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#         jsonString = json.dumps(jsonArray, ensure_ascii=False, indent=4)
#         jsonf.write(jsonString)
#
#
# csvFilePath = '/Users/boronoff/PycharmProjects/skypro_27/data/user.csv'
# jsonFilePath = '/Users/boronoff/PycharmProjects/skypro_27/data/user.json'
#
# csv_to_json(csvFilePath, jsonFilePath)
import random


def random_location():
    return float(str(random.uniform(10, 99))[0:8])
