# Fibonacci vs Python, TypeScript, Ruby, and OCaml

## Running the programs

```bash
# Python
python fibo.py  # Execute file
python3 fibo.py # Execute file

# Ruby
ruby fibo.rb # Execute file

# OCaml
ocaml fibo.ml # Execute file

# TypeScript Node
npm install -g ts-node # Install dependencies
ts-node fibo.ts  # Execute file

# TypeScript Deno
deno run fibo.ts # Execute file
```

## Running static checks

```bash
# Python
pip install black flake8 mypy # Install dependencies
black fibo.py   # Run style checker with auto correct
flake8 fibo.py  # Run style checker
mypy fibo.py    # Run type checker

# Ruby
gem install rubocop # Install dependencies
rubocop fibo.rb    # Run style checker
rubocop -A fibo.rb # Run style checker with auto correct
```
