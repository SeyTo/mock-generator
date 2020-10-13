# https://faker.readthedocs.io/en/
from faker import Faker
import random

# http://zetcode.com/python/argparse/
# import argparse


# w = write, a = append
writeFormat = 'w'
outFileName = 'out1.csv'
delimiter = ';'
no_export = False

region_ids = range(1, 10)
size = len(region_ids)
region_ids_iter = iter(region_ids)

def data(fake):
  return (
    str(region_ids_iter.__next__()),
    fake.name(),
  )

def exportToCSV(data):
  """
  Writes mock data to file in csv format.

  Paramters
  ----------
  data: list of row (in tuple)

  Returns
  ------- 
  undefined
  """

  if len(data) == 0:
    print('Nothing to do')
    return

  result = '\n'.join(
    [delimiter.join(d) for d in data]
  )

  print('Final Result ...')
  print(result) 
  if not no_export:
    print('Exporting ...')
    with open(outFileName, writeFormat) as file:
      file.write(result)


def main():
  fake = Faker()
  # serial = Serial()
  fake_data = []

  for _ in range(size):
    fake_data.append(data(fake))

  exportToCSV(fake_data)


if __name__ == "__main__":
  main()
