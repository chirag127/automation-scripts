import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

def post_urls(urls):

     with futures.ThreadPoolExecutor(max_workers=1000) as executor:

        the_futures = []
        for url in urls:
            the_futures.append(executor.submit(add_url, url))

        for future in futures.as_completed(the_futures):
            pass

def post_url(url):
    try:
        print(f"posting url: {url}")
        response = requests.post(url)

        if response.ok:
            pass
        else:
            print(f"error posting url: {url}")
    except Exception as e:
        print(f"error posting url: {url}")
        print(e)

# Obtain a request token
def get_request_token():
    # Step 2: Obtain a request token
    # To begin the Pocket authorization process, your application must obtain a request token from our servers by making a POST request.

    # Method URL:
    # https://getpocket.com/v3/oauth/request

    # Parameters
    # consumer_key	string		The consumer key for your application (see Step 1).
    # redirect_uri	string		The URL to be called when the authorization process has been completed. This URL should direct back to your application. See the Platform Specific Notes section for details about setting up custom urls for the redirect_uri on iOS and Android.
    # state	string	optional	A string of metadata used by your app. This string will be returned in all subsequent authentication responses.
    # Important note: In all the examples that follow, some HTTP headers have been removed to simplify the display.
    # Example request (x-www-form-urlencoded):
    # POST /v3/oauth/request HTTP/1.1
    # Host: getpocket.com
    # Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    # X-Accept: application/x-www-form-urlencoded

    # consumer_key=1234-abcd1234abcd1234abcd1234&
    # redirect_uri=pocketapp1234:authorizationFinished
    # Example response (x-www-form-urlencoded):
    # HTTP/1.1 200 OK
    # Content-Type: application/x-www-form-urlencoded
    # Status: 200 OK

    # code=dcba4321-dcba-4321-dcba-4321dc
    # Example request (JSON):
    # POST /v3/oauth/request HTTP/1.1
    # Host: getpocket.com
    # Content-Type: application/json; charset=UTF-8
    # X-Accept: application/json

    # {"consumer_key":"1234-abcd1234abcd1234abcd1234",
    # "redirect_uri":"pocketapp1234:authorizationFinished"}
    # Example response (JSON):
    # HTTP/1.1 200 OK
    # Content-Type: application/json
    # Status: 200 OK

    # {"code":"dcba4321-dcba-4321-dcba-4321dc"}
    # This request token (the "code" in the response) must be stored for use in step 5. For web applications, it should be associated with the user's session or other persistent state.

    # If the HTTP status of the response is 200, then the request completed successfully. Otherwise, an error occurred. When there is an error, the HTTP Header will contain details of the error using three fields: HTTP Status Code, X-Error-Code and X-Error.

    # HTTP Status	X-Error-Code	X-Error
    # 400	138	Missing consumer key.
    # 400	140	Missing redirect url.
    # 403	152	Invalid consumer key.
    # 50X	199	Pocket server issue.

    json 	= {
        "consumer_key":"REDACTED_POCKET_CONSUMER_KEY",
        "redirect_uri":"pocketapp1234:authorizationFinished"
    }
    headers = {
        'Host': 'getpocket.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Accept': 'application/json',
    }

    r = requests.post('https://getpocket.com/v3/oauth/request', headers=headers, data=json)
    print(r.text)
    print(r.status_code)


# Step 5: Convert a request token into a Pocket access token
# The final step to authorize Pocket with your application is to convert the request token into a Pocket access token. The Pocket access token is the user specific token that you will use to make further calls to the Pocket API.

# When your application receives the callback to the redirect_uri supplied in /v3/oauth/request (step 4), you should present some UI to indicate that your application is logging in and make a POST request.

# Method URL:
# https://getpocket.com/v3/oauth/authorize

# Parameters
# consumer_key	string		The consumer key for your application (see Step 1).
# code	string		The request token supplied in the code field of the /v3/oauth/request call.
# Example request (x-www-form-urlencoded):
# POST /v3/oauth/authorize HTTP/1.1
# Host: getpocket.com
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# X-Accept: application/x-www-form-urlencoded

# consumer_key=1234-abcd1234abcd1234abcd1234&
# code=dcba4321-dcba-4321-dcba-4321dc
# Example response (x-www-form-urlencoded):
# HTTP/1.1 200 OK
# Content-Type: application/x-www-form-urlencoded
# Status: 200 OK

# access_token=5678defg-5678-defg-5678-defg56&
# username=pocketuser
# Example request (JSON):
# POST /v3/oauth/authorize HTTP/1.1
# Host: getpocket.com
# Content-Type: application/json; charset=UTF-8
# X-Accept: application/json

# {"consumer_key":"1234-abcd1234abcd1234abcd1234",
# "code":"dcba4321-dcba-4321-dcba-4321dc"}
# Example response (JSON):
# HTTP/1.1 200 OK
# Content-Type: application/json
# Status: 200 OK

# {"access_token":"5678defg-5678-defg-5678-defg56",
# "username":"pocketuser"}
# The username of the user represented by the access token is provided for presentation in your UI to convey the username of the authenticated user.

# If you optionally supplied a state parameter with the original /v3/oauth/request POST, you will also receive that same value in the response.

# If the HTTP status of the response is 200, then the request completed successfully. Otherwise, an error occurred. When there is an error, the HTTP Header will contain details of the error using three fields: HTTP Status Code, X-Error-Code and X-Error.

# HTTP Status	X-Error-Code	X-Error
# 400	138	Missing consumer key.
# 403	152	Invalid consumer key.
# 400	181	Invalid redirect uri.
# 400	182	Missing code.
# 400	185	Code not found.
# 403	158	User rejected code.
# 403	159	Already used code.
# 50X	199	Pocket server issue.

def convert_request_token():
    json = {
        "consumer_key": "REDACTED_POCKET_CONSUMER_KEY",
        "code": "REDACTED_POCKET_REQUEST_TOKEN"
        }
    r = requests.post("https://getpocket.com/v3/oauth/authorize", json=json)
    print(r.text)
    print(r.json)
    print(r.status_code)
    print(r.headers)

access_token="REDACTED_POCKET_ACCESS_TOKEN"
username="REDACTED_EMAIL"

def add_url(url):
    #     Allowing users to add articles, videos, images and URLs to Pocket is most likely the first type of integration that you’ll want to build into your application. Adding items to Pocket is easy.

    # Required Permissions
    # In order to use the /v3/add endpoint, your consumer key must have the "Add" permission.

    # Adding a Single Item
    # To save an item to a user’s Pocket list, you’ll make a single request to the /v3/add endpoint.

    # Method URL
    # https://getpocket.com/v3/add

    # Parameters
    # url	string		The URL of the item you want to save
    # title	string	optional	This can be included for cases where an item does not have a title, which is typical for image or PDF URLs. If Pocket detects a title from the content of the page, this parameter will be ignored.
    # tags	string	optional	A comma-separated list of tags to apply to the item
    # tweet_id	string	optional	If you are adding Pocket support to a Twitter client, please send along a reference to the tweet status id. This allows Pocket to show the original tweet alongside the article.
    # consumer_key	string		Your application's Consumer Key
    # access_token	string		The user's Pocket access token
    # Example request (JSON):
    # POST /v3/add HTTP/1.1
    # Host: getpocket.com
    # Content-Type: application/json; charset=UTF-8
    # X-Accept: application/json

    # {"url":"http:\/\/pocket.co\/s8Kga",
    # "title":"iTeaching: The New Pedagogy (How the iPad is Inspiring Better Ways of
    # Teaching)",
    # "time":1346976937,
    # "consumer_key":"1234-abcd1234abcd1234abcd1234",
    # "access_token":"5678defg-5678-defg-5678-defg56"}
    # Example response (JSON):
    # HTTP/1.1 200 OK
    # Content-Type: application/json
    # Status: 200 OK

    # {"item":{[See Details Below]}, "status":1}
    # The item array in the response contains all of the meta information we have resolved about the saved item. The list of fields that may be returned include:

    # item_id: A unique identifier for the added item
    # normal_url: The original url for the added item
    # resolved_id: A unique identifier for the resolved item
    # resolved_url: The resolved url for the added item. The easiest way to think about the resolved_url - if you add a bit.ly link, the resolved_url will be the url of the page the bit.ly link points to
    # domain_id: A unique identifier for the domain of the resolved_url
    # origin_domain_id: A unique identifier for the domain of the normal_url
    # response_code: The response code received by the Pocket parser when it tried to access the item
    # mime_type: The MIME type returned by the item
    # content_length: The content length of the item
    # encoding: The encoding of the item
    # date_resolved: The date the item was resolved
    # date_published: The date the item was published (if the parser was able to find one)
    # title: The title of the resolved_url
    # excerpt: The excerpt of the resolved_url
    # word_count: For an article, the number of words
    # has_image: 0: no image; 1: has an image in the body of the article; 2: is an image
    # has_video: 0: no video; 1: has a video in the body of the article; 2: is a video
    # is_index: 0 or 1; If the parser thinks this item is an index page it will be set to 1
    # is_article: 0 or 1; If the parser thinks this item is an article it will be set to 1
    # authors: Array of author data (if author(s) were found)
    # images: Array of image data (if image(s) were found)
    # videos: Array of video data (if video(s) were found)
    # Best Practices
    # Be sure to url-encode the parameters you are sending. Otherwise if your url or title have characters like ? or &, they will often break the request.
    # Batch Adding
    # If you have a need to add several items at once or want perform other actions on a user’s list (like archive or favorite), please see the v3 API Modify endpoint.

    # Error Handling
    # View the Error and Response Headers Documentation for detailed information on how to respond to errors.

    request_url = "https://getpocket.com/v3/add"

    # Build the request
    request_data = {
        "url": url,
        "consumer_key": "REDACTED_POCKET_CONSUMER_KEY",
        "access_token": access_token
        }

    # Send the request
    response = requests.post(request_url, data=request_data)

    # Parse the response
    response_json = response.json()

    # Check for errors
    if response_json["status"] == 1:
        print("Successfully added item to Pocket")
        return True
    else:
        print("Error adding item to Pocket")
        print(response_json["error"])
        return False


