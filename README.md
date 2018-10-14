# CSV Pattern Split

This is a fork of csvsplit that has been tweaked for a particular usage.  If I didn't make this fork just for you, it's probably not what you want--go check out master.

## Requirements

Be sure python 3 is installed

## Usage

This command will fix the columns in ra_in.csv and write the fixed file to one called ra_out.csv

    ❯ python3 csvsplit.py ra_in.csv > ra_out.csv

## Warnings

We're relying on the presence of '2.21822E+12' as a signal that the row starts.  We're also relying on no field containing a comma.

If these assumptions fail, the columns will be a mess.  Now that we understand the file, adapting to such a failure should be trivial.
