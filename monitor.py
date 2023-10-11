import numpy as np
import time
from sense_hat import SenseHat
from easysnmp import Session

def calculate_utilization(sample, sample_rate, max_capacity_bps):
    # Calculate the data rate per second (sample_rate)
    data_rate_bps = sample / sample_rate  

    # Calculate the utilzation percentage
    utilization_percentage = (data_rate_bps / max_capacity_bps) * 100 * 8
    
    return utilization_percentage


def scale_to_buckets(number, min_value, max_value, num_buckets):
    # Calculate the range of values in each bucket
    bucket_range = (max_value - min_value) / num_buckets
    
    # Calculate the bucket index for the given number
    bucket_index = int((number - min_value) / bucket_range)
    
    # Ensure the bucket index is within the valid range [0, num_buckets - 1]
    bucket_index = max(0, min(bucket_index, num_buckets - 1))
    
    return bucket_index


def update_grid(grid_to_update, bucket_index):
    bucket_string = [1 if i <= bucket_index else 0 for i in range(8)]   
    grid_to_update = np.column_stack((grid_to_update, bucket_string))
    grid_to_update = np.delete(grid_to_update, 0, 1)
    
    return grid_to_update


def main():
    # Initialize important variables
    min_utilization = 0
    max_utilization = 100
    bucket_count = 8              # Size of the display is 8x8
    max_capacity_bps = 600000000  # 100 Mbps
    sample_rate = 4               # How often to take a sample from the switch (seconds)
    pixel_not_lit = [0, 0, 0]     # RGB value for pixels that aren't lit
    pixel_lit = [255, 0, 0]       # RGB value for pixels that make up thebg

    # Set up the 2d NumPy array to internally represent the SenseHat display 
    matrix = np.zeros((8, 8), dtype=int)

    # Intitalize the SenseHat object, clear it, and set the brightness
    sense = SenseHat()
    sense.clear()
    sense.low_light = True
     
    # Create an SNMP session to be used for all our requests
    snmp_session = Session(hostname='192.168.0.3', community='public', version=2)

    # Flag
    first_get = True

    while True:
        octets = int(snmp_session.get('.1.3.6.1.2.1.2.2.1.10.3').value)
         
        if first_get:
            last_octets = octets
            first_get = False
        else:
            octet_change = octets - last_octets
            last_octets = octets
            
            util_percent = calculate_utilization(octet_change, sample_rate, max_capacity_bps)
            bucket_index = scale_to_buckets(util_percent, min_utilization, max_utilization, bucket_count)
            matrix = update_grid(matrix, bucket_index)  
            flipped_matrix = np.fliplr(matrix)
            
            
            print("Octets: " + str(octets))
            print("Octet change: " + str(octet_change))
            print("Util: " + str(util_percent))
            print("Bucket Index:" + str(bucket_index) + '\n')
            print(flipped_matrix)


            senshat_display = [pixel_lit if num == 1 else pixel_not_lit for num in flipped_matrix.flatten()]
            #print(senshat_display)
            sense.set_pixels(senshat_display)
            
        time.sleep(sample_rate)
            

main()
    