#!/usr/bin/python3
import hidde_4
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
