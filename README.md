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

- p: Use Proxy (Tor)

- v: Verbose Output

- h: Help

# Examples

```
python3 ForceUrSelf.py -u admin -pl wordlist.txt --url http://example.com/login.php
```

```

```

python3 ForceUrSelf.py -u admin -pl wordlist.txt -p --url http://example.com/login.php

```

```

python3 ForceUrSelf.py -u admin -pl wordlist.txt -p -v --url http://example.com/login.php

```

```
