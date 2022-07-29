# Fibonacci vs Python, Lua, Ruby, and TypeScript

The "compute the nth Fibonacci number" algorithm implemented, tested, and profiled in:

- Python
- Lua
- Ruby
- TypeScript

## Running the programs

```bash
# Python 3.10
python python/main.py
python python/main.py --index 15 --reps 20 --range_start 0 --range_end 5 --range_reps 20

# Lua 5.1
lua lua/main.lua
luajit lua/main.lua

# Ruby 3.0
ruby ruby/main.rb

# TypeScript 4.7
ts-node typescript/main.ts
deno typescript/run main.ts
bun typescript/main.ts
```
