# Location Converter

This brane package converts locations (cities, states etc.) to the country they belong to. 

## Installation

If on Linux or MacOS first run:

``` chmod +x run.py ```

Otherwise/then:

```console
brane build container.yml
brane push location 1.0.0
```

Or install using the brane import function: 
```
brane import lucasdegeus/braneLocation --kind ecu
```

## Usage

```brane
import location;

let locations := ["rotterdam", "berlin", "paris", "ohio"];

let keys := [**insert key(s)**];

convert_location(locations, keys);
```


## Notes
This package accepts any array of strings. If a location is mapped to a country, it will be added to the result array. In case no mapping is found 'None' will be added as the result.

*the library geocode, which aids in converting the locations to countries, requires a key. On https://www.geonames.org/login one can create a new account and a key that can be used. For quick (and limited) access the key "wdps14_2" can be used.
