from __future__ import print_function
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkContext

# $example on$
from pyspark.mllib.feature import HashingTF, IDF

# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="TFIDFExample")  # SparkContext

    # $example on$
    # Load documents (one per line).
    documents = sc.textFile("hdfs:///datasets/gutenberg-txt-es/*.txt").map(lambda line: line.split(" "))

    hashingTF = HashingTF()
    tf = hashingTF.transform(documents)

    # While applying HashingTF only needs a single pass to the data, applying IDF needs two passes:
    # First to compute the IDF vector and second to scale the term frequencies by IDF.

    tf.cache()
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)

    # spark.mllib's IDF implementation provides an option for ignoring terms
    # which occur in less than a minimum number of documents.
    # In such cases, the IDF for these terms is set to 0.
    # This feature can be used by passing the minDocFreq value to the IDF constructor.

    idfIgnore = IDF(minDocFreq=2).fit(tf)
    tfidfIgnore = idfIgnore.transform(tf)

    # $example off$

    print("tfidf:")

    for each in tfidf.collect():
        print(each)

    print("tfidfIgnore:")

    for each in tfidfIgnore.collect():
        print(each)


    clusters = KMeans.train(tfidf, 2, maxIterations=10, initializationMode="random")
    clusters.save(sc, "hdfs:///tmp/pruebaout3")
    sc.stop()
