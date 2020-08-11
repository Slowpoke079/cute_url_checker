<h1 align="center">
  <br>
  <a href=""><img src="https://github.com/Slowpoke079/cute_url_checker/blob/master/image.PNG" alt="" width="308px;"></a>
  <br>
  Slowpoke079 - cute_url_checker
  <br>
</h1>
A super simple yet effective webapp url HTTP response code checker to see what urls are alive. Quickly filters out dead urls from an url list for you.

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

# How to install?

```console
my@pc:~$ sudo apt install -y git
my@pc:~$ git clone https://github.com/Slowpoke079/cute_url_checker.git
my@pc:~$ sudo apt install python3 python3-pip
my@pc:~$ pip3 install requests
```
