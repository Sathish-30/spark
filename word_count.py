from pyspark import SparkConf, SparkContext

def main():
    conf = SparkConf().setAppName("WordCount").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    data = [
        "Apache Spark is fast",
        "Spark runs in memory",
        "Spark is simple",
        "Docker makes deployment easy"
    ]

    rdd = sc.parallelize(data)

    wordCounts = (
        rdd.flatMap(lambda line: line.split())
           .map(lambda word: (word, 1))
           .reduceByKey(lambda a, b: a + b)
    )

    results = wordCounts.collect()
    for word, count in results:
        print(f"{word}: {count}")

    sc.stop()

if __name__ == "__main__":
    main()
