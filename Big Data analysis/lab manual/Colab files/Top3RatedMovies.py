%%writefile Top3RatedMovies.py
# import modules
from mrjob.job import MRJob
from mrjob.step import MRStep

# create class inherited from MRJob
class Top3RatedMovies(MRJob):
  # assign steps, first mapper last reducer
  def steps(self):
    return [
            MRStep(mapper=self.mapper,
                   combiner = self.combiner,
                   reducer=self.reducer),
            MRStep(mapper=self.mapper1,
                   reducer=self.reducer1)
    ]

  # creating mapper, assigning attributes from dataset
  def mapper(self, _, line):
    (userID, movieID, rating, timestamp) = line.split('\t')
    yield movieID, float(rating)

  def combiner (self, key, values):
    sum = 0
    count = 0
    for value in values:
      sum = sum + value
      count = count + 1
    yield key, (sum, count)

  # creating reducer, sum
  def reducer(self, key, values):
    sum = 0
    count = 0
    for r,c in values:
      sum = sum + r
      count = count + c
    yield key, sum/count

  def mapper1(self, key, value):
    yield "X", (value, key)

  def reducer1(self, key, values):
    values = sorted(values, reverse=True)[0:3]
    for v in values:
      yield v[1], v[0]

if __name__ == '__main__':
  Top3RatedMovies.run()