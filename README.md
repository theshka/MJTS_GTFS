City of Moose Jaw Transit Service - General Transit Feed Specification
======

[![GitHub License](https://img.shields.io/badge/license-MIT%20License-blue.svg)](https://github.com/theshka/MJTS_GTFS/blob/master/LICENSE.md)
[![Software Version](https://img.shields.io/badge/version-0.0.2-red.svg)](https://github.com/theshka/MJTS_GTFS/archive/v.0.0.2.zip)

---

**MJTS_GTFS** is a python script to generate a [GTFS][] feed using [Google TransitFeed][] for the [City of Moose Jaw Transit Service](http://www.moosejaw.ca/engineering/city-transit/city-of-moose-jaw-transit-division).

## Download
* [Dev-Master](https://github.com/theshka/MJTS_GTFS/archive/master.zip)
* [Version 0.0.2](https://github.com/theshka/MJTS_GTFS/archive/v.0.0.2.zip)

## Requirements
- [Python 2.5+](https://www.python.org/download/releases/2.5/)
- [Google TransitFeed][]

### Data
The data in this dataset was hand-collected from various resources, and
assembled here to be used in transit applications.

>NOTE: This project is **incomplete** and the data here is not ready for production use!

## Usage
The raw-data is not much use in-and-of itself, you will need to use this data
with your own applications, OR check out [Google TransitFeed][] collection of Python scripts to view the data graphically.

### Clone
```
$ git clone https://github.com/theshka/MJTS_GTFS.git
```

### Generate the feed
```
$ cd src
$ python generate_feed.py
```

### View the feed
```
$ transitfeed/schedule_viewer.py output/mjts_gtfs_0.0.2.zip
```

## License
This project is licensed under the [MIT LICENSE](https://github.com/theshka/MJTS_GTFS/blob/master/LICENSE)

## Contributors

### Contributors on GitHub
* [Contributors](https://github.com/theshka/MJTS_GTFS/graphs/contributors)

### Third party libraries
* see [Google TransitFeed][]
* see [GTFS][] Specification

## Contributing
If you would like to help make this software better, please follow our guidelines found in [CONTRIBUTING.md](https://github.com/theshka/MJTS_GTFS/blob/master/CONTRIBUTING.md)

## Contact
* Homepage: http://heshka.com
* E-mail: tyler@heshka.com
* KeyBase: https://keybase.io/theshka

[Google TransitFeed]:https://github.com/google/transitfeed
[GTFS]: https://developers.google.com/transit/gtfs/
