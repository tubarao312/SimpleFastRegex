import simple_fast_regex as sfr
import regex as re
import time

TEXT = "This is a test"

# Rust Implementation
start = time.time()
engine = sfr.RegexEngine(["test", "this pattern doesn't exist"])
rust_compile_time = time.time() - start
print(f"Rust took {rust_compile_time} seconds to compile the Regex.")

start = time.time()
engine.get_pattern_matches(TEXT) # [0] because only the first pattern matches
rust_match_time = time.time() - start
print(f"Rust took {time.time() - start} seconds to run compiled Regex.")

print(f"----------------------------------")

# Python implementation
start = time.time()
compiled_patterns = [re.compile("test"), re.compile("this pattern doesn't exist")]
python_compile_time = time.time() - start
print(f"Python took {python_compile_time} seconds to compile the Regex.")

start = time.time()
matches = [pattern.search(TEXT) for pattern in compiled_patterns]
python_match_time = time.time() - start
print(f"Python took {time.time() - start} seconds to run compiled Regex.")