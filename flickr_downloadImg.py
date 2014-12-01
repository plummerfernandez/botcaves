# with help from Jonas Lund:
# http://pzwart3.wdka.hro.nl/wiki/User:Jonas_Lund/ImageMerger

import flickrapi
from subprocess import call

flickr = flickrapi.FlickrAPI("xxxxxxxxxxxxx", "xxxxxxxxxxxxx", cache = True)


#https://www.flickr.com/services/api/flickr.photos.search.html
photos = flickr.photos.search(tags='"face"', per_page='1')


for photo in photos[0]:
	pid = photo.attrib['id']
  	photoSizes = flickr.photos_getSizes(photo_id=pid)  
  	flickSrc = photoSizes[0][3].attrib['source']
  	print flickSrc
  	segements = flickSrc.rpartition('/')
  	for s in segements:
  		flickrFile = s
  		
  	ext = flickrFile.partition(".")
  	flickTmp = "flicktmp.{0}".format(ext[2])
  	print flickTmp
  	#download
  	cmd = "wget {0} -O /Users/xxxxxxx/{1} -q".format(flickSrc, flickTmp)
  	call(cmd, shell=True)

    
