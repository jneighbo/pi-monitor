import time
import numpy as np
from easysnmp import Session

def calculate_utilization(sample, sample_rate, max_capacity_bps):
    data_rate_bps = sample / sample_rate  # Data rate per second
    utilization_percentage = (data_rate_bps / max_capacity_bps) * 100
    
    return utilization_percentage


def scale_to_buckets(number, min_value, max_value, num_buckets):
    # Calculate the range of values in each bucket
    bucket_range = (max_value - min_value) / num_buckets
    
    # Calculate the bucket index for the given number
    bucket_index = int((number - min_value) / bucket_range)
    
    # Ensure the bucket index is within the valid range [0, num_buckets - 1]
    bucket_index = max(0, min(bucket_index, num_buckets - 1))
    
    return bucket_index


def main():
    min_value = 0
    max_value = 100
    num_buckets = 8

    matrix = np.zeros((8, 8), dtype=int)

    max_capacity_bps = 100000000  # 1 Gbps
    sample_rate = 5

    # Create an SNMP session to be used for all our requests
    session = Session(hostname='192.168.0.3', community='public', version=2)

    first_get = True

    while True:
        octets_pdu = session.get('.1.3.6.1.2.1.2.2.1.10.3')
        octets = int(octets_pdu.value)
 
        if first_get == True:
            lastoctets = octets
            first_get = False
        else:
            octet_change = octets - lastoctets
            lastoctets = octets
            util_percent = calculate_utilization(octet_change, sample_rate, max_capacity_bps)
            bucket_index = scale_to_buckets(util_percent, min_value, max_value, num_buckets)
            print("Octet change: " + str(octet_change))
            print("Util: " + str(util_percent))
            print("Bucket Index:" + str(bucket_index) + "\n")


            
            
        time.sleep(sample_rate)

            

main()
    