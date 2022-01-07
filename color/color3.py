#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""

    print("Full name is:")

    # print my name in different colors
    print(f"{crayons.red('Kimuli')} {crayons.blue('Danstan')} {crayons.magenta('Mark')} {crayons.green('Ndahiro')}")

# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

