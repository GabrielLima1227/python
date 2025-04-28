import math
import os
import sys
from datetime import datetime

def soma(a, b):
    return a + b


def main():
    print(soma(5, 3))
    now = datetime.now()
    print("Hora atual:", now)
    r = requests.get("https://example.com")
    print(r.status_code)


if __name__ == "__main__":
    main()
