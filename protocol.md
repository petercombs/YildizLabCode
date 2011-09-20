Step 1: Generate a "hole map".
* Use about 1 million holes over a 512x512 CCD (for a coverage of approximately 4 holes/pixel; with my grid of holes, this was about 5,000 frames, but your mileage may vary).  As best as I can tell, it's better to move the grid of holes randomly, and by relatively large amounts (i.e. 2-3 inter-hole distances), rather than doing a raster-scan of the CCD.  There's some speculation that this is related to charge buildup on the CCD, but there's absolutely no evidence that's actually the cause. 

* As an interesting side note, the NTFS file system (and possibly others) bogs down when you have many, many items in the same folder.  I tend to keep a folder of folders, each of which contains 1,000 images.

* Use the python script Processing.py to generate a holes map file.  The default options typically work if you start in the folder containing the folder-of-folders. Otherwise, you may need to use the --specification flag to tell the program where to look.

Step 2: Generate a beads "offset map".
* 
