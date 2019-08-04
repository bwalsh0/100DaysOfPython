import requests


def main():
    reqCount = 0

    with open(r'.\r_post_titles.txt', 'a') as txt:
        handle_recursive_req(None, txt, reqCount)


def handle_recursive_req(paramId, outFile, reqCount):
    if reqCount > 9: outFile.close(); exit(0)

    baseUrl = 'https://www.reddit.com/r/ucr/new.json?limit=100'
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
        title = postData['title'] + '\n'
        try:
            outFile.write(title)
        except UnicodeEncodeError:
            print("UEE")
            continue
    handle_recursive_req(recurParam, outFile, reqCount)


def sanitize_outfile():
    pass

main()
