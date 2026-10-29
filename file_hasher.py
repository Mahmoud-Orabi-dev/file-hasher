import hashlib
import sys


def hash_file(path, algo="sha256"):
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_hasher.py <file> [expected_sha256]")
        sys.exit(1)

    path = sys.argv[1]
    digest = hash_file(path)
    print("SHA-256:", digest)

    if len(sys.argv) >= 3:
        expected = sys.argv[2].strip().lower()
        if digest == expected:
            print("MATCH: the file is intact.")
        else:
            print("MISMATCH: the file was changed or is different!")
