import requests
import time
import argparse

parser = argparse.ArgumentParser(description='VirusTotal Report Query Tool')
parser.add_argument('-f', '--file', required=True, type=str, help='File containing list of IOCs (md5s, URLs, IP Addresses, or domains) delineated by new lines (/n)')
parser.add_argument('-of', '--output_files', action='store_true', help='Will output files with IOC list based number of detections for the IOC')
parser.add_argument('-nf', '--NoFile', action='store_true', help='Will output results to the console instead of a file')
parser.add_argument('-k', '--key', required=True, type=str, help='VirusTotal API Key')
args = parser.parse_args()

def main():
    file = args.file

    with open(file) as f:

        high_confidence = ''
        moderate_confidence = ''
        low_confidence = ''
        not_detected = ''

        for i in f:
            resource = i
            print(resource.strip('\n') + ' scanned')
            apikey = args.key
            url = 'https://www.virustotal.com/vtapi/v2/file/report'
            params = {'apikey': apikey, 'resource': resource}
            response = requests.get(url, params=params)
            data = response.json()

            try:

                if 2 >= data['positives'] >= 1:
                    low_confidence += resource
                elif 3 <= data['positives'] <= 6:
                    moderate_confidence += resource
                elif data['positives'] >= 7:
                    high_confidence += resource

            except:
                not_detected += resource

            time.sleep(15)

    if args.NoFile:

        print('High: ' + high_confidence)
        print('Moderate: ' + moderate_confidence)
        print('Low: ' + low_confidence)
        print('Not Found: ' + not_detected)

    elif args.output_files:

        if len(high_confidence) > 1:
            with open('high_conf.txt', "w") as hc:
                hc.write('These IOCs are set at high confidence due to having 7 or more positive hits on VirusTotal!')
                hc.write(high_confidence)
        else:
            print('No high confidence IOCs found!')
        if len(moderate_confidence) > 1:
            with open('mod_conf.txt', "w") as mc:
                mc.write('These IOCs are set at moderate confidence due to having more than 3 hits on VirusTotal, but less than 7 hits. ')
                mc.write(moderate_confidence)
        else:
            print('No moderate confidence IOCs found!')
        if len(low_confidence) > 1:
            with open('low_conf.txt', "w") as lc:
                lc.write('These IOCs are set at low confidence due to having 2 or less detections on VirusTotal!')
                lc.write(low_confidence)
        else:
            print('No low confidence IOCs found!')
        if len(not_detected) > 1:
            with open('not_detected.txt', "w") as nd:
                nd.write('These IOCs have not been detected by any vendor on VirusTotal...')
                nd.write(not_detected)
        else:
            print('All IOCs submitted found')

    quit()

main()
