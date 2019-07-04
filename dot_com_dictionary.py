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
file_output = open('dot_coms.txt', 'a')

for line in en_dictionary:
    i += 1
    # if i == 100:
    #     break
    word = line.splitlines()

    url = word[0] + '.com'

    try:
        whois.whois(url)
    except whois.parser.PywhoisError:
        file_output.write(word[0] + '\n')
        print(i)
        # print(word)
    except socket.timeout:
        file_output.write(word[0] + ' TIMEOUT' + '\n')
        print(i)
        # print(word, " TIMEOUT")
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
file_output.close()
sys.exit(0)

# WIP: Ping every *.com domain name in the english dictionary to check which ones are still unclaimed
