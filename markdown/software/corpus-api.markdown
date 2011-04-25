Corpus API Documentation

Along with my Corpus Analyzer application. I am providing a RESTful API for
developers interested in building apps around the British and American National
Corpora. This API allows you to query for word counts in either corpus.

To use the API, set a GET request to http://zhehaomao.com/corpus/api/. There
should be one GET parameter called `q`, which holds the query. This query
should should be a well-formed JSON string. The JSON can either be an object
or a list. If it is an object, it should have two keys, "corpus" and
"word". The corpus key should hold the corpus you wish to search in,
either "anc" or "bnc" and the word key should contain the word you want to
search. If it is a list, it should be a list of objects in the
same format as the single object parameter.

If an object is passed in, the response will be a JSON object with three fields,
"ok", "count", and "relfreq". The "ok" field will be set to *true* if the query
is well formed or false otherwise. If ok is *false*, the other parts of the
response will not be present. The "count" field gives the absolute number of
occurences in the corpus. The "relfreq" field gives the relative frequency, which
is the count divided by the total word count in the corpus. If the request argument
was a list, a JSON list will be returned. Each element of the list will be an object
in the same format as a single object response.

If you want the entire corpora, CSV files are available [here](http://zhehaomao.com/static/files/corpora/).
The CSV files contain the word in the first column and the count in the second. The first row is
marked TOTAL. This is the total number of words in the corpus.

Important Note:
I do not keep the entire ANC or BNC because of the long tail in the distribution. I only keep
those words which are used more than 5 times. 
