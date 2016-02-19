#Mahamadou Sylla 61549479

class Steps:
    def lookup(self, json_object):
        '''
        takes in a json object and
        finds out directions about
        a particular trip
        '''
        directions = [ ] #empty list
        for dictionary in json_object['route']['legs']: #we are at the dictionary under [route][legs]
            for subdict in dictionary['maneuvers']: #we go in another layer deep and sublist is another dictionary inside dictionary[maneuvers]
                directions.append(subdict['narrative']) #in this dictionary, add all narratives to the list 'directions'
        print('DIRECTIONS') #print this message
        for narrative in directions: #for every narrative in this list
            print(narrative) #prints narrative
        return #returns and leaves function
                
            
class Total_distance:
    def lookup(self, json_object):
        '''
        takes in a json object and
        finds the total distance about
        a particular trip
        '''
        return 'TOTAL DISTANCE: ' + str(round(json_object['route']['distance'])) + ' miles' #prints 'Total distance' along with the total amount of miles the trip is

                          
class Total_time:
    def lookup(self, json_object):
        '''
        takes in a json object and
        finds out the total time about
        a particular trip
        '''
        return 'TOTAL TIME: ' + str(round(json_object['route']['time']/60)) + ' minutes' #prints 'Total time' along with the total amount of time it will take to complete the trip


class Latlong:
    def lookup(self, json_object):
        '''
        takes in a json object and
        finds out the lattitude and
        longitude about a particular trip
        '''
        latLng = [ ] #empty list
        index = 0 #used as an index. To be used as iteration
        print('LATLONGS') #prints this message to the console
        for dictionary in json_object['route']['locations']: #for the dictionary in this dictionary
            latLng.append(dictionary['latLng']['lat']) #appends the latitude to the 'latLng' list
            latLng.append(dictionary['latLng']['lng']) #appends the longitude to the 'latLng' list
            if str(latLng[index]).startswith('-'): #if the lattitude is negative
                latLng[index] = str(latLng[index]).replace('-', '') #removes the negative sign
                print('{:.2f}S {:.2f}E'.format(float(latLng[index]),float(latLng[-1]))) #prints the latitude in this format showing it is South
            elif str(latLng[-1]).startswith('-'): #if the longitude is negative
                latLng[-1] = str(latLng[-1]).replace('-', '') #removes the negative sign
                print('{:.2f}N {:.2f}W'.format(float(latLng[index]),float(latLng[-1]))) #prints the longitude in this format showing it is East
            elif str(latLng[index]).startswith('-') and latLng[-1].startswith('-'): #if the lattitude and longitude are both negative
                latLng[index] = str(latLng[index]).replace('-', '') #removes the negative sign
                print('{:.2f}S {:.2f}W'.format(float(latLng[index]),float(latLng[-1]))) #prints the latitude and longitude in this format showing it is South and East respectively
            else: #otherwise
                print('{:.2f}N {:.2f}E'.format(float(latLng[index]),float(latLng[-1]))) #prints the latitude and longitude in this format showing it is North and West respectively

            index += 2 #this is used to grab the lattidue and longitude as pairs as the latLng list is increasing by these 2 elements at the same time
        return #leaves function
                                                                       
class Elevation:
    def lookup(self, json_object):
        '''
        takes in a json object and
        finds out elevation details about
        a particular trip
        '''
        print('ELEVATIONS') #prints this message
        for item in json_object: #this object is a list, so for every item in this list
            item = round((float(item)) *3.280952380952381) #converts elevation to feet
            print(item) #print item
        print()
        return #leaves function
