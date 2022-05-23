#
# Example file for parsing and processing JSON
#

import urllib.request
import json


def print_results(data: str) -> None:
    # Use the json module to load the string data into a dictionary
    the_json = json.loads(data)

    # Now we can access the contents of the JSON like any other Python object
    if 'title' in the_json['metadata']:
        print(the_json['metadata']['title'])

    # Output the number of events, plus the magnitude and each event name
    count = the_json['metadata']['count']
    print(str(count) + ' events recorded')

    # For each event, print the place where it occurred
    for i in the_json['features']:
        print(i['properties']['place'])

    # Print the events that only have a magnitude greater than 4
    for i in the_json['features']:
        if i['properties']['mag'] >= 4.0:
            print('%2.1f' % i['properties']['mag'], i['properties']['place'])

    # Print only the events where at least 1 person reported feeling something
    for i in the_json['features']:
        feltReports = i['properties']['felt']
        if feltReports != None:
            if feltReports > 0:
                print(
                    '%2.1f' % i['properties']['mag'],
                    i['properties']['place'],
                    ' reported ' + str(feltReports) + ' times',
                )


def main() -> None:
    url_data = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    webUrl = urllib.request.urlopen(url_data)
    print('result code: ' + str(webUrl.getcode()))

    if webUrl.getcode() == 200:
        data = webUrl.read().decode('utf-8')
        print_results(data)
    else:
        print(
            'Received an error from server, cannot retrieve results '
            + str(webUrl.getcode())
        )


if __name__ == '__main__':
    main()
