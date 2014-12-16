##Installing PIL on a Raspberry PI

--download and compile the JPEG library


```wget http://www.ijg.org/files/jpegsrc.v8c.tar.gz```   

```tar xvfz jpegsrc.v8c.tar.gz```

```cd jpeg-8c```

```./configure --enable-shared --prefix=$CONFIGURE_PREFIX```

make

sudo make install


--link the libraries correctly - RASPBERRY PI ONLY

```sudo ln -s /usr/lib/arm-linux-gnueabi/libjpeg.so /usr/lib```

```sudo ln -s /usr/lib/arm-linux-gnueabi/libfreetype.so /usr/lib```

```sudo ln -s /usr/lib/arm-linux-gnueabi/libz.so /usr/lib```

--install rest of the libraries, as well as freetrype and zlib

```sudo apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev```

--Install PIL

```sudo pip install pil```
