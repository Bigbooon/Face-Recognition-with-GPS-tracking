import geocoder
import haversine as hs

def get_current_gps_coordinates():
    
    g = geocoder.ip('me')
    if g.latlng is not None:
        return g.latlng
    else:
        return None


if __name__ == "__main__":
    coordinates = get_current_gps_coordinates()
    latitude, longitude = coordinates
    classroom = (43.25, 76.9167)
    loc_student = (latitude, longitude)
    distance = hs.haversine(classroom, loc_student)
    if distance < 5:
        print("Student is present")
    else:
        print("Student is not in classroom")