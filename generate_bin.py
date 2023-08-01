import os


def generate_bin_files(count: int, size: int) -> None:
    for cnt in range(count):
        with open(os.path.join("large_files", str(cnt+1)), "wb") as file:
            file.write(os.urandom(size))


if __name__ == "__main__":
    generate_bin_files(10, 1024*1024)