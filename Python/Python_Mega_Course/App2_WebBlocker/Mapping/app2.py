# # Section 11 - Application 2: Creating Webmaps with Python and Folium
# # 86 - Demostration of the Web Mapping Application
# # Web application with an interactive map with multiple layers, each one representing
# # different informations, with on and off swiitching of the layers.
#
# # Folium - translates python to form html, javascript and css code
# # use a map object
# import folium
# # see what arguments are in the map object using dir and help
# # location takes the latitude and longitude, in a list format
# # we can pass addresses using the geocoder package
# from geopy.geocoders import Nominatim
# def string_to_coordinate(address):
#     nom = Nominatim()
#     location = nom.geocode(address)
#     if location != None:
#         return [location.latitude, location.longitude]
#     else:
#         return None
#
# nom=Nominatim()
# address = 'Rua Sebastião Antônio Carlos, 260, Belo Horizonte, Minas Gerais, Brasil'
# coord = string_to_coordinate(address)
# print(coord)
# my_map = folium.Map(location=coord, zoom_start = 23)
#
# # 88 - Add a Point Marker Feature to the Map
# # We will use the Marker or the CircleMarker method
# # We will add a child object folium.Marker to our map to add a point marker
# my_map.add_child(folium.Marker(location=coord, popup='My House!',
#                 icon=folium.Icon(color='purple', icon_color='lightgreen')))
# my_map.save("Map.html")

# # a better aproach is to use folium.FeatureGroup, in this manner we can add
# # multiple features to our map
# # 89 - Adding Multiple Markers to the Map
# # we need to iterate trhough the coordinates, in a form of a list of lists
# # or incrementing the coordinates that we have and repeat the fg.add_child(marker)
# # code in the for loop

# # # so, the complete code for now is:
# import folium
# from geopy.geocoders import Nominatim
#
# def string_to_coordinate(address):
#     nom = Nominatim()
#     location = nom.geocode(address)
#     if location != None:
#         return [location.latitude, location.longitude]
#     else:
#         return None
#
# #
# # nom=Nominatim()
# # address = 'Rua Sebastião Antônio Carlos, 260, Belo Horizonte, Minas Gerais, Brasil'
# # coord = string_to_coordinate(address)
# coord = [-19.858996, -43.999206]
# my_map = folium.Map(location=coord, zoom_start = 22)
# # creates the featuregroup
# fg = folium.FeatureGroup(name='My Map')
# # for loop to add multiple coordinates
# for i in range(10):
#     # changes the coordinates summing a factor of i
#     coord[0]+=0.05*i
#     coord[1]+=0.05*i
#     # passes the marker as child object to the featuregroup
#     fg.add_child(folium.Marker(location=coord, popup='My House!'+' + '+str(i),
#                     icon=folium.Icon(color='purple', icon_color='lightgreen')))
# # and then we pass the fg as a child for the map object
# my_map.add_child(fg)
# # save the map in a html file
# my_map.save("Map.html")

# the next step is to add markers from datafiles.
# complete code without lesson:
import folium
import pandas as pd

# 92 - Color Based Point Markerse
# Change the colors of the markers to reflect a range of elevation
# receives an elevation value and returns a color string

# 93 - Coding Exercise: style the markers as displyed in the lesson
# use folium.CircleMarker method

# 96 - Using GeoJson datafiles
# adding a third layer to the map: polygon layers
# Markers represents locations, polygons represents areas
# We need the approrpiate data to work with polygons
# We can use the folium.GeoJson method

# 98 - Color Based Polygon features
# changing the colors of the country polygons based on the population

# 99 - Adding a Layer Control Panel
# Turn the marker and polygon layer on a off with a command
# the control would be added as a child object for the map object
# the method used is folium.LayerControl
def elev_color(elev):
    if elev>2500.0:
        return '#B22222'
    elif elev>2000.0:
        return '#FFD700'
    elif elev>1500.0:
        return '#4B0082'
    elif elev>1200.0:
        return '#9370DB'
    elif elev>1000.0:
        return '#48D1CC'
    elif elev>500.0:
        return '#9ACD32'
    else:
        return '#98FB98'

# initialize a map with a random location in USA
USA_coord = [39.147118, -105.385366]
volc_map = folium.Map(location=USA_coord, zoom_start=5)
# creates a featuregroup to store the Markers
fg = folium.FeatureGroup(name='Volcano Markers')
# open the volcano datafile into a pd dataframe
df_volc = pd.read_csv('Volcanoes_USA.txt')
# iterates trough the dataframe getting the information and creating the Markers
# in a feature group
# if I use df_volc.head(), which contains only 5 elements, the map works fine!
for i in range(df_volc.shape[0]):
    info_str = "Name: {}\nLocation: {}\nElevation: {} m\nStatus: {}".format(
                df_volc.iloc[i]['NAME'], df_volc.iloc[i]['LOCATION'],
                df_volc.iloc[i]['ELEV'], df_volc.iloc[i]['STATUS'])
    volc_coord = [df_volc.iloc[i]['LAT'], df_volc.iloc[i]['LON']]
    # adds the information to the foldergroup
    pop_up=folium.Popup(info_str, parse_html=True)
    # fg.add_child(folium.Marker(location=volc_coord, popup=pop_up,
    #             icon=folium.Icon(color=elev_color(df_volc.iloc[i]['ELEV']))))
    #
    fg.add_child(folium.CircleMarker(location=volc_coord, popup=pop_up, radius=5,
                fill=True, fill_opacity=0.8, color=elev_color(df_volc.iloc[i]['ELEV'])))

# creates a different feature group for the polygons so the layer control can
# distinguish the marker and polygon layers
fg_p = folium.FeatureGroup(name='Population')

# adds the GeoJson info into the feature group
# the world.json file has a bunch of different information about all the contries
# in the wold, such as population, geographic location, etc.
data_file = open('world.json', 'r', encoding='utf-8-sig').read()
# style function expects a lambda function
fg_p.add_child(folium.GeoJson(data=data_file,
                            style_function=lambda x: {'fillColor':'green'
                            if x['properties']['POP2005'] < 10000000 else
                            'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# passes the markers to the map
volc_map.add_child(fg)
volc_map.add_child(fg_p)
# we need to specify two different feature groups to account for the two different kinds of maps
volc_map.add_child(folium.LayerControl())
# saves the map
volc_map.save('Volcano_Map.html')




# app alternative idea
# open trekking map website, with all trails added by users displayed
# you can select a trail and download the GPS coordinates by clicking in one of
# the treck points
# you can see different layers, activating different kinds of trails, images of
# the places (coordinates from the .jpg camera file) in attachement links
# also, the username that made the trekking, report, photos, etc, contribuition
