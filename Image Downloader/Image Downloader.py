# imported the requests library
import requests
image_url = "https://images.pexels.com/photos/12880191/pexels-photo-12880191.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object

# send a HTTP request to the server and save
# the HTTL response in a resonse object called r
with open("black-mountain.jpeg", 'wb') as f:

  # Saving received content as a png file in
  # binary format

  # write the contents of the response (r.content)
  # to a new file in binary mode.
  f.write(r.content)