#Pi Plate

Pi Plate is an insanely simple yet powerful way to render Markdown into static webpages.

##How it works

**Configure the project**

Place your Markdown files inside the content folder. Feel free to tweak the theme styles inside the styles folder. You can use one of the preset themes inside the theme folder simply by changing the import in the `global.less` file:

    @import "themes/light.less";

You can even make your own theme.

**Build the project**

    sudo python3 build.py

This will create the compiled CSS and HTML files.

**Host the project**

    sudo python3 server.py &


##Installation and Dependencies

Running this application requires [Tornado Web Server](http://www.tornadoweb.org/en/stable/) and the [Python LESS compiler](https://github.com/lesscpy/lesscpy).

After configuring the dependencies, simply download the most recent copy to the Pi or copy the files to the Pi remotely:

    scp -r ~/Desktop/Pi-Plate/* pi@raspberrypi:~/Pi-Plate/

Configure the project (as described above) and you're all set!

##FAQ

**I don't have a Raspberry Pi. Can I still use this?**

The Raspberry Pi is awesome — you should definitely get one. But yes, you can still use the framework. Place your Markdown in the content folder, start the Python build script, and host the files generated in the compiled folder where ever you want.

The project's build functionality is really the key part of this project, but I also wanted to include the Tornado Web Server to make it a complete packaged bundle.
