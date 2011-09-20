Step 1: Generate a "hole map"
=============================

* Use about 1 million holes over a 512x512 CCD (for a coverage of approximately 4 holes/pixel; with my grid of holes, this was about 5,000 frames, but your mileage may vary).  As best as I can tell, it's better to move the grid of holes randomly, and by relatively large amounts (i.e. 2-3 inter-hole distances), rather than doing a raster-scan of the CCD.  There's some speculation that this is related to charge buildup on the CCD, but there's absolutely no evidence that's actually the cause. 

* As an interesting side note, the NTFS file system (and possibly others) bogs down when you have many, many items in the same folder.  I tend to keep a folder of folders, each of which contains 1,000 images.

* Use the python script Processing.py to generate a holes map file.  The default options typically work if you start in the folder containing the folder-of-folders. Otherwise, you may need to use the --specification flag to tell the program where to look.


Step 2: Imaging
===============

* Capture your two-color movies.

* Using fluorescent beads that are roughly equally bright in both channels, capture movies of approximately 300-500 beads, leaving each bead stable for ~10-15 frames.  Depending on the stability of your system, you may want to do this fairly frequently (I typically do two rounds of protein imaging, then a single round of bead imaging, then two more rounds of protein.

Step 3: Data-processing
=======================

* Localize beads using WHTrackHighRes.  Select only beads that are bright, but not saturated, and well separated from each other.

* This process is very tedious, so I came up with a couple scripts which, combined with the CellCounter plugin in ImageJ, makes it only slightly less tedious.
  + For one frame in a series, click on every object of interest in the upper half-field using a Type 2 marker in the Cell Counter.  In the current version of the software, the lower half can also be selected using Type 1 markers, but if it isn't , will be automatically calculated using the input map.  This is a huge time saver.
  + For the rest of the frames in that series, click at least once with a type 2 marker, anywhere.
  + Make sure to leave at least 2-3 completely unmarked frames between each series.
  + Use the CellCounter to save the XML file.  I almost always accept the default name.
  + Turn the XML file that CellCounter saves into a WHTrackHighRes-compatible spotlist using XML2Spotlist.  From IPython, it will look something like this: *run XML2spotlist -m 0916-map_1_20 Red-s1_1.xml* 

  + Actually track the spots.  Through some tinkering, I've put together ProcessAll.m, a matlab script that will call WHTrackHighRes on all the spotlistsi in the current folder with appropriate parameters. This can take a while to run, but requires no human input.

* 
