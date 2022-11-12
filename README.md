# ForceUrSelf

ForceUrSelf is a Bruteforcing Tool written in Python.
Core functionalities are:

- Ability to use proxies (Tor)
- CLI-Arguments

# Install

1. Clone:

```
git clone https://github.com/FujiwaraChoki/ForceUrSelf.git
```

2. Install PIP dependencies:

```
cd ForceUrSelf
pip3 install -r requirements.txt
```

# Usage

ForceUrSelf takes following Arguments:

- u: Username

- pl: Passwordlist

- p: Proxy (Tor)

- t: Threads

- v: Verbose

- h: Help

# Examples

```
python3 ForceUrSelf.py -u admin -w wordlist.txt -p socks5://
```

```
python3 ForceUrSelf.py -u admin -w wordlist.txt -p socks5:// -t 10
```

```
python3 ForceUrSelf.py -u admin -w wordlist.txt -p socks5:// -t 10 -v
```
