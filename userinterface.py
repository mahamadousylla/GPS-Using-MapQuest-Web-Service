#Mahamadou Sylla 61549479

import interaction_with_api
import ducktyping

def location_count():
    '''
    prompts user to type in amount of locations they will be traveling to
    along with the destinations they are starting from and going to
    '''
    locations = [] #empty list
    how_many_locations = int(input()) #prompts user to type in amount of locations they will be traveling between
    for num in range(0, how_many_locations): #iterates through amount of locations user will be traveling to
        a_location = input() #for amount of locations user will be traveling to, they will be prompted to specify the location
        locations.append(a_location) #appends each location user will be traveling to, to locations list
    return locations #returns locations list


def output_count():
    '''
    prompts user to typle in amount of outputs/information about
    the trip that they would like to know about
    '''
    outputs = [] #empty list
    how_many_outputs = int(input()) #prompts user to type in amout of ouputs/information about the trip that they would like
    for num in range(0, how_many_outputs): #iterates through amount of outputs/information user would like to know about their trip
        an_output = input() #for amount of outputs/information user would like to know, they will be prompted to specify what output/information they would like to know
        outputs.append(an_output) #appends each output/information user would like to know about their trip to the output list
    return outputs #retuns outputs list


def main_program():
    '''
    main program that prompts user to specify their trip
    and details and what outputs/information about the trip
    they would like to know about
    '''
    url = None #url is set to none

    try:
        directions = ducktyping.Steps() #the created class from the ducktyping module that finds the directions for a specific trip
        total_distance = ducktyping.Total_distance() #the created class from the ducktyping module that finds the total distance for a specific trip
        total_time = ducktyping.Total_time() #the created class from the ducktyping module that finds the total time for a specific trip
        lat_long = ducktyping.Latlong() #the created class from the ducktyping module that finds the latitude and longitude for each specified location for a given trip
        elevation = ducktyping.Elevation() #the created class from the ducktyping module that finds the elevation for each specified location for a given trip

        locations = location_count() #the function returns a list of an entire trip from location to location
        output = output_count() #this function returns a list of of different output choices the user would like to know about a specific trip 
        print('\n')
        url = interaction_with_api.build_url(locations) #given the locations list, the 'build_url' function from the 'interaction_with_api' module constructs a URL that can be passed to the MapQuest API to get information about a specific location
        json_result = interaction_with_api.get_result(url) #given the newly constructed URL, the 'get_result' function from the 'interaction_with_api' module constructs a Python object
        elevation_result = interaction_with_api.elevation_url(json_result) #get the elevation information for each location in the specified trip

        for description in output: #for the different types of output information in the output list
            if description.startswith('STEPS'): #if this output information starts with 'STEPS'
                directions.lookup(json_result) #calls this method from the 'ducktyping' module that gets directions for a trip
                print('\n')
            elif description.startswith('TOTALDISTANCE'): #if this output information starts with 'TOTALDISTANCE'
                print(total_distance.lookup(json_result)) #calls this method from the 'ducktyping' module that gets the total distance for a trip
                print('\n')
            elif description.startswith('TOTALTIME'): #if this output information starts with 'TOTALTIME'
                print(total_time.lookup(json_result)) #calls this method from the 'ducktyping' module that gets the total time for a trip
                print('\n')
            elif description.startswith('LATLONG'): #if this output information starts with 'LATLONG'
                lat_long.lookup(json_result) #calls this method from the 'ducktyping' module that gets the latitude and longitude for each location in a given trip
                print('\n')
            elif description.startswith('ELEVATION'): #if this output information starts with 'ELEVATION'
                elevation.lookup(elevation_result) #calls this method from the 'ducktyping' module that shows the elevation for each location in a given trip

    except:
        print()
        print('NO ROUTE FOUND') #if the try block fails prints this message

    finally:
        if url != None: #if the try statement was successfull the url will no longer be set to None
            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.') #print this copy right message
    

    

if __name__ == '__main__':
    main_program()
