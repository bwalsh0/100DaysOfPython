import requests

retrieved_text = set()
files = [r'.\askreddit_content', r'.\casualconv_content']


def main():
    reqCount = 1

    get_user_comments()
    # handle_recursive_req(None, reqCount)
    # with open(r'.\post_authors.txt', 'a') as txt:
    #     for i in retrieved_text:
    #         txt.write(i + '\n')
    #     txt.close()
    #     exit(0)


def get_user_comments():
    for userList in files:
        with open(userList + '_authors.txt', 'r') as txt, open(userList + '_comments.txt', 'a') as outTxt:
            for user in txt.readlines():
                baseUrl = 'https://www.reddit.com/user/' + user + '/comments/.json?limit=100'
                response = requests.get(baseUrl, headers={'User-agent': 'JsonGrab'})
                if not response.ok:
                    print("Error", response.status_code)
                    exit()

                data = response.json()['data']
                allPosts = data['children']

                for post in allPosts:
                    postData = post['data']
                    try:
                        outTxt.write(postData['body'] + '\n')
                    except UnicodeEncodeError:
                        print("** UEE exception caught")
                        continue


def handle_recursive_req(paramId, reqCount):
    if reqCount > 1: return
    print("Parsed page No.", reqCount, " -- Approx.", (reqCount) * 100, " total posts.")

    baseUrl = 'https://www.reddit.com/r/askreddit/hot.json?limit=100'
    if paramId is not None:
        baseUrl += "&after=" + paramId
    response = requests.get(baseUrl, headers={'User-agent': 'JsonGrab'})
    if not response.ok:
        print("Error", response.status_code)
        exit()
    reqCount += 1

    data = response.json()['data']
    recurParam = data['after']
    allPosts = data['children']

    for post in allPosts:
        postData = post['data']
        retrieved_text.add(postData['author'])
    handle_recursive_req(recurParam, reqCount)

        #     try:
        #     outFile.write(title + '\n')
        # except UnicodeEncodeError:
        #     print("** UEE exception caught")
        #     continue


def sanitize_outfile():
    pass

main()
