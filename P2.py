#P2

import math

def cam_expos(neutral_setting, photographer_setting):
    # Define dictionaries for mapping f-number, shutter speed, and ISO to numerical values
    aperture_map = {'f/1.4': 1.4, 'f/2': 2, 'f/2.8': 2.8, 'f/4': 4, 'f/5.6': 5.6, 
                    'f/8': 8, 'f/11': 11, 'f/16': 16, 'f/22': 22}
    shutter_speed_map = {'1/4': 1/4, '1/8': 1/8, '1/15': 1/15, '1/30': 1/30, '1/60': 1/60,
                         '1/125': 1/125, '1/250': 1/250, '1/500': 1/500, '1/1000': 1/1000, 
                         '1/2000': 1/2000, '1/4000': 1/4000}
    iso_map = {'100': 100, '200': 200, '400': 400, '800': 800, '1600': 1600, '3200': 3200}
    
    # Parse neutral and photographer settings
    neutral_aperture = aperture_map[neutral_setting[0]]
    neutral_shutter_speed = shutter_speed_map[neutral_setting[1]]
    neutral_iso = iso_map[neutral_setting[2]]
    
    photographer_aperture = aperture_map[photographer_setting[0]]
    photographer_shutter_speed = shutter_speed_map[photographer_setting[1]]
    photographer_iso = iso_map[photographer_setting[2]]
    
    # Calculate differences in stops for aperture, shutter speed, and ISO
    aperture_diff = math.log2(neutral_aperture**2 / photographer_aperture**2)
    shutter_speed_diff = math.log2(photographer_shutter_speed / neutral_shutter_speed)
    iso_diff = math.log2(photographer_iso / neutral_iso)
    
    # Round differences to nearest stop
    aperture_diff = round(aperture_diff)
    shutter_speed_diff = round(shutter_speed_diff)
    iso_diff = round(iso_diff)
    
    # Calculate overall exposure difference
    overall_exposure_diff = aperture_diff + shutter_speed_diff + iso_diff
    
    return (aperture_diff, shutter_speed_diff, iso_diff, overall_exposure_diff)

if __name__ == "__main__":
    # Example usage:
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/1.4', '1/60', '100'])
    print(res) 
