<h1 align="center">
  <br>
  <a href=""><img src="https://github.com/Slowpoke079/cute_url_checker/blob/master/image.PNG" alt="" width="308px;"></a>
  <br>
  Slowpoke079 - cute_url_checker
  <br>
</h1>
A super simple yet effective webapp url HTTP response code checker to see what urls are alive. Quickly filters out dead urls from an url list for you.

# How to install?

```console
my@pc:~$ sudo apt install -y git
my@pc:~$ git clone https://github.com/Slowpoke079/cute_url_checker.git
my@pc:~$ sudo apt install python3 python3-pip
my@pc:~$ pip3 install requests
```

# How to use?
- Make git clone
```console
my@pc:~$ git clone https://github.com/Slowpoke079/cute_url_checker.git
```

- filter url file "file" and print all output to terminal:
```console
my@pc:~$ cat file | python3 cute_url_checker.py
```

- filter url file "file" and print all output to output.txt:
```console
my@pc:~$ cat file | python3 cute_url_checker.py > output.txt
```

(Note: "file" should contain only http:// or https:// links. otherwise the links will be discarded by the filtering process.)

# Use case?
For example: I normally run tools like gobuster and gospider to fetch me a lot of webapp urls for a pentest or bug-whatever-audit. But i want to filter out all "not on scope/domain urls", and all dead urls.
So i filter the "gospider output url-list file for example" on domain urls only with grep and then test all links in file with cute_url_checker.py to filter out all dead links.
```console
$ /home/$USER/go/bin/gospider -s http://192.168.56.4/ --sitemap --robots --no-redirect -c 10 -d 5 -o /home/$USER/Desktop/outputJS/gospider_out/
$ cat /home/$USER/Desktop/outputJS/gospider_out/* | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u > /home/$USER/Desktop/outputJS/gospider_grep_filtered
$ cat gospider_grep_filtered | grep 192.168.56.4 > file
$ cat file | python3 cute_url_checker.py > output.txt
```
