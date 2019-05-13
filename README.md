# ICASSP-Exporter

Get your conference schedule in your personal calendar.


**Disclaimer:** Only tested on iOS.

## Installation

```
conda env create -f environment.yaml
conda activate icassp_exporter
```

## Steps

* Compose your schedule for the conference
* In the app, go to the settings and "Send Backup to Support"
* Send it to you (it's an SQLite database)
* run `python export.py -i example.icassp-ios-backup`

It will export an ICS file which you can then open with your favourite tool.

## Adapt Timezone

This is a quick hack. I had to adjust my timezone handling.

```
python export.py -i example.icassp-ios-backup -o -1
```


If you find this tool helpful, I take cocktail vouchers.
