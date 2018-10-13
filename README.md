# CSV Pattern Split

## Requirements

Be sure python 3 is installed

## Usage

If your file looks like this:

    foo1,bar1,SAME,baz1,foo2,bar2,SAME,baz2,foo3,bar3,SAME,baz3

Do this:

    ❯ python3 patternsplit.py sample_in.csv --pattern SAME

...and get this:

        foo1,bar1,SAME,baz1
        foo2,bar2,SAME,baz2
        foo3,bar3,SAME,baz3


## Interactive Help

    ❯ python3 patternsplit.py --help
