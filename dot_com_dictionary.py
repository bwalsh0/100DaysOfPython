import socket
import sys
import whois
import socks

socket.setdefaulttimeout(2)

sockproto = socket.AF_INET6
s = socks.socksocket(sockproto)
s.settimeout(2)

i = 0
en_dictionary = open('words_alpha.txt')
for line in en_dictionary:
    i += 1
    if i == 100:
        break
    word = line.splitlines()

    suf = '.com'
    url = word[0] + suf

    try:
        resp = whois.whois(url)
    except whois.parser.PywhoisError:
        print(word)
    except socket.timeout:
        print(word, " TIMEOUT")
        continue

    # if not resp.name:
    #     print(word)
    # else:
    #     pass
        # print(resp.name)

    # resp = subprocess.call(['ping', '-l', '2', '-n', '2', '-w', '3', url])
    #
    # if resp == 1:
    #     print(word)

en_dictionary.close()
sys.exit(0)


# WIP: Ping every *.com domain name in the english dictionary to check which ones are still unclaimed