if __name__ == '__main__':
    urls = """javascript:void(0)
https://www.javatpoint.com/
https://www.javatpoint.com/python-tutorial
https://www.javatpoint.com/python-if-else
https://www.javatpoint.com/python-for-loop
https://www.javatpoint.com/python-functions
https://www.javatpoint.com/python-arrays
https://www.javatpoint.com/python-strings
https://www.javatpoint.com/python-regex
https://www.javatpoint.com/python-lists
https://www.javatpoint.com/python-set
https://www.javatpoint.com/python-tuples
https://www.javatpoint.com/python-dictionary
https://www.javatpoint.com/python-programs
https://www.javatpoint.com/numpy-tutorial
https://www.javatpoint.com/python-interview-questions
https://www.javatpoint.com/python-features
https://www.javatpoint.com/python-history
https://www.javatpoint.com/python-applications
https://www.javatpoint.com/how-to-install-python
https://www.javatpoint.com/python-example
https://www.javatpoint.com/python-variables
https://www.javatpoint.com/python-data-types
https://www.javatpoint.com/python-keywords
https://www.javatpoint.com/python-literals
https://www.javatpoint.com/python-operators
https://www.javatpoint.com/python-comments
https://www.javatpoint.com/python-loops
https://www.javatpoint.com/python-while-loop
https://www.javatpoint.com/python-break
https://www.javatpoint.com/python-continue
https://www.javatpoint.com/python-pass
https://www.javatpoint.com/python-list-vs-tuple
https://www.javatpoint.com/python-built-in-functions
https://www.javatpoint.com/python-lambda-functions
https://www.javatpoint.com/python-files-io
https://www.javatpoint.com/python-modules
https://www.javatpoint.com/python-exception-handling
https://www.javatpoint.com/python-date
https://www.javatpoint.com/python-sending-email
https://www.javatpoint.com/python-read-csv-file
https://www.javatpoint.com/python-write-csv-file
https://www.javatpoint.com/python-read-excel-file
https://www.javatpoint.com/python-write-excel-file
https://www.javatpoint.com/python-assert-keyword
https://www.javatpoint.com/python-list-comprehension
https://www.javatpoint.com/python-collection-module
https://www.javatpoint.com/python-math-module
https://www.javatpoint.com/python-os-module
https://www.javatpoint.com/python-random-module
https://www.javatpoint.com/python-statistics-module
https://www.javatpoint.com/python-sys-module
https://www.javatpoint.com/python-ides
https://www.javatpoint.com/python-command-line-arguments
https://www.javatpoint.com/python-magic-method
https://www.javatpoint.com/python-stack-and-queue
https://www.javatpoint.com/pyspark-mllib
https://www.javatpoint.com/python-decorator
https://www.javatpoint.com/python-generators
https://www.javatpoint.com/web-scraping-using-python
https://www.javatpoint.com/python-json
https://www.javatpoint.com/python-itertools
https://www.javatpoint.com/python-multiprocessing
https://www.javatpoint.com/how-to-calculate-distance-between-two-points-using-geopy
https://www.javatpoint.com/gmail-api-in-python
https://www.javatpoint.com/how-to-plot-the-google-map-using-folium-package-in-python
https://www.javatpoint.com/grid-search-in-python
https://www.javatpoint.com/python-high-order-function
https://www.javatpoint.com/nsetools-in-python
https://www.javatpoint.com/python-program-to-find-the-nth-fibonacci-number
https://www.javatpoint.com/python-opencv-object-detection
https://www.javatpoint.com/python-simpleimputer-module
https://www.javatpoint.com/second-largest-number-in-python
https://www.javatpoint.com/python-oops-concepts
https://www.javatpoint.com/python-objects-classes
https://www.javatpoint.com/python-constructors
https://www.javatpoint.com/inheritance-in-python
https://www.javatpoint.com/abstraction-in-python
https://www.javatpoint.com/python-mysql-environment-setup
https://www.javatpoint.com/python-mysql-database-connection
https://www.javatpoint.com/python-mysql-creating-new-database
https://www.javatpoint.com/python-mysql-creating-tables
https://www.javatpoint.com/python-mysql-insert-operation
https://www.javatpoint.com/python-mysql-read-operation
https://www.javatpoint.com/python-mysql-update-operation
https://www.javatpoint.com/python-mysql-join-operation
https://www.javatpoint.com/python-mysql-performing-transactions
https://www.javatpoint.com/python-mongodb
https://www.javatpoint.com/python-sqlite
https://www.javatpoint.com/how-to-install-python-in-windows
https://www.javatpoint.com/how-to-reverse-a-string-in-python
https://www.javatpoint.com/how-to-read-csv-file-in-python
https://www.javatpoint.com/how-to-run-python-program
https://www.javatpoint.com/how-to-take-input-in-python
https://www.javatpoint.com/how-to-convert-list-to-string-in-python
https://www.javatpoint.com/how-to-append-element-in-the-list
https://www.javatpoint.com/how-to-compare-two-lists-in-python
https://www.javatpoint.com/how-to-convert-int-to-string-in-python
https://www.javatpoint.com/how-to-create-a-dictionary-in-python
https://www.javatpoint.com/how-to-create-a-virtual-environment-in-python
https://www.javatpoint.com/how-to-declare-a-variable-in-python
https://www.javatpoint.com/how-to-install-matplotlib-in-python
https://www.javatpoint.com/how-to-install-opencv-in-python
https://www.javatpoint.com/how-to-print-in-same-line-in-python
https://www.javatpoint.com/how-to-read-json-file-in-python
https://www.javatpoint.com/how-to-read-a-text-file-in-python
https://www.javatpoint.com/how-to-use-for-loop-in-python
https://www.javatpoint.com/is-python-scripting-language
https://www.javatpoint.com/how-long-does-it-take-to-learn-python
https://www.javatpoint.com/how-to-concatenate-two-strings-in-python
https://www.javatpoint.com/how-to-connect-database-in-python
https://www.javatpoint.com/how-to-convert-list-to-dictionary-in-python
https://www.javatpoint.com/how-to-declare-a-global-variable-in-python
https://www.javatpoint.com/how-to-reverse-a-number-in-python
https://www.javatpoint.com/what-is-an-object-in-python
https://www.javatpoint.com/which-is-the-fastest-implementation-of-python
https://www.javatpoint.com/how-to-clear-python-shell
https://www.javatpoint.com/how-to-create-a-dataframes-in-python
https://www.javatpoint.com/how-to-develop-a-game-in-python
https://www.javatpoint.com/how-to-install-tkinter-in-python
https://www.javatpoint.com/how-to-plot-a-graph-in-python
https://www.javatpoint.com/how-to-print-pattern-in-python
https://www.javatpoint.com/how-to-remove-an-element-from-a-list-in-python
https://www.javatpoint.com/how-to-round-number-in-python
https://www.javatpoint.com/how-to-sort-a-dictionary-in-python
https://www.javatpoint.com/strong-number-in-python
https://www.javatpoint.com/how-to-convert-text-to-speech-in-python
https://www.javatpoint.com/bubble-sort-in-python
https://www.javatpoint.com/logging-in-python
https://www.javatpoint.com/insertion-sort-in-python
https://www.javatpoint.com/binary-search-in-python
https://www.javatpoint.com/linear-search-in-python
https://www.javatpoint.com/python-vs-scala
https://www.javatpoint.com/queue-in-python
https://www.javatpoint.com/stack-in-python
https://www.javatpoint.com/heap-sort-in-python
https://www.javatpoint.com/palindrome-program-in-python
https://www.javatpoint.com/program-of-cumulative-sum-in-python
https://www.javatpoint.com/merge-sort-in-python
https://www.javatpoint.com/python-matrix
https://www.javatpoint.com/python-unit-testing
https://www.javatpoint.com/python-forensics-and-virtualization
https://www.javatpoint.com/best-books-to-learn-python
https://www.javatpoint.com/best-books-to-learn-django-for-beginners-and-advance-programmers
https://www.javatpoint.com/gcd-of-two-number-in-python
https://www.javatpoint.com/python-program-to-generate-a-random-string
https://www.javatpoint.com/how-to-one-hot-encode-sequence-data-in-python
https://www.javatpoint.com/how-to-write-square-root-in-python
https://www.javatpoint.com/pointer-in-python
https://www.javatpoint.com/python-2d-array
https://www.javatpoint.com/python-memory-management
https://www.javatpoint.com/python-libraries-for-data-visualization
https://www.javatpoint.com/how-to-call-a-function-in-python
https://www.javatpoint.com/git-modules-in-python
https://www.javatpoint.com/top-python-frameworks-for-gaming
https://www.javatpoint.com/python-audio-modules
https://www.javatpoint.com/wikipedia-module-in-python
https://www.javatpoint.com/python-random-randrange
https://www.javatpoint.com/permutation-and-combination-in-python
https://www.javatpoint.com/getopt-module-in-python
https://www.javatpoint.com/merge-two-dictionaries-in-python
https://www.javatpoint.com/multithreading-in-python-3
https://www.javatpoint.com/static-in-python
https://www.javatpoint.com/how-to-get-the-current-date-in-python
https://www.javatpoint.com/argparse-in-python
https://www.javatpoint.com/python-tqdm-module
https://www.javatpoint.com/caesar-cipher-in-python
https://www.javatpoint.com/tokenizer-in-python
https://www.javatpoint.com/how-to-add-two-lists-in-python
https://www.javatpoint.com/shallow-copy-and-deep-copy-in-python
https://www.javatpoint.com/atom-python
https://www.javatpoint.com/contains-in-python
https://www.javatpoint.com/label-encoding-in-python
https://www.javatpoint.com/django-vs-node-js
https://www.javatpoint.com/python-frameworks
https://www.javatpoint.com/how-to-create-a-vector-in-python-using-numpy
https://www.javatpoint.com/pickle-module-of-python
https://www.javatpoint.com/how-to-convert-bytes-to-string-in-python
https://www.javatpoint.com/python-program-to-find-anagram
https://www.javatpoint.com/how-to-convert-list-to-set
https://www.javatpoint.com/python-vs-javascript
https://www.javatpoint.com/python-holidays-module
https://www.javatpoint.com/fuzzywuzzy-python-library
https://www.javatpoint.com/dask-python
https://www.javatpoint.com/dask-python-part-2
https://www.javatpoint.com/mode-in-python
https://www.javatpoint.com/menu-driven-programs-in-python
https://www.javatpoint.com/python-array-vs-list
https://www.javatpoint.com/what-is-duck-typing-in-python
https://www.javatpoint.com/pep-8-in-python
https://www.javatpoint.com/python-user-groups
https://www.javatpoint.com/basic-commands-in-python
https://www.javatpoint.com/f-string-in-python
https://www.javatpoint.com/how-brython-works
https://www.javatpoint.com/how-to-use-brython-in-the-browser
https://www.javatpoint.com/arima-model-in-python
https://www.javatpoint.com/python-modulus-operator
https://www.javatpoint.com/matlab-vs-python
https://www.javatpoint.com/method-resolution-order-in-python
https://www.javatpoint.com/monkey-patching-in-python
https://www.javatpoint.com/python__call__method
https://www.javatpoint.com/python-heapq-module
https://www.javatpoint.com/python-substring
https://www.javatpoint.com/project-ideas-for-python-beginners
https://www.javatpoint.com/python-faker
https://www.javatpoint.com/fizz-buzz-program-in-python
https://www.javatpoint.com/tabula-python
https://www.javatpoint.com/python-program-to-print-prime-factor-of-given-number
https://www.javatpoint.com/python-program-to-print-pascal-triangle
https://www.javatpoint.com/namedtuple-in-python
https://www.javatpoint.com/ordereddict-in-python
https://www.javatpoint.com/t-test-in-python
https://www.javatpoint.com/python-return-statement
https://www.javatpoint.com/getter-and-setter-in-python
https://www.javatpoint.com/enum-class-in-python
https://www.javatpoint.com/destructors-in-python
https://www.javatpoint.com/curve-fit-in-python
https://www.javatpoint.com/converting-csv-to-json-in-python
https://www.javatpoint.com/underscore-in-python
https://www.javatpoint.com/set-vs-list-in-python
https://www.javatpoint.com/locating-and-executing-modules-in-python
https://www.javatpoint.com/flatten-list-in-python
https://www.javatpoint.com/pair-plot-in-python
https://www.javatpoint.com/data-hiding-in-python
https://www.javatpoint.com/python-program-to-find-intersection-of-two-lists
https://www.javatpoint.com/how-to-create-requirements-txt-file-in-python
https://www.javatpoint.com/tic-tac-toe-in-python
https://www.javatpoint.com/python-asynchronous-programming-asyncio-and-await
https://www.javatpoint.com/python-main-function
https://www.javatpoint.com/strftime-function-in-python
https://www.javatpoint.com/verbose-flag-in-python-regex
https://www.javatpoint.com/python-ast-module
https://www.javatpoint.com/python-requests-module-http-request
https://www.javatpoint.com/shutil-module-in-python
https://www.javatpoint.com/python-epoch-to-datetime
https://www.javatpoint.com/python-del-statement
https://www.javatpoint.com/looping-technique-in-python
https://www.javatpoint.com/metaprogramming-with-metaclasses-in-python
https://www.javatpoint.com/precision-handling-in-python
https://www.javatpoint.com/python-join-list
https://www.javatpoint.com/strip-function-in-python
https://www.javatpoint.com/gradient-descent-algorithm
https://www.javatpoint.com/prettytable-in-python
https://www.javatpoint.com/sentiment-analysis-in-python
https://www.javatpoint.com/convert-python-list-to-numpy-arrays
https://www.javatpoint.com/traceback-in-python
https://www.javatpoint.com/time-clock-method-in-python
https://www.javatpoint.com/deque-in-python
https://www.javatpoint.com/dictionary-comprehension-in-python
https://www.javatpoint.com/python-data-analytics
https://www.javatpoint.com/python-seek-method
https://www.javatpoint.com/ternary-operator-in-python
https://www.javatpoint.com/how-to-calculate-area-of-circle-using-python
https://www.javatpoint.com/how-to-write-in-text-file-using-python
https://www.javatpoint.com/python-keyerror
https://www.javatpoint.com/python-super-function
https://www.javatpoint.com/max-function-in-python
https://www.javatpoint.com/fraction-module-in-python
https://www.javatpoint.com/popular-python-framework-to-build-api
https://www.javatpoint.com/how-to-check-python-version
https://www.javatpoint.com/python-s-string-formatting
https://www.javatpoint.com/python-seaborn-library
https://www.javatpoint.com/countplot-in-python
https://www.javatpoint.com/range-vs-xrange-python
https://www.javatpoint.com/wordcloud-package-in-python
https://www.javatpoint.com/convert-dataframe-into-list
https://www.javatpoint.com/anova-test-in-python
https://www.javatpoint.com/python-program-to-find-compound-interest
https://www.javatpoint.com/ansible-in-python
https://www.javatpoint.com/python-important-tips-and-tricks
https://www.javatpoint.com/python-coroutines
https://www.javatpoint.com/double-underscores-in-python
https://www.javatpoint.com/re-search-vs-re-findall-in-python-regex
https://www.javatpoint.com/how-to-install-statsmodels-in-python
https://www.javatpoint.com/cos-in-python
https://www.javatpoint.com/vif-in-python
https://www.javatpoint.com/__add__-in-python
https://www.javatpoint.com/ethical-hacking-with-python
https://www.javatpoint.com/class-variable-vs-instance
https://www.javatpoint.com/perfect-number-in-python
https://www.javatpoint.com/eol-in-python
https://www.javatpoint.com/python-program-to-convert-hexadecimal-string-to-decimal-string
https://www.javatpoint.com/different-methods-in-python-for-swapping-two-numbers-without-using-third-variable
https://www.javatpoint.com/how-to-change-plot-size-in-matplotlib
https://www.javatpoint.com/how-to-get-zip-code-in-python
https://www.javatpoint.com/eel-in-python
https://www.javatpoint.com/assignment-operators-in-python
https://www.javatpoint.com/speech-recognition-python
https://www.javatpoint.com/yield-vs-return-in-python
https://www.javatpoint.com/graphene-python
https://www.javatpoint.com/name-mangling-in-python
https://www.javatpoint.com/python-combination-without-itertools
https://www.javatpoint.com/python-comprehensions
https://www.javatpoint.com/Influxdb-in-python
https://www.javatpoint.com/kafka-in-python
https://www.javatpoint.com/augmented-assignment-expressions-in-python
https://www.javatpoint.com/python-x-y-software
https://www.javatpoint.com/python-event-driven-programming
https://www.javatpoint.com/python-semaphore
https://www.javatpoint.com/python-sorted-reverse
https://www.javatpoint.com/automorphic-number-in-python
https://www.javatpoint.com/sizeof-in-python
https://www.javatpoint.com/python-program-for-accepting-the-strings-which-contains-all-vowels
https://www.javatpoint.com/class-based-views-vs-function-based-views
https://www.javatpoint.com/how-to-handle-cookies-in-django
https://www.javatpoint.com/agg-function-in-python
https://www.javatpoint.com/amicable-numbers-in-python
https://www.javatpoint.com/context-manager-in-python
https://www.javatpoint.com/create-bmi-calculator-using-python
https://www.javatpoint.com/string-to-binary-in-python
https://www.javatpoint.com/what-is-script-mode-in-python
https://www.javatpoint.com/best-python-libraries-for-machine-learning
https://www.javatpoint.com/python-program-to-display-calendar-of-given-year
https://www.javatpoint.com/how-to-open-url-in-python
https://www.javatpoint.com/broken-pipe-error-in-python
https://www.javatpoint.com/code-template-for-creating-objects-in-python
https://www.javatpoint.com/python-program-to-calculate-the-best-time-to-buy-and-sell-stock
https://www.javatpoint.com/tuple-to-string-in-python
https://www.javatpoint.com/kadanes-algorithm-in-python
https://www.javatpoint.com/loggers-in-django
https://www.javatpoint.com/weather-app-in-django
https://www.javatpoint.com/missing-data-conundrum-exploration-and-imputation-techniques
https://www.javatpoint.com/different-methods-of-array-rotation-in-python
https://www.javatpoint.com/what-is-operator-overloading-in-python
https://www.javatpoint.com/defaultdict-in-python
https://www.javatpoint.com/operator-module-in-python
https://www.javatpoint.com/spinner-widget-in-kivy-library-of-python
https://www.javatpoint.com/number-plate-recognition-using-python
https://www.javatpoint.com/obfuscating-a-python-program
https://www.javatpoint.com/convert-string-to-dictionary-in-python
https://www.javatpoint.com/convert-string-to-json-in-python
https://www.javatpoint.com/dbscan-algorithm-in-python
https://www.javatpoint.com/how-to-write-a-code-for-printing-python-exception-errorhierarchy
https://www.javatpoint.com/principal-component-analysis-with-python
https://www.javatpoint.com/python-program-to-find-number-of-days-between-two-given-dates
https://www.javatpoint.com/object-recognition-using-python
https://www.javatpoint.com/python-vlc-module
https://www.javatpoint.com/set-to-list-in-python
https://www.javatpoint.com/string-to-int-in-python
https://www.javatpoint.com/internet-of-things-with-python
https://www.javatpoint.com/python-pysftp-module
https://www.javatpoint.com/amazing-hacks-of-python
https://www.javatpoint.com/average-of-list-in-python
https://www.javatpoint.com/check-installed-modules-in-python
https://www.javatpoint.com/choice-in-python
https://www.javatpoint.com/convert-list-to-dataframe-in-python
https://www.javatpoint.com/convert-string-to-float-in-python
https://www.javatpoint.com/decorators-with-parameters-in-python
https://www.javatpoint.com/dynamic-typing-in-python
https://www.javatpoint.com/fabs-in-python
https://www.javatpoint.com/how-to-remove-decimal-in-python
https://www.javatpoint.com/python-closure
https://www.javatpoint.com/python-glob-module
https://www.javatpoint.com/writing-a-python-module
https://www.javatpoint.com/modules-vs-packages-in-python
https://www.javatpoint.com/snmp-module-in-python
https://www.javatpoint.com/append-vs-extend-vs-insert-in-python
https://www.javatpoint.com/how-to-remove-duplicates-from-a-list-in-python
https://www.javatpoint.com/remove-multiple-characters-from-a-string-in-python
https://www.javatpoint.com/shuffle-in-python
https://www.javatpoint.com/floor-and-ceil-functions-in-python
https://www.javatpoint.com/sqrt-math-function-of-python
https://www.javatpoint.com/python-yfinance-module
https://www.javatpoint.com/difflib-module-in-python
https://www.javatpoint.com/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe
https://www.javatpoint.com/python-wxpython-module
https://www.javatpoint.com/random-uniform-python
https://www.javatpoint.com/relational-operators-in-python
https://www.javatpoint.com/string-to-list-in-python
https://www.javatpoint.com/chatbot-in-python
https://www.javatpoint.com/how-to-convert-float-to-int-in-python
https://www.javatpoint.com/multiply-all-elements-in-list-of-python
https://www.javatpoint.com/module-vs-function-in-python
https://www.javatpoint.com/reverse-a-tuple-in-python
https://www.javatpoint.com/tuple-to-dictionary-in-python
https://www.javatpoint.com/datetime-timedelta-function-of-python
https://www.javatpoint.com/python-bio-module
https://www.javatpoint.com/python-dash-module
https://www.javatpoint.com/how-to-select-rows-in-pandas-dataframe-based-on-conditions
https://www.javatpoint.com/typecasting-in-python
https://www.javatpoint.com/dateutil-module-in-python
https://www.javatpoint.com/getpass-module-in-python
https://www.javatpoint.com/python-wand-library
https://www.javatpoint.com/generate-a-qr-code-using-python
https://www.javatpoint.com/best-python-pdf-library
https://www.javatpoint.com/python-cachetools-module
https://www.javatpoint.com/python-cmdparser-module
https://www.javatpoint.com/python-emoji-module
https://www.javatpoint.com/python-nmap-module
https://www.javatpoint.com/python-pylab-module
https://www.javatpoint.com/working-with-pdf-files-in-python
https://www.javatpoint.com/pdf-handling-in-python
https://www.javatpoint.com/manipulating-pdf-using-python
https://www.javatpoint.com/list-all-functions-from-a-python-module
https://www.javatpoint.com/python-list-of-dictionaries
https://www.javatpoint.com/python-shelve-module
https://www.javatpoint.com/creating-interactive-pdf-forms-using-python
https://www.javatpoint.com/python-newspaper-module
https://www.javatpoint.com/how-to-connect-wi-fi-using-python
https://www.javatpoint.com/best-python-libraries-used-for-ethical-hacking
https://www.javatpoint.com/windows-system-administration-management-using-python
https://www.javatpoint.com/indentation-error-in-python
https://www.javatpoint.com/python-imaplib-module
https://www.javatpoint.com/python-lxml-module
https://www.javatpoint.com/python-mayavi-module
https://www.javatpoint.com/python-os-listdir-method
https://www.javatpoint.com/python-modules-for-automation
https://www.javatpoint.com/data-visualization-in-python-using-bokeh-library
https://www.javatpoint.com/how-to-plot-glyphs-over-a-google-map-by-using-bokeh-library-in-python
https://www.javatpoint.com/how-to-plot-a-pie-chart-using-bokeh-library-in-python
https://www.javatpoint.com/how-to-read-contents-of-pdf-using-ocr-in-python
https://www.javatpoint.com/grammar-and-spell-checker-in-python
https://www.javatpoint.com/converting-html-to-pdf-files-using-python
https://www.javatpoint.com/readlines-in-python
https://www.javatpoint.com/how-to-plot-multiple-lines-on-a-graph-using-bokeh-in-python
https://www.javatpoint.com/bokeh-plotting-figure-circle_x-function-in-python
https://www.javatpoint.com/bokeh-plotting-figure-diamond_cross-function-in-python
https://www.javatpoint.com/how-to-plot-rays-on-a-graph-using-bokeh-in-python
https://www.javatpoint.com/image-steganography-using-python
https://www.javatpoint.com/inconsistent-use-of-tabs-and-spaces-in-indentation
https://www.javatpoint.com/how-to-plot-multiple-plots-using-bokeh-in-python
https://www.javatpoint.com/how-to-make-an-area-plot-in-python-using-bokeh
https://www.javatpoint.com/python-chempy-module
https://www.javatpoint.com/python-memory-profiler-module
https://www.javatpoint.com/python-phonenumbers-module
https://www.javatpoint.com/python-platform-module
https://www.javatpoint.com/typeerror-string-indices-must-be-an-integer
https://www.javatpoint.com/time-series-forecasting-with-prophet-in-python
https://www.javatpoint.com/python-pexpect-module
https://www.javatpoint.com/python-optparse-module
https://www.javatpoint.com/int-object-is-not-iterable
https://www.javatpoint.com/python-peewee-library
https://www.javatpoint.com/some-cryptocurrency-libraries-for-python
https://www.javatpoint.com/building-a-blockchain-using-python
https://www.javatpoint.com/huffman-coding-using-python
https://www.javatpoint.com/nested-dictionary-in-python
https://www.javatpoint.com/collections-userstring-in-python
https://www.javatpoint.com/how-to-customize-legends-with-matplotlib
https://www.javatpoint.com/matplotlib-legend-in-subplot
https://www.javatpoint.com/morphological-operations-in-image-processing-in-python
https://www.javatpoint.com/role-of-python-in-artificial-intelligence
https://www.javatpoint.com/python-instagramy-module
https://www.javatpoint.com/python-pprint-module
https://www.javatpoint.com/python-primepy-module
https://www.javatpoint.com/android-development-using-python
https://www.javatpoint.com/python-fbchat-library
https://www.javatpoint.com/artificial-intelligence-in-cybersecurity-pitting-algorithms-vs-algorithms
https://www.javatpoint.com/understanding-recognition-pattern-of-artificial-intelligence
https://www.javatpoint.com/when-and-how-to-leverage-lambda-architecture-in-big-data
https://www.javatpoint.com/why-should-we-learn-python-for-data-science
https://www.javatpoint.com/how-to-change-legend-position-in-matplotlib
https://www.javatpoint.com/how-to-check-if-element-exists-in-list-in-python
https://www.javatpoint.com/how-to-check-spellings-of-given-words-using-enchant-in-python
https://www.javatpoint.com/python-program-to-count-number-of-matching-characters-in-a-pair-of-string
https://www.javatpoint.com/ping-pong-game-using-turtle-in-python
https://www.javatpoint.com/python-function-to-display-clendar
https://www.javatpoint.com/python-program-for-calculating-sum-of-squares-of-first-n-natural-numbers
https://www.javatpoint.com/python-program-for-how-to-check-if-a-given-number-is-fibonacci-number-or-not
https://www.javatpoint.com/randint-function-in-python
https://www.javatpoint.com/visualize-tiff-file-using-matplotlib-and-gdal-in-python
https://www.javatpoint.com/rarfile-module-in-python
https://www.javatpoint.com/stemming-words-using-python
https://www.javatpoint.com/python-program-for-word-guessing-game
https://www.javatpoint.com/blockchain-in-healthcare-innovations-and-opportunities
https://www.javatpoint.com/snake-game-in-python-using-turtle-module
https://www.javatpoint.com/how-to-find-armstrong-numbers-between-two-given-integers
https://www.javatpoint.com/celery-tutorial-using-python
https://www.javatpoint.com/rsme-root-mean-square-error-in-python
https://www.javatpoint.com/building-a-twitter-bot-using-python
https://www.javatpoint.com/python-progressbar-module
https://www.javatpoint.com/python-pronouncing-module
https://www.javatpoint.com/python-pyautogui-module
https://www.javatpoint.com/python-pyperclip-module
https://www.javatpoint.com/how-to-generate-uuid-in-python
https://www.javatpoint.com/python-top-10-libraries-to-learn-in-2022
https://www.javatpoint.com/reading-netcdf-data-using-python
https://www.javatpoint.com/reprlib-module-in-python
https://www.javatpoint.com/how-to-take-multiple-input-from-user-in-python
https://www.javatpoint.com/python-zlib-library
https://www.javatpoint.com/python-queue-module
https://www.javatpoint.com/python-yaml-parser
https://www.javatpoint.com/effective-root-searching-algorithms-in-python
https://www.javatpoint.com/python-bz2-module
https://www.javatpoint.com/python-ipaddress-module
https://www.javatpoint.com/python-pylint-module
https://www.javatpoint.com/how-to-process-xml-in-python
https://www.javatpoint.com/bisect-algorithm-functions-in-python
https://www.javatpoint.com/creating-and-updating-powerpoint-presentation-using-python
https://www.javatpoint.com/how-to-change-the-size-of-figure-drawn-with-matplotlib
https://www.javatpoint.com/keyboard-module-in-python
https://www.javatpoint.com/python-pyfiglet-module
https://www.javatpoint.com/creating-an-mcq-quiz-game-in-python
https://www.javatpoint.com/statistic-with-python
https://www.javatpoint.com/what-is-gil-in-python-global-interpreter-lock
https://www.javatpoint.com/basic-python-for-java-developers
https://www.javatpoint.com/how-to-download-youtube-videos-using-python-scripts
https://www.javatpoint.com/traffic-flow-simulation-in-python
https://www.javatpoint.com/how-to-merge-and-sort-two-lists-in-python
https://www.javatpoint.com/metacharacters-in-python
https://www.javatpoint.com/write-python-program-to-print-all-possible-combination-of-integers
https://www.javatpoint.com/modulo-string-formatting-in-python
https://www.javatpoint.com/counters-in-python
https://www.javatpoint.com/python-pyautogui-library
https://www.javatpoint.com/how-to-draw-the-mandelbrot-set-in-python
https://www.javatpoint.com/python-dbm-module
https://www.javatpoint.com/webcam-motion-detector-in-python
https://www.javatpoint.com/graphql-implementation-in-django
https://www.javatpoint.com/how-to-implement-protobuf-in-python
https://www.javatpoint.com/pyqt-library-in-python
https://www.javatpoint.com/how-to-prettify-data-structures-with-pretty-print-in-python
https://www.javatpoint.com/encrypt-a-password-in-python-using-bcrypt
https://www.javatpoint.com/pyramid-framework-in-python
https://www.javatpoint.com/building-a-telegram-bot-using-python
https://www.javatpoint.com/web2py-framework-in-python
https://www.javatpoint.com/python-os-chdir-method
https://www.javatpoint.com/balancing-parentheses-in-python
https://www.javatpoint.com/how-to-provide-multiple-constructors-in-python-classes
https://www.javatpoint.com/profiling-the-python-code
https://www.javatpoint.com/build-a-dice-rolling-application-with-python
https://www.javatpoint.com/email-module-in-python
https://www.javatpoint.com/essential-recursion-programs-in-python
https://www.javatpoint.com/how-to-design-hashset-in-python
https://www.javatpoint.com/how-to-extract-youtube-data-in-python
https://www.javatpoint.com/how-to-solve-stock-span-problem-using-python
https://www.javatpoint.com/selection-sort-in-python
https://www.javatpoint.com/info-function-in-python
https://www.javatpoint.com/python-solution-of-two-sum-problem-of-given-list
https://www.javatpoint.com/write-a-python-program-to-check-a-list-contains-duplicate-element
https://www.javatpoint.com/write-python-program-to-search-an-element-in-sorted-array
https://www.javatpoint.com/pathlib-module-in-python
https://www.javatpoint.com/create-a-real-time-voice-translator-using-python
https://www.javatpoint.com/how-to-sort-tuple-in-python
https://www.javatpoint.com/advantages-of-python-that-made-it-so-popular-and-its-major-applications
https://www.javatpoint.com/library-in-python
https://www.javatpoint.com/packages-of-data-visualization-in-python
https://www.javatpoint.com/python-pympler-library
https://www.javatpoint.com/snakeviz-library-in-python
https://www.javatpoint.com/materialized-view-vs-view
https://www.javatpoint.com/namespace-in-python
https://www.javatpoint.com/python-program-to-return-the-sign-of-the-product-of-an-array
https://www.javatpoint.com/fabric-module-in-python
https://www.javatpoint.com/tracemalloc-module-in-python
https://www.javatpoint.com/split-sub-subn-functions-of-re-module-in-python
https://www.javatpoint.com/robot-framework-in-python
https://www.javatpoint.com/understanding-robotics-with-python
https://www.javatpoint.com/gzip-module-in-python
https://www.javatpoint.com/guppy-heapy-in-python
https://www.javatpoint.com/microservices-in-python
https://www.javatpoint.com/functools-module-in-python
https://www.javatpoint.com/plotting-google-map-using-gmplot-package-in-python
https://www.javatpoint.com/monitoring-devices-using-python
https://www.javatpoint.com/webbrowser-module-in-python
https://www.javatpoint.com/binary-search-using-recursion-in-python
https://www.javatpoint.com/c-vs-cpp-vs-python-vs-java
https://www.javatpoint.com/how-to-check-version-of-python
https://www.javatpoint.com/convert-roman-number-to-decimal-integer
https://www.javatpoint.com/create-rest-api-using-django-rest-framework
https://www.javatpoint.com/memoization-using-decorators-in-python
https://www.javatpoint.com/python-for-network-engineering
https://www.javatpoint.com/and-vs-and-in-python
https://www.javatpoint.com/cryptography-package-in-python
https://www.javatpoint.com/hangman-game-in-python
https://www.javatpoint.com/implementation-of-linear-regression-using-python
https://www.javatpoint.com/nested-decorators-in-python
https://www.javatpoint.com/python-program-to-find-difference-between-two-strings
https://www.javatpoint.com/python-urllib-library
https://www.javatpoint.com/fiona-module-in-python
https://www.javatpoint.com/firebase-module-in-python
https://www.javatpoint.com/python-for-kids
https://www.javatpoint.com/floor-division-in-python
https://www.javatpoint.com/top-10-best-coursera-python-courses
https://www.javatpoint.com/top-python-for-network-engineering-libraries
https://www.javatpoint.com/how-does-tokenizing-text-sentence-words-works
https://www.javatpoint.com/how-to-import-datasets-using-sklearn-in-pybrain
https://www.javatpoint.com/part-of-speech-tagging-using-textblob
https://www.javatpoint.com/python-for-kids-resources-for-python-learning-path
https://www.javatpoint.com/xgboost-ml-model-in-python
https://www.javatpoint.com/simple-flames-game-in-python
https://www.javatpoint.com/alarm-clock-with-gui-in-python
https://www.javatpoint.com/rock-paper-scissors-game-in-python
https://www.javatpoint.com/check-if-a-given-linked-list-is-circular-linked-list
https://www.javatpoint.com/reverse-linked-list-in-python
https://www.javatpoint.com/flatten-vs-ravel-numpy-functions
https://www.javatpoint.com/learning-vector-quantization
https://www.javatpoint.com/lemmatization-and-tokenize-with-textblob
https://www.javatpoint.com/how-to-round-numbers-in-python
https://www.javatpoint.com/precedence-and-associativity-of-operators-in-python
https://www.javatpoint.com/python-unofficial-libraries
https://www.javatpoint.com/12-best-python-projects-for-class-12
https://www.javatpoint.com/desktop-notifier-in-python
https://www.javatpoint.com/how-to-handle-time-zones-in-python
https://www.javatpoint.com/python-secret-module
https://www.javatpoint.com/make-notepad-using-tkinter
https://www.javatpoint.com/camelcase-in-python
https://www.javatpoint.com/difference-between-python-and-scala
https://www.javatpoint.com/how-to-use-cbind-in-python
https://www.javatpoint.com/python-asserts
https://www.javatpoint.com/python-bitwise-operators
https://www.javatpoint.com/python-time-asctime-method
https://www.javatpoint.com/q-learning-in-python
https://www.javatpoint.com/combinatoric-iterators-in-python
https://www.javatpoint.com/class-method-vs-static-method-vs-instance-method
https://www.javatpoint.com/free-python-ebooks
https://www.javatpoint.com/eight-amazing-ideas-of-python-tkinter-projects
https://www.javatpoint.com/creating-a-keylogger-using-python
https://www.javatpoint.com/quandl-package-in-python
https://www.javatpoint.com/implementing-apriori-algorithm-in-python
https://www.javatpoint.com/sentiment-analysis-using-vader
https://www.javatpoint.com/break-statement-in-python
https://www.javatpoint.com/handling-imbalanced-data-in-python-with-smote-algorithm-and-near-miss-algorithm
https://www.javatpoint.com/gui-calculator-using-python
https://www.javatpoint.com/sympy-module-in-python
https://www.javatpoint.com/smote-python
https://www.javatpoint.com/breadth-first-search-in-python
https://www.javatpoint.com/python-graphviz-dot-language
https://www.javatpoint.com/how-to-visualize-a-neural-network-in-python-using-graphviz
https://www.javatpoint.com/python-graphviz
https://www.javatpoint.com/compound-interest-gui-calculator-using-python
https://www.javatpoint.com/rank-based-percentile-gui-calculator-in-python
https://www.javatpoint.com/url-shortner-in-python
https://www.javatpoint.com/automate-instagram-messages-using-python
https://www.javatpoint.com/python-simplehttpserver-module
https://www.javatpoint.com/standard-gui-unit-converter-in-python
https://www.javatpoint.com/python-paramiko-module
https://www.javatpoint.com/dispatch-decorators-in-python
https://www.javatpoint.com/introspection-in-python
https://www.javatpoint.com/class-decorator-in-python
https://www.javatpoint.com/customizing-parser-behaviour-python-module-configparser
https://www.javatpoint.com/pythons-module-configparser
https://www.javatpoint.com/gui-calendar-using-tkinter-in-python
https://www.javatpoint.com/python-program-to-rotate-an-image
https://www.javatpoint.com/validate-the-ip-address-in-python
https://www.javatpoint.com/program-to-print-diagonal-elements-of-the-given-2d-matrix
https://www.javatpoint.com/encapsulation-in-python
https://www.javatpoint.com/polymorphism-in-python
https://www.javatpoint.com/stringio-module-in-python
https://www.javatpoint.com/10-python-image-manipulation-tools
https://www.javatpoint.com/how-to-insert-current_timestamp-into-postgres-via-python
https://www.javatpoint.com/how-to-perform-a-one-way-anova-in-python
https://www.javatpoint.com/types-of-inheritance-python
https://www.javatpoint.com/python-for-mechanical-engineers
https://www.javatpoint.com/python-module-xxhash
https://www.javatpoint.com/escape-sequences-in-python
https://www.javatpoint.com/python-null-statement
https://www.javatpoint.com/python-and-operator
https://www.javatpoint.com/python-or-operator
https://www.javatpoint.com/python-bitwise-xor-operator
https://www.javatpoint.com/python-new-line
https://www.javatpoint.com/__init__-in-python
https://www.javatpoint.com/__dict__-in-python
https://www.javatpoint.com/simple-to-do-list-gui-application-in-python
https://www.javatpoint.com/automate-software-testing-with-python
https://www.javatpoint.com/automate-the-google-search-using-python
https://www.javatpoint.com/__name__-in-python
https://www.javatpoint.com/_name_-_main_-in-python
https://www.javatpoint.com/8-puzzle-problem-in-python
https://www.javatpoint.com/accuracy_score-in-sklearn
https://www.javatpoint.com/python-vs-julia
https://www.javatpoint.com/python-crontab-module
https://www.javatpoint.com/python-execute-shell-command
https://www.javatpoint.com/file-explorer-using-tkinter-in-python
https://www.javatpoint.com/automated-trading-in-python
https://www.javatpoint.com/python-automation-project-ideas
https://www.javatpoint.com/k-means-1d-clustering-in-python
https://www.javatpoint.com/adding-a-key-value-pair-to-a-dictionary-in-python
https://www.javatpoint.com/fit-transform-and-fit_transform-methods-in-python
https://www.javatpoint.com/python-for-finance
https://www.javatpoint.com/librosa-library-in-python
https://www.javatpoint.com/python-artificial-pntelligence-projects-for-beginners
https://www.javatpoint.com/age-calculator-using-tkinter-in-python
https://www.javatpoint.com/how-to-iterate-a-dictionary-in-python
https://www.javatpoint.com/how-to-iterate-through-a-list-in-python
https://www.javatpoint.com/how-to-learn-python-online
https://www.javatpoint.com/cross-validation-in-sklearn
https://www.javatpoint.com/popular-python-libraries-for-finance-industry
https://www.javatpoint.com/famous-python-certification-courses-for-finance
https://www.javatpoint.com/k-fold-cross-validation-in-sklearn
https://www.javatpoint.com/python-projects-on-ml-applications-in-finance
https://www.javatpoint.com/digital-clock-using-tkinter-in-python
https://www.javatpoint.com/plot-correlation-matrix-in-python
https://www.javatpoint.com/euclidian-distance-using-numpy
https://www.javatpoint.com/how-to-parse-json-in-python
https://www.javatpoint.com/how-to-make-the-first-column-an-index-in-python
https://www.javatpoint.com/how-to-make-an-app-in-python
https://www.javatpoint.com/morse-code-translator-in-python
https://www.javatpoint.com/python-locust-module
https://www.javatpoint.com/python-time-module
https://www.javatpoint.com/sklearn-linear-regression-example
https://www.javatpoint.com/python-timeit-module
https://www.javatpoint.com/qr-code-using-python
https://www.javatpoint.com/flipping-tiles-using-python
https://www.javatpoint.com/python-curl
https://www.javatpoint.com/examples-of-python-curl
https://www.javatpoint.com/sklearn-model-selection
https://www.javatpoint.com/standardscaler-in-sklearn
https://www.javatpoint.com/filter-list-in-python
https://www.javatpoint.com/python-projects-in-networking
https://www.javatpoint.com/python-networkx
https://www.javatpoint.com/sklearn-logistic-regression
https://www.javatpoint.com/what-is-sklearn-in-python
https://www.javatpoint.com/tkinter-application-to-switch-between-different-page-frames-in-python
https://www.javatpoint.com/append-pair-to-dictionary
https://www.javatpoint.com/any-in-python
https://www.javatpoint.com/arguments-and-parameters-in-python
https://www.javatpoint.com/attributes-meaning-in-python
https://www.javatpoint.com/data-structures-and-algorithms-in-python-set-1
https://www.javatpoint.com/gaussian-elimination-in-python
https://www.javatpoint.com/learn-python-from-best-youtube-channels-in-2022
https://www.javatpoint.com/sklearn-clustering
https://www.javatpoint.com/sklearn-tutorial
https://www.javatpoint.com/what-is-sleeping-time-in-python
https://www.javatpoint.com/python-word2vec
https://www.javatpoint.com/creating-the-gui-marksheet-using-tkinter-in-python
https://www.javatpoint.com/colour-game-using-tkinter-in-python
https://www.javatpoint.com/simple-flames-game-using-tkinter-in-python
https://www.javatpoint.com/youtube-video-downloader-using-python-tkinter
https://www.javatpoint.com/find-key-from-value-in-dictionary
https://www.javatpoint.com/sklearn-regression-models
https://www.javatpoint.com/covid-19-data-representation-app-using-tkinter-in-python
https://www.javatpoint.com/image-viewer-app-using-tkinter-in-python
https://www.javatpoint.com/simple-registration-form-using-tkinter-in-python
https://www.javatpoint.com/python-string-equals
https://www.javatpoint.com/control-statements-in-python
https://www.javatpoint.com/how-to-plot-histogram-in-python
https://www.javatpoint.com/how-to-plot-multiple-linear-regression-in-python
https://www.javatpoint.com/physics-calculations-in-python
https://www.javatpoint.com/solve-physics-computational-problems-using-python
https://www.javatpoint.com/screen-rotation-gui-using-python-tkinter
https://www.javatpoint.com/application-to-search-installed-applications-using-tkinter-in-python
https://www.javatpoint.com/spell-corrector-gui-using-tkinter-in-python
https://www.javatpoint.com/data-structures-and-algorithms-in-python
https://www.javatpoint.com/gui-to-shut-down-restart-and-log-off-the-computer-using-tkinter-in-python
https://www.javatpoint.com/gui-to-extract-lyrics-from-a-song-using-tkinter-in-python
https://www.javatpoint.com/sentiment-detector-gui-using-tkinter-in-python
https://www.javatpoint.com/python-sleep-function
https://www.javatpoint.com/diabetes-prediction-using-machine-learning
https://www.javatpoint.com/first-unique-character-in-a-string-python
https://www.javatpoint.com/using-python-create-own-movies-recommendation-engine
https://www.javatpoint.com/find-hotel-price-using-the-hotel-price-comparison-api-using-python
https://www.javatpoint.com/get-started-with-rabbitmq-and-python
https://www.javatpoint.com/how-to-send-push-notification-in-python
https://www.javatpoint.com/how-to-use-redis-with-python
https://www.javatpoint.com/advance-concepts-of-python-for-python-developer
https://www.javatpoint.com/pycricbuzz-library-cricket-api-for-python
https://www.javatpoint.com/write-the-python-program-to-combine-two-dictionary-values-for-common-keys
https://www.javatpoint.com/apache-airflow-in-python
https://www.javatpoint.com/currying-in-python
https://www.javatpoint.com/how-to-find-the-users-location-using-geolocation-api
https://www.javatpoint.com/lru-cache-in-python
https://www.javatpoint.com/python-list-comprehension-vs-generator-expression
https://www.javatpoint.com/python-output-formatting
https://www.javatpoint.com/python-property-decorator
https://www.javatpoint.com/dfs-in-python
https://www.javatpoint.com/fast-api-a-framework-to-create-apis
https://www.javatpoint.com/mirror-character-of-a-string-in-python
https://www.javatpoint.com/python-imdbpy-a-library-for-movies
https://www.javatpoint.com/python-packing-and-unpacking-arguments-in-python
https://www.javatpoint.com/python-pdb
https://www.javatpoint.com/python-program-to-move-all-the-zeros-to-the-end-of-array
https://www.javatpoint.com/regular-dictionary-vs-ordered-dictionary-in-python
https://www.javatpoint.com/topology-sorting-in-python
https://www.javatpoint.com/tqdm-integration-with-pandas
https://www.javatpoint.com/bisect-module-in-python
https://www.javatpoint.com/boruvkas-algorithm-minimum-spanning-trees
https://www.javatpoint.com/property-vs-attributes-in-python
https://www.javatpoint.com/draw-great-indian-flag-using-python-code
https://www.javatpoint.com/find-all-triplets-with-zero-sum-in-python
https://www.javatpoint.com/generate-html-using-tinyhtml-module-in-python
https://www.javatpoint.com/google-search-packages-using-python
https://www.javatpoint.com/kmp-algorithm-implementation-of-kmp-algorithm-using-python
https://www.javatpoint.com/new-features-in-python-3_10
https://www.javatpoint.com/types-of-constant-in-python
https://www.javatpoint.com/python-program-to-sort-an-odd-even-sort-or-odd-even-transposition-sort
https://www.javatpoint.com/python-program-to-print-the-doubly-linked-list-in-reverse-order
https://www.javatpoint.com/application-to-get-live-usd-inr-rate-using-tkinter-in-python
https://www.javatpoint.com/create-the-first-gui-application-using-pyqt5-in-python
https://www.javatpoint.com/simple-gui-calculator-using-pyqt5-in-python
https://www.javatpoint.com/best-resources-to-learn-numpy-and-pandas
https://www.javatpoint.com/decision-tree-in-python-sklearn
https://www.javatpoint.com/python-books-for-data-structures-and-algorithms
https://www.javatpoint.com/python-tkinter-top-level-widget
https://www.javatpoint.com/remove-first-character-from-string-in-python
https://www.javatpoint.com/loan-calculator-using-pyqt5-in-python
https://www.javatpoint.com/flappy-bird-game-using-pygame-in-python
https://www.javatpoint.com/rank-based-percentile-gui-calculator-using-pyqt5-in-python
https://www.javatpoint.com/3d-scatter-plotting-in-python-using-matplotlib
https://www.javatpoint.com/function-annotations-in-python
https://www.javatpoint.com/numpy-3d-matrix-multiplication
https://www.javatpoint.com/os_path_abspath-method-in-python
https://www.javatpoint.com/emerging-advance-python-projects-2022
https://www.javatpoint.com/how-to-check-nan-values-in-pandas
https://www.javatpoint.com/how-to-combine-two-dataframe-in-python-pandas
https://www.javatpoint.com/how-to-make-a-python-auto-clicker
https://www.javatpoint.com/age-calculator-using-pyqt5-in-python
https://www.javatpoint.com/create-a-table-using-pyqt5-in-python
https://www.javatpoint.com/create-a-gui-calendar-using-pyqt5-in-python
https://www.javatpoint.com/snake-game-using-pygame-in-python
https://www.javatpoint.com/return-two-values-from-a-function-in-python
https://www.javatpoint.com/complete-roadmap-to-learn-python
https://www.javatpoint.com/tree-view-widgets-and-tree-view-scrollbar-in-tkinter-python
https://www.javatpoint.com/aes-ctr-python
https://www.javatpoint.com/curdir-python
https://www.javatpoint.com/fastnlmeansdenoising-in-python
https://www.javatpoint.com/python-email-utils
https://www.javatpoint.com/python-win32-process
https://www.javatpoint.com/data-science-projects-in-python-with-proper-project-description
https://www.javatpoint.com/how-to-practice-python-programming
https://www.javatpoint.com/hypothesis-testing-python
https://www.javatpoint.com/args-and-kwargs-in-python
https://www.javatpoint.com/__file__-in-python
https://www.javatpoint.com/__future__-module-in-python
https://www.javatpoint.com/applying-lambda-functions-to-pandas-dataframe
https://www.javatpoint.com/box-plot-in-python-using-matplotlib
https://www.javatpoint.com/box-cox-transformation-in-python
https://www.javatpoint.com/assertionerror-in-python
https://www.javatpoint.com/find-key-with-maximum-value-in-dictionary
https://www.javatpoint.com/project-in-python-breast-cancer-classification-with-deep-learning
https://www.javatpoint.com/colour-game-using-pyqt5-in-python
https://www.javatpoint.com/digital-clock-using-pyqt5-in-python
https://www.javatpoint.com/countdown-timer-using-pyqt5-in-python
https://www.javatpoint.com/gui-to-shut-down-restart-and-log-off-computer-using-tkinter-in-python
https://www.javatpoint.com/simple-flames-game-using-pyqt5-in-python
https://www.javatpoint.com/__getitem__-in-python
https://www.javatpoint.com/get-and-post-requests-using-python
https://www.javatpoint.com/attributeerror-in-python
https://www.javatpoint.com/matplotlib_figure_figure_add_subplot-in-python
https://www.javatpoint.com/python-bit-functions-on-int
https://www.javatpoint.com/check-if-string-has-character-in-python
https://www.javatpoint.com/how-to-get-2-decimal-places-in-python
https://www.javatpoint.com/how-to-get-index-of-element-in-list-python
https://www.javatpoint.com/nested-tuples-in-python
https://www.javatpoint.com/gui-assistant-using-wolfram-alpha-api-in-python
https://www.javatpoint.com/signal-processing-hands-on-in-python
https://www.javatpoint.com/scatter-plot-pandas-in-python
https://www.javatpoint.com/scatter-plot-matplotlib-in-python
https://www.javatpoint.com/python-tkinter
https://www.javatpoint.com/python-tkinter-button
https://www.javatpoint.com/python-tkinter-canvas
https://www.javatpoint.com/python-tkinter-checkbutton
https://www.javatpoint.com/python-tkinter-entry
https://www.javatpoint.com/python-tkinter-frame
https://www.javatpoint.com/python-tkinter-label
https://www.javatpoint.com/python-tkinter-listbox
https://www.javatpoint.com/python-tkinter-menubutton
https://www.javatpoint.com/python-tkinter-menu
https://www.javatpoint.com/python-tkinter-message
https://www.javatpoint.com/python-tkinter-radiobutton
https://www.javatpoint.com/python-tkinter-scale
https://www.javatpoint.com/python-tkinter-scrollbar
https://www.javatpoint.com/python-tkinter-text
https://www.javatpoint.com/python-tkinter-toplevel
https://www.javatpoint.com/python-tkinter-spinbox
https://www.javatpoint.com/python-tkinter-panedwindow
https://www.javatpoint.com/python-tkinter-labelframe
https://www.javatpoint.com/python-tkinter-messagebox
https://www.javatpoint.com/python-website-blocker
https://www.javatpoint.com/python-website-blocker-building-python-script
https://www.javatpoint.com/python-website-blocker-script-deployment-on-linux
https://www.javatpoint.com/python-website-blocker-script-deployment-on-windows
https://www.javatpoint.com/python-mcq
https://www.javatpoint.com/python-mcq-part-2
https://www.javatpoint.com/django-tutorial
https://www.javatpoint.com/flask-tutorial
https://www.javatpoint.com/python-pandas
https://www.javatpoint.com/pytorch
https://www.javatpoint.com/pygame
https://www.javatpoint.com/matplotlib
https://www.javatpoint.com/opencv
https://www.javatpoint.com/python-openpyxl
https://www.javatpoint.com/python-cgi-programming
https://www.javatpoint.com/python-design-pattern
https://www.javatpoint.com/classification-of-programming-languages
https://bit.ly/2FOeX6S
https://www.javatpoint.com/splunk
https://www.javatpoint.com/spss
https://www.javatpoint.com/swagger
https://www.javatpoint.com/t-sql
https://www.javatpoint.com/tumblr
https://www.javatpoint.com/reactjs-tutorial
https://www.javatpoint.com/regex
https://www.javatpoint.com/reinforcement-learning
https://www.javatpoint.com/r-tutorial
https://www.javatpoint.com/rxjs
https://www.javatpoint.com/react-native-tutorial
https://www.javatpoint.com/python-pillow
https://www.javatpoint.com/python-turtle-programming
https://www.javatpoint.com/keras
https://www.javatpoint.com/aptitude/quantitative
https://www.javatpoint.com/reasoning
https://www.javatpoint.com/verbal-ability
https://www.javatpoint.com/interview-questions-and-answers
https://www.javatpoint.com/company-interview-questions-and-recruitment-process
https://www.javatpoint.com/artificial-intelligence-tutorial
https://www.javatpoint.com/aws-tutorial
https://www.javatpoint.com/selenium-tutorial
https://www.javatpoint.com/cloud-computing-tutorial
https://www.javatpoint.com/hadoop-tutorial
https://www.javatpoint.com/data-science
https://www.javatpoint.com/angular-7-tutorial
https://www.javatpoint.com/blockchain-tutorial
https://www.javatpoint.com/git
https://www.javatpoint.com/machine-learning
https://www.javatpoint.com/devops
https://www.javatpoint.com/dbms-tutorial
https://www.javatpoint.com/data-structure-tutorial
https://www.javatpoint.com/daa-tutorial
https://www.javatpoint.com/os-tutorial
https://www.javatpoint.com/computer-network-tutorial
https://www.javatpoint.com/compiler-tutorial
https://www.javatpoint.com/computer-organization-and-architecture-tutorial
https://www.javatpoint.com/discrete-mathematics-tutorial
https://www.javatpoint.com/ethical-hacking-tutorial
https://www.javatpoint.com/computer-graphics-tutorial
https://www.javatpoint.com/software-engineering-tutorial
https://www.javatpoint.com/html-tutorial
https://www.javatpoint.com/cyber-security-tutorial
https://www.javatpoint.com/automata-tutorial
https://www.javatpoint.com/c-programming-language-tutorial
https://www.javatpoint.com/cpp-tutorial
https://www.javatpoint.com/java-tutorial
https://www.javatpoint.com/net-framework
https://www.javatpoint.com/programs-list
https://www.javatpoint.com/control-system-tutorial
https://www.javatpoint.com/data-mining
https://www.javatpoint.com/data-warehouse
https://www.javatpoint.com/c-sharp-tutorial
https://www.javatpoint.com/php-tutorial
https://www.javatpoint.com/javascript-tutorial
https://www.javatpoint.com/jquery-tutorial
https://www.javatpoint.com/spring-tutorial
https://www.hindi100.com/
https://www.lyricsia.com/
https://www.quoteperson.com/
https://www.jobandplacement.com/
https://www.javatpoint.com/contact-us
https://www.javatpoint.com/subscribe.jsp
https://www.javatpoint.com/privacy-policy
https://www.javatpoint.com/sitemap.xml
https://www.javatpoint.com/sonoo-jaiswal
https://www.javatpoint.com/
https://www.javatpoint.com/javascript-tutorial
https://www.javatpoint.com/html-tutorial
https://www.javatpoint.com/css-tutorial
https://www.javatpoint.com/bootstrap-tutorial
https://www.javatpoint.com/jquery-tutorial
https://www.javatpoint.com/nodejs-tutorial
https://www.javatpoint.com/php-tutorial
https://www.javatpoint.com/python-tutorial
https://www.javatpoint.com/c-programming-language-tutorial
https://www.javatpoint.com/cpp-tutorial
https://www.javatpoint.com/java-tutorial
https://www.javatpoint.com/c-sharp-tutorial
https://www.javatpoint.com/sql-tutorial
https://www.javatpoint.com/android-tutorial
https://www.javatpoint.com/javascript-interview-questions
https://www.javatpoint.com/javascript-example
https://www.javatpoint.com/external-javascript-file
https://www.javatpoint.com/javascript-comment
https://www.javatpoint.com/javascript-variable
https://www.javatpoint.com/javascript-global-variable
https://www.javatpoint.com/javascript-data-types
https://www.javatpoint.com/javascript-operators
https://www.javatpoint.com/javascript-if
https://www.javatpoint.com/javascript-switch
https://www.javatpoint.com/javascript-loop
https://www.javatpoint.com/javascript-function
https://www.javatpoint.com/javascript-objects
https://www.javatpoint.com/javascript-array
https://www.javatpoint.com/javascript-string
https://www.javatpoint.com/javascript-date
https://www.javatpoint.com/javascript-math
https://www.javatpoint.com/javascript-number
https://www.javatpoint.com/javascript-boolean
https://www.javatpoint.com/browser-object-model
https://www.javatpoint.com/window-object
https://www.javatpoint.com/javascript-history-object
https://www.javatpoint.com/javascript-navigator-object
https://www.javatpoint.com/javascript-screen
https://www.javatpoint.com/document-object-model
https://www.javatpoint.com/document-getElementById()-method
https://www.javatpoint.com/javascript-getelementsbyclassname
https://www.javatpoint.com/document-getElementsByName()-method
https://www.javatpoint.com/document-getElementsByTagName()-method
https://www.javatpoint.com/javascript-innerHTML
https://www.javatpoint.com/javascript-innerText
https://www.javatpoint.com/javascript-form-validation
https://www.javatpoint.com/javascript-form-validation#email
https://www.javatpoint.com/javascript-oops-classes
https://www.javatpoint.com/javascript-oops-prototype-object
https://www.javatpoint.com/javascript-oops-constructor-method
https://www.javatpoint.com/javascript-oops-static-method
https://www.javatpoint.com/javascript-oops-encapsulation
https://www.javatpoint.com/javascript-oops-inheritance
https://www.javatpoint.com/javascript-oops-polymorphism
https://www.javatpoint.com/javascript-oops-abstraction
https://www.javatpoint.com/javascript-cookies
https://www.javatpoint.com/javascript-cookie-attributes
https://www.javatpoint.com/javascript-cookie-with-multiple-name
https://www.javatpoint.com/javascript-deleting-cookies
https://www.javatpoint.com/javascript-events
https://www.javatpoint.com/javascript-addeventlistener
https://www.javatpoint.com/javascript-onclick-event
https://www.javatpoint.com/javascript-dblclick-event
https://www.javatpoint.com/javascript-onload
https://www.javatpoint.com/javascript-onresize-event
https://www.javatpoint.com/exception-handling-in-javascript
https://www.javatpoint.com/javascript-try-catch
https://www.javatpoint.com/javascript-this-keyword
https://www.javatpoint.com/javascript-debugging
https://www.javatpoint.com/javascript-hoisting
https://www.javatpoint.com/javascript-strict-mode
https://www.javatpoint.com/javascript-promise
https://www.javatpoint.com/javascript-compare-dates
https://www.javatpoint.com/javascript-array-length-property
https://www.javatpoint.com/javascript-alert
https://www.javatpoint.com/javascript-eval-function
https://www.javatpoint.com/javascript-closest
https://www.javatpoint.com/javascript-continue-statement
https://www.javatpoint.com/javascript-getattribute-method
https://www.javatpoint.com/javascript-hide-elements
https://www.javatpoint.com/javascript-prompt-dialog-box
https://www.javatpoint.com/javascript-removeattribute-method
https://www.javatpoint.com/javascript-reset
https://www.javatpoint.com/javascript-return
https://www.javatpoint.com/javascript-string-split
https://www.javatpoint.com/javascript-typeof-operator
https://www.javatpoint.com/javascript-ternary-operator
https://www.javatpoint.com/javascript-reload-method
https://www.javatpoint.com/javascript-setattribute
https://www.javatpoint.com/javascript-setinterval-method
https://www.javatpoint.com/javascript-settimeout-method
https://www.javatpoint.com/javascript-string-includes
https://www.javatpoint.com/calculate-current-week-number-in-javascript
https://www.javatpoint.com/calculate-days-between-two-dates-in-javascript
https://www.javatpoint.com/javascript-string-trim
https://www.javatpoint.com/javascript-timer
https://www.javatpoint.com/remove-elements-from-array-in-javascript
https://www.javatpoint.com/javascript-localstorage
https://www.javatpoint.com/javascript-offsetheight
https://www.javatpoint.com/confirm-password-validation-in-javascript
https://www.javatpoint.com/static-vs-const-in-javascript
https://www.javatpoint.com/how-to-convert-comma-separated-string-into-an-array-in-javascript
https://www.javatpoint.com/calculate-age-using-javascript
https://www.javatpoint.com/javascript-label-statement
https://www.javatpoint.com/javascript-string-with-quotes
https://www.javatpoint.com/how-to-create-dropdown-list-using-javascript
https://www.javatpoint.com/how-to-disable-radio-button-using-javascript
https://www.javatpoint.com/check-if-the-value-exists-in-array-in-javascript
https://www.javatpoint.com/javascript-setinterval
https://www.javatpoint.com/javascript-debouncing
https://www.javatpoint.com/javascript-print-method
https://www.javatpoint.com/javascript-editable-table
https://www.javatpoint.com/canvasjs
https://www.javatpoint.com/javascript-typedarray
https://www.javatpoint.com/javascript-set
https://www.javatpoint.com/javascript-map
https://www.javatpoint.com/javascript-weakset
https://www.javatpoint.com/javascript-weakmap
https://www.javatpoint.com/javascript-callback
https://www.javatpoint.com/javascript-closures
https://www.javatpoint.com/javascript-date-difference
https://www.javatpoint.com/javascript-date-format
https://www.javatpoint.com/javascript-date-parse-method
https://www.javatpoint.com/javascript-defer
https://www.javatpoint.com/javascript-redirect
https://www.javatpoint.com/javascript-scope
https://www.javatpoint.com/javascript-scroll
https://www.javatpoint.com/javascript-sleep
https://www.javatpoint.com/javascript-void
https://www.javatpoint.com/javascript-form
https://www.javatpoint.com/jquery-vs-javascript
https://www.javatpoint.com/javascript-vs-php
https://www.javatpoint.com/dart-vs-javascript
https://www.javatpoint.com/javascript-vs-angularjs
https://www.javatpoint.com/javascript-vs-nodejs
https://www.javatpoint.com/how-to-add-javascript-to-html
https://www.javatpoint.com/how-to-enable-javascript-in-my-browser
https://www.javatpoint.com/difference-between-java-and-javascript
https://www.javatpoint.com/how-to-call-javascript-function-in-html
https://www.javatpoint.com/how-to-write-a-function-in-javascript
https://www.javatpoint.com/is-javascript-case-sensitive
https://www.javatpoint.com/how-does-javascript-work
https://www.javatpoint.com/how-to-debug-javascript
https://www.javatpoint.com/how-to-enable-javascript-on-android
https://www.javatpoint.com/what-is-a-promise-in-javascript
https://www.javatpoint.com/what-is-hoisting-in-javascript
https://www.javatpoint.com/what-is-vanilla-javascript
https://www.javatpoint.com/how-to-add-a-class-to-an-element-using-javascript
https://www.javatpoint.com/how-to-calculate-the-perimeter-and-area-of-a-circle-using-javascript
https://www.javatpoint.com/how-to-create-an-image-map-in-javascript
https://www.javatpoint.com/how-to-find-factorial-of-a-number-in-javascript
https://www.javatpoint.com/how-to-get-the-value-of-pi-using-javascript
https://www.javatpoint.com/how-to-make-a-text-italic-using-javascript
https://www.javatpoint.com/what-are-the-uses-of-javascript
https://www.javatpoint.com/how-to-get-all-checked-checkbox-value-in-javascript
https://www.javatpoint.com/how-to-open-json-file
https://www.javatpoint.com/random-image-generator-in-javascript
https://www.javatpoint.com/how-to-add-object-in-array-using-javascript
https://www.javatpoint.com/javascript-window-open-method
https://www.javatpoint.com/javascript-window-close-method
https://www.javatpoint.com/how-to-check-a-radio-button-using-javascript
https://www.javatpoint.com/javascript-const
https://www.javatpoint.com/javascript-function-to-check-array-is-empty-or-not
https://www.javatpoint.com/javascript-multi-line-string
https://www.javatpoint.com/javascript-anonymous-functions
https://www.javatpoint.com/implementing-javascript-stack-using-array
https://www.javatpoint.com/javascript-classlist
https://www.javatpoint.com/javascript-code-editors
https://www.javatpoint.com/javascript-let-keyword
https://www.javatpoint.com/random-string-generator-using-javascript
https://www.javatpoint.com/javascript-queue
https://www.javatpoint.com/event-bubbling-and-capturing-in-javascript
https://www.javatpoint.com/how-to-select-all-checkboxes-using-javascript
https://www.javatpoint.com/javascript-change-event
https://www.javatpoint.com/javascript-focusout-event
https://www.javatpoint.com/traverse-array-object-using-javascript
https://www.javatpoint.com/javascript-create-and-download-csv-file
https://www.javatpoint.com/how-to-make-beep-sound-in-javascript
https://www.javatpoint.com/how-to-add-a-whatsapp-share-button-in-a-website-using-javascript
https://www.javatpoint.com/javascript-execution-context
https://www.javatpoint.com/javascript-queryselector
https://www.javatpoint.com/shallow-copy-in-javascript
https://www.javatpoint.com/how-to-toggle-password-visibility-in-javascript
https://www.javatpoint.com/removing-duplicate-from-arrays-in-javascript
https://www.javatpoint.com/javascript-insertbefore
https://www.javatpoint.com/javascript-select-option
https://www.javatpoint.com/get-and-set-scroll-position-of-an-element
https://www.javatpoint.com/getting-child-elements-of-a-node-in-javascript
https://www.javatpoint.com/javascript-scrollintoview
https://www.javatpoint.com/javascript-string-startswith
https://www.javatpoint.com/js-first-class-function
https://www.javatpoint.com/javascript-default-parameters
https://www.javatpoint.com/javascript-recursion-in-real-life
https://www.javatpoint.com/javascript-removechild
https://www.javatpoint.com/remove-options-from-select-list-in-javascript
https://www.javatpoint.com/javascript-calculator
https://www.javatpoint.com/palindrome-in-javascript
https://www.javatpoint.com/javascript-call-stack
https://www.javatpoint.com/fibonacci-series-in-javascript
https://www.javatpoint.com/javascript-appendchild-method
https://www.javatpoint.com/ripple-effect-javascript
https://www.javatpoint.com/convert-object-to-array-in-javascript
https://www.javatpoint.com/javascript-async-and-await
https://www.javatpoint.com/javascript-blob
https://www.javatpoint.com/check-if-the-array-is-empty-or-null-or-undefined-in-javascript
https://www.javatpoint.com/javascript-animation
https://www.javatpoint.com/javascript-design-patterns
https://www.javatpoint.com/javascript-format-numbers-with-commas
https://www.javatpoint.com/currying-in-javascript
https://www.javatpoint.com/javascript-hasownproperty
https://www.javatpoint.com/how-to-make-a-curved-active-tab-in-the-navigation-menu-using-html-css-and-javascript
https://www.javatpoint.com/http-cookies
https://www.javatpoint.com/javascript-comparison
https://www.javatpoint.com/javascript-confirm
https://www.javatpoint.com/javascript-garbage
https://www.javatpoint.com/javascript-special-characters
https://www.javatpoint.com/javascript-time-now
https://www.javatpoint.com/lodash_chain-method
https://www.javatpoint.com/underscorejs-_filter-function
https://www.javatpoint.com/lodash_find-method
https://www.javatpoint.com/lodash_get-method
https://www.javatpoint.com/javascript-mcq
https://www.javatpoint.com/oprweb/test.jsp?filename=hellojs
https://www.javatpoint.com/post/javascript-dataview
https://www.javatpoint.com/javascript-handler
https://www.javatpoint.com/javascript-json
https://www.javatpoint.com/javascript-reflect
https://www.javatpoint.com/javascript-regexp
https://www.javatpoint.com/javascript-symbol
https://www.javatpoint.com/understanding-html-dom-events
https://www.javatpoint.com/javascript-array-concat-method
https://www.javatpoint.com/javascript-array-copywithin-method
https://www.javatpoint.com/javascript-array-every-method
https://www.javatpoint.com/javascript-array-fill-method
https://www.javatpoint.com/javascript-array-filter-method
https://www.javatpoint.com/javascript-array-find-method
https://www.javatpoint.com/javascript-array-findindex-method
https://www.javatpoint.com/javascript-array-foreach-method
https://www.javatpoint.com/javascript-array-includes-method
https://www.javatpoint.com/javascript-array-indexof-method
https://www.javatpoint.com/javascript-array-join-method
https://www.javatpoint.com/javascript-array-lastindexof-method
https://www.javatpoint.com/javascript-array-map-method
https://www.javatpoint.com/javascript-array-pop-method
https://www.javatpoint.com/javascript-array-push-method
https://www.javatpoint.com/javascript-array-reverse-method
https://www.javatpoint.com/javascript-array-shift-method
https://www.javatpoint.com/javascript-array-slice-method
https://www.javatpoint.com/javascript-array-sort-method
https://www.javatpoint.com/javascript-array-splice-method
https://www.javatpoint.com/javascript-array-unshift-method
https://www.javatpoint.com/post/javascript-dataview-getfloat32-method
https://www.javatpoint.com/post/javascript-dataview-getfloat64-method
https://www.javatpoint.com/post/javascript-dataview-getint8-method
https://www.javatpoint.com/post/javascript-dataview-getint16-method
https://www.javatpoint.com/post/javascript-dataview-getint32-method
https://www.javatpoint.com/post/javascript-dataview-getuint8-method
https://www.javatpoint.com/post/javascript-dataview-getuint16-method
https://www.javatpoint.com/post/javascript-dataview-getuint32-method
https://www.javatpoint.com/javascript-function-apply-method
https://www.javatpoint.com/javascript-function-bind-method
https://www.javatpoint.com/javascript-function-call-method
https://www.javatpoint.com/javascript-function-tostring-method
https://www.javatpoint.com/javascript-date-getdate-method
https://www.javatpoint.com/javascript-date-getday-method
https://www.javatpoint.com/javascript-date-getfullyear-method
https://www.javatpoint.com/javascript-date-gethours-method
https://www.javatpoint.com/javascript-date-getmilliseconds-method
https://www.javatpoint.com/javascript-date-getminutes-method
https://www.javatpoint.com/javascript-date-getmonth-method
https://www.javatpoint.com/javascript-date-getseconds-method
https://www.javatpoint.com/javascript-date-getutcdate-method
https://www.javatpoint.com/javascript-date-getutcday-method
https://www.javatpoint.com/javascript-date-getutcfullyears-method
https://www.javatpoint.com/javascript-date-getutchours-method
https://www.javatpoint.com/javascript-date-getutcminutes-method
https://www.javatpoint.com/javascript-date-getutcmonth-method
https://www.javatpoint.com/javascript-date-getutcseconds-method
https://www.javatpoint.com/javascript-date-sethours-method
https://www.javatpoint.com/javascript-date-setmilliseconds-method
https://www.javatpoint.com/javascript-date-setminutes-method
https://www.javatpoint.com/javascript-date-setseconds-method
https://www.javatpoint.com/javascript-date-setutcdate-method
https://www.javatpoint.com/javascript-date-setutcfullyears-method
https://www.javatpoint.com/javascript-date-setutchours-method
https://www.javatpoint.com/javascript-date-setutcminutes-method
https://www.javatpoint.com/javascript-date-setutcmonth-method
https://www.javatpoint.com/javascript-date-setutcseconds-method
https://www.javatpoint.com/javascript-date-todatestring-method
https://www.javatpoint.com/javascript-date-toisostring-method
https://www.javatpoint.com/javascript-date-tojson-method
https://www.javatpoint.com/javascript-date-tostring-method
https://www.javatpoint.com/javascript-date-totimestring-method
https://www.javatpoint.com/javascript-date-toutcstring-method
https://www.javatpoint.com/javascript-date-valueof-method
https://www.javatpoint.com/javascript-handler-apply-method
https://www.javatpoint.com/javascript-handler-construct-method
https://www.javatpoint.com/javascript-handler-defineproperty-method
https://www.javatpoint.com/javascript-handler-deleteproperty-method
https://www.javatpoint.com/javascript-handler-get-method
https://www.javatpoint.com/javascript-handler-getownpropertydescriptor-method
https://www.javatpoint.com/javascript-handler-getprototypeof-method
https://www.javatpoint.com/javascript-handler-has-method
https://www.javatpoint.com/javascript-handler-isextensible-method
https://www.javatpoint.com/javascript-handler-ownkeys-method
https://www.javatpoint.com/javascript-handler-preventextensions-method
https://www.javatpoint.com/javascript-handler-set-method
https://www.javatpoint.com/javascript-handler-setprototypeof-method
https://www.javatpoint.com/javascript-json-parse-method
https://www.javatpoint.com/javascript-json-stringify-method
https://www.javatpoint.com/javascript-map-clear-method
https://www.javatpoint.com/javascript-map-delete-method
https://www.javatpoint.com/javascript-map-entries-method
https://www.javatpoint.com/javascript-map-foreach-method
https://www.javatpoint.com/javascript-map-get-method
https://www.javatpoint.com/javascript-map-has-method
https://www.javatpoint.com/javascript-map-keys-method
https://www.javatpoint.com/javascript-map-set-method
https://www.javatpoint.com/javascript-map-values-method
https://www.javatpoint.com/javascript-math-abs-method
https://www.javatpoint.com/javascript-math-acos-method
https://www.javatpoint.com/javascript-math-asin-method
https://www.javatpoint.com/javascript-math-atan-method
https://www.javatpoint.com/javascript-math-cbrt-method
https://www.javatpoint.com/javascript-math-ceil-method
https://www.javatpoint.com/javascript-math-cos-method
https://www.javatpoint.com/javascript-math-cosh-method
https://www.javatpoint.com/javascript-math-exp-method
https://www.javatpoint.com/javascript-math-floor-method
https://www.javatpoint.com/javascript-math-hypot-method
https://www.javatpoint.com/javascript-math-log-method
https://www.javatpoint.com/javascript-math-max-method
https://www.javatpoint.com/javascript-math-min-method
https://www.javatpoint.com/javascript-math-pow-method
https://www.javatpoint.com/javascript-math-random-method
https://www.javatpoint.com/javascript-math-round-method
https://www.javatpoint.com/javascript-math-sign-method
https://www.javatpoint.com/javascript-math-sin-method
https://www.javatpoint.com/javascript-math-sinh-method
https://www.javatpoint.com/javascript-math-sqrt-method
https://www.javatpoint.com/javascript-math-tan-method
https://www.javatpoint.com/javascript-math-tanh-method
https://www.javatpoint.com/javascript-math-trunc-method
https://www.javatpoint.com/javascript-number-isfinite-method
https://www.javatpoint.com/javascript-number-isinteger-method
https://www.javatpoint.com/javascript-number-parsefloat-method
https://www.javatpoint.com/javascript-number-parseint-method
https://www.javatpoint.com/javascript-number-toexponential-method
https://www.javatpoint.com/javascript-number-tofixed-method
https://www.javatpoint.com/javascript-number-toprecision-method
https://www.javatpoint.com/javascript-number-tostring-method
https://www.javatpoint.com/javascript-regexp-exec-method
https://www.javatpoint.com/javascript-regexp-test-method
https://www.javatpoint.com/javascript-regexp-tostring-method
https://www.javatpoint.com/javascript-object-assign-method
https://www.javatpoint.com/javascript-object-create-method
https://www.javatpoint.com/javascript-object-defineproperty-method
https://www.javatpoint.com/javascript-object-defineproperties-method
https://www.javatpoint.com/javascript-object-entries-method
https://www.javatpoint.com/javascript-object-freeze-method
https://www.javatpoint.com/javascript-object-getownpropertydescriptor-method
https://www.javatpoint.com/javascript-object-getownpropertydescriptors-method
https://www.javatpoint.com/javascript-object-getownpropertynames-method
https://www.javatpoint.com/javascript-object-getownpropertysymbols-method
https://www.javatpoint.com/javascript-object-getprototypeof-method
https://www.javatpoint.com/javascript-object-is-method
https://www.javatpoint.com/javascript-object-preventextensions-method
https://www.javatpoint.com/javascript-object-seal-method
https://www.javatpoint.com/javascript-object-setprototypeof-method
https://www.javatpoint.com/javascript-object-values-method
https://www.javatpoint.com/javascript-reflect-apply-method
https://www.javatpoint.com/javascript-reflect-construct-method
https://www.javatpoint.com/javascript-reflect-defineproperty-method
https://www.javatpoint.com/javascript-reflect-deleteproperty-method
https://www.javatpoint.com/javascript-reflect-get-method
https://www.javatpoint.com/javascript-reflect-getownpropertydescriptor-method
https://www.javatpoint.com/javascript-reflect-getprototypeof-method
https://www.javatpoint.com/javascript-reflect-has-method
https://www.javatpoint.com/javascript-reflect-isextensible-method
https://www.javatpoint.com/javascript-reflect-ownkeys-method
https://www.javatpoint.com/javascript-reflect-preventextensions-method
https://www.javatpoint.com/javascript-reflect-set-method
https://www.javatpoint.com/javascript-reflect-setprototypeof-method
https://www.javatpoint.com/javascript-set-add-method
https://www.javatpoint.com/javascript-set-clear-method
https://www.javatpoint.com/javascript-set-delete-method
https://www.javatpoint.com/javascript-set-entries-method
https://www.javatpoint.com/javascript-set-foreach-method
https://www.javatpoint.com/javascript-set-has-method
https://www.javatpoint.com/javascript-set-values-method
https://www.javatpoint.com/javascript-string-charat-method
https://www.javatpoint.com/javascript-string-charcodeat-method
https://www.javatpoint.com/javascript-string-concat-method
https://www.javatpoint.com/javascript-string-indexof-method
https://www.javatpoint.com/javascript-string-lastindexof-method
https://www.javatpoint.com/javascript-string-search-method
https://www.javatpoint.com/javascript-string-match-method
https://www.javatpoint.com/javascript-string-replace-method
https://www.javatpoint.com/javascript-string-substr-method
https://www.javatpoint.com/javascript-string-substring-method
https://www.javatpoint.com/javascript-string-slice-method
https://www.javatpoint.com/javascript-string-tolowercase-method
https://www.javatpoint.com/javascript-string-tolocalelowercase-method
https://www.javatpoint.com/javascript-string-touppercase-method
https://www.javatpoint.com/javascript-string-tolocaleuppercase-method
https://www.javatpoint.com/javascript-string-tostring-method
https://www.javatpoint.com/javascript-string-valueof-method
https://www.javatpoint.com/javascript-symbol-for-method
https://www.javatpoint.com/javascript-symbol-keyfor-method
https://www.javatpoint.com/javascript-symbol-tostring-method
https://www.javatpoint.com/javascript-symbol-hasinstance-property
https://www.javatpoint.com/javascript-symbol-isconcatspreadable-property
https://www.javatpoint.com/javascript-symbol-match-property
https://www.javatpoint.com/javascript-symbol-prototype-property
https://www.javatpoint.com/javascript-symbol-replace-property
https://www.javatpoint.com/javascript-symbol-search-property
https://www.javatpoint.com/javascript-symbol-split-property
https://www.javatpoint.com/javascript-symbol-tostringtag-property
https://www.javatpoint.com/javascript-symbol-unscopables-property
https://www.javatpoint.com/javascript-typedarray-copywithin-method
https://www.javatpoint.com/javascript-typedarray-entries-method
https://www.javatpoint.com/javascript-typedarray-every-method
https://www.javatpoint.com/javascript-typedarray-fill-method
https://www.javatpoint.com/javascript-typedarray-filter-method
https://www.javatpoint.com/javascript-typedarray-find-method
https://www.javatpoint.com/javascript-typedarray-findindex-method
https://www.javatpoint.com/javascript-typedarray-foreach-method
https://www.javatpoint.com/javascript-typedarray-includes-method
https://www.javatpoint.com/javascript-typedarray-indexof-method
https://www.javatpoint.com/javascript-typedarray-join-method
https://www.javatpoint.com/javascript-typedarray-keys-method
https://www.javatpoint.com/javascript-typedarray-lastindexof-method
https://www.javatpoint.com/javascript-typedarray-map-method
https://www.javatpoint.com/javascript-typedarray-reduce-method
https://www.javatpoint.com/javascript-typedarray-reduceright-method
https://www.javatpoint.com/javascript-typedarray-reverse-method
https://www.javatpoint.com/javascript-typedarray-set-method
https://www.javatpoint.com/javascript-typedarray-slice-method
https://www.javatpoint.com/javascript-typedarray-some-method
https://www.javatpoint.com/javascript-typedarray-sort-method
https://www.javatpoint.com/javascript-typedarray-subarray-method
https://www.javatpoint.com/javascript-typedarray-values-method
https://www.javatpoint.com/javascript-typedarray-tolocalestring-method
https://www.javatpoint.com/javascript-typedarray-tostring-method
https://www.javatpoint.com/javascript-weakmap-delete-method
https://www.javatpoint.com/javascript-weakmap-get-method
https://www.javatpoint.com/javascript-weakmap-has-method
https://www.javatpoint.com/javascript-weakmap-set-method
https://www.javatpoint.com/javascript-weakset-add-method
https://www.javatpoint.com/javascript-weakset-delete-method
https://www.javatpoint.com/javascript-weakset-has-method
https://bit.ly/2FOeX6S
https://www.javatpoint.com/splunk
https://www.javatpoint.com/spss
https://www.javatpoint.com/swagger
https://www.javatpoint.com/t-sql
https://www.javatpoint.com/tumblr
https://www.javatpoint.com/reactjs-tutorial
https://www.javatpoint.com/regex
https://www.javatpoint.com/reinforcement-learning
https://www.javatpoint.com/r-tutorial
https://www.javatpoint.com/rxjs
https://www.javatpoint.com/react-native-tutorial
https://www.javatpoint.com/python-design-pattern
https://www.javatpoint.com/python-pillow
https://www.javatpoint.com/python-turtle-programming
https://www.javatpoint.com/keras
https://www.javatpoint.com/aptitude/quantitative
https://www.javatpoint.com/reasoning
https://www.javatpoint.com/verbal-ability
https://www.javatpoint.com/interview-questions-and-answers
https://www.javatpoint.com/company-interview-questions-and-recruitment-process
https://www.javatpoint.com/artificial-intelligence-tutorial
https://www.javatpoint.com/aws-tutorial
https://www.javatpoint.com/selenium-tutorial
https://www.javatpoint.com/cloud-computing-tutorial
https://www.javatpoint.com/hadoop-tutorial
https://www.javatpoint.com/data-science
https://www.javatpoint.com/angular-7-tutorial
https://www.javatpoint.com/blockchain-tutorial
https://www.javatpoint.com/git
https://www.javatpoint.com/machine-learning
https://www.javatpoint.com/devops
https://www.javatpoint.com/dbms-tutorial
https://www.javatpoint.com/data-structure-tutorial
https://www.javatpoint.com/daa-tutorial
https://www.javatpoint.com/os-tutorial
https://www.javatpoint.com/computer-network-tutorial
https://www.javatpoint.com/compiler-tutorial
https://www.javatpoint.com/computer-organization-and-architecture-tutorial
https://www.javatpoint.com/discrete-mathematics-tutorial
https://www.javatpoint.com/ethical-hacking-tutorial
https://www.javatpoint.com/computer-graphics-tutorial
https://www.javatpoint.com/software-engineering-tutorial
https://www.javatpoint.com/cyber-security-tutorial
https://www.javatpoint.com/automata-tutorial
https://www.javatpoint.com/net-framework
https://www.javatpoint.com/programs-list
https://www.javatpoint.com/control-system-tutorial
https://www.javatpoint.com/data-mining
https://www.javatpoint.com/data-warehouse
https://www.javatpoint.com/spring-tutorial
https://www.hindi100.com/
https://www.lyricsia.com/
https://www.quoteperson.com/
https://www.jobandplacement.com/
https://www.javatpoint.com/contact-us
https://www.javatpoint.com/subscribe.jsp
https://www.javatpoint.com/privacy-policy
https://www.javatpoint.com/sitemap.xml
https://www.javatpoint.com/sonoo-jaiswal
"""

    urls = urls.split("\n")
    post_urls(urls)