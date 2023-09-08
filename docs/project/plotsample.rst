
2. In the Plot Generation section, you can specify the type and number
   of sample plots.

i. **Spatial Distribution** defines the distribution of the sample
   points. In CEO, you can specify either a random or a gridded (spatial
   systematic) sampling approach.

a) Random sampling has the advantage of being extremely simple and
      producing unbiased parameters that are straightforward to
      calculate. However, geographic balance is not certain with smaller
      sample sizes, and rare classes may not be adequately sampled
      unless the sample size is large.

b) Systematic sampling has the advantage of providing excellent
   geographic balance. However, it is not possible to calculate a truly
   unbiased estimate of the variance of population metrics when using
   systematic sampling. Additionally, if patterns in your landscape
   match up with the spacing of your systematic gridded points, you will
   produce a very biased estimate.

c) If you select **Random**, you will need to provide the number of
   plots for the whole project.

d) If you select **Gridded**, you will need to provide the spacing
   between the centers of the plots (in meters).

ii. CEO will provide an estimate of how many plots will be generated for
    your project based on your sampling design.

*Using CEO’s sampling, the maximum number of plots for a project is
5,000*. For gridded sampling, you may need to increase the space between
plots to avoid exceeding 5,000 plots.

3. Plot Shape can be either a Circle or a Square.

i.   You will need to specify the **Diameter** in meters.

ii.  These sizes should be driven by the needs of your project.

iii. If they are small, your users will need to zoom out significantly
     to see the relevant background imagery because CEO automatically
     centers and zooms in to the plot’s boundaries.

4. You can now choose to assign users plots to review using the User
   Assignment feature, and implement quality control for your plots
   using the **Quality Control** dropdown. See Section H: Plot
   Design—Quality Control Options for more.

5. Click “Next” when you are finished.

   A. **Sample Design—CEO’s built-in system**

Here we determine how many sample points are within each plot, and
whether they are sampled using random sampling or gridded sampling.

1. Under Spatial Distribution:

i.   With **Random sampling** sample points will be randomly distributed
     within the plot boundary. You will also need to specify the
     **Number of Samples** per plot.

ii.  With **Gridded sampling**, sample points will be arranged on a grid
     within the plot boundary. You will need to specify the distance
     between points within the plot under **Sample resolution** (m).

iii. With **Center** a sample point will be placed in the center of the
     plot; you do not need to specify anything else.

iv.  With **None,** you will not predefine any samples. This requires
     users to draw their own samples during collection.

2. For any of these Spatial Distributions, you can click the checkbox
   next to Allow users to draw their own samples to enable proactive
   sampling.

Proactive sampling enables data collectors to draw points, lines, and
polygons directly onto the map to create their own samples. The data
collector then answers questions about each shape.\ |image3|

Proactive sampling is useful for collecting training data to inform
random forest and machine learning models. It can also increase the
accuracy of land use land cover area estimates by allowing users to map
the entire area of the plot instead of sample points within the
plot.\ |image4|

*Using CEO’s sampling, the maximum number of sample points per plot is
200.*

*Using CEO’s sampling, the maximum total number of sample points for the
project (number of plots times the number of points/plot) is 50,000.*

If you need more plots or samples, please create your sampling design in
another program and upload it to CEO using the .csv or .shp file format
and directions in the next section.

A.  **Plot & Sample Design—CSV & SHP files**

While the default sampling design will work for many users, you may want
to create your own sampling design and upload it to CEO using the .csv
or .shp file capability. For example, this functionality is useful when:
you want to draw your sample plots from within a shape other than a
rectangle (e.g. the outline of a region or country) or if you want to do
any stratification in your sampling design. You can create a .csv or
.shp with your desired sampling plots/points through services and
applications including Sepal, ArcGIS (e.g.
https://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-random-points.htm),
and QGIS (e.g.
https://freegistutorial.com/how-to-create-random-points-inside-polygon-on-qgis/).

As when using CEO’s built-in system, you can now choose to assign users
plots to review using the **User Assignment** feature and implement
quality control for your plots using the **Quality Control** dropdown.
See Plot Design—Quality Control Options for more.

*Using .csv and .shp files, the maximum number of plots is 50,000 and
the total sample point limit is 350,000.*

*You must use WGS84 EPSG:4326 format for coordinates in both .csv and
.shp files.*

*Example CSV and SHP files are available for download. When used, the
plots should spell out “OK” when used to create a project.*

*For .csv files*, specify plot centers by uploading a .csv with these
columns: LON, LAT, PLOTID.

You can also upload a second file where you specify your own sample
point centers by uploading a .csv with these columns: LON, LAT, PLOTID,
SAMPLEID. LON and LAT can also be LONGITUDE and LATITUDE. You can have
additional columns with data about your sample plots and points but they
MUST come after these key fields.

If you do not specify the column names correctly (spelling or order),
you will get the following error:

Longitude should be between -180 and 180, while latitude should be
between -90 and 90. If you mix them up, you may get an error if your
longitude is greater than 90 or less than -90 (when this is mixed up
with latitude, it is ‘above’ the pole). Double check these values.

You can upload just one file for the plot centers OR two files, one for
the plot centers and one for the point centers. When your .csv files are
fit the above specifications, follow the directions below.

For one file with just the plot centers:

1. Under Plot Generation, select **CSV File**.

2. Then, click on **[Upload plot file]** and navigate to the .csv on
   your computer with your sample plot centers.

3. After you upload the file, the file name will appear next to
   **File:**.

4. You will need to specify the **Plot Shape** and corresponding
   **Diameter**.

5. You will also need to specify your **Sample (Point) Design**, as in
   Part 4: F Sample Plot Design above.

For two .csv files, one with plot centers and one with sample point
centers,

1. Follow steps 1-4 above for the Plot Design.

2. In step 4, it is important that you specify a plot size that is large
   enough to contain your points if they are also uploaded through a
   .csv or .shp. This will not be a problem if you use the built-in
   sample point design function.

3. Then, under Sample Design, set Spatial Distribution to CSV File.

4. Click on **[Upload sample file]** and navigate to your .csv on your
   computer. Click Open and the file name will appear next to **File.**

5. Note that you can also choose SHP file and upload a shape file at
   this point..

6. You can click the checkbox next to Allow users to draw their own
   samples to enable proactive sampling.

*For .shp files*, you can specify your own plot boundaries by uploading
a zipped Shapefile (containing SHP, SHX, DBF, and PRJ files) of polygon
features. Each feature must have a unique PLOTID field. LON and LAT are
not required for polygons.

You will also need to upload a second file where you specify your own
sample points. This can be a .csv with these columns: LON, LAT, PLOTID,
SAMPLEID. LON and LAT can also be LONGITUDE and LATITUDE. It can also be
a zipped .shp file (containing SHP, SHX, DBF, and PRJ files). Each
feature must have PLOTID and SAMPLEID fields. Either points or polygons
will work for the sample point file, though point files must include LON
and LAT. As with .csv files, you can have additional fields with
information about your plots and points if and only if they come after
these key fields.

If you do not specify your PLOTID in the sample point .csv or .shp zip
file, you will get the following errors:

You can zip your files easily in Windows by selecting the relevant
files, right clicking on one, and the clicking **[Send to] ->
[Compressed (zipped) folder]**.

For a Mac, select the relevant files, right click on one of the files,
and select **[Compress Items]** from the pop-up menu.

When your .shp files fit the above specifications, follow the directions
below.

1. Under Plot Generation, set **Spatial Distribution** to **SHP File**.
   You must have the radio point selected before the button to upload
   becomes available.

2. Then, click on **[Upload plot file]** and navigate to your zipped
   .shp file.

3. Click [Next]. Under Sample Design, set Spatial Distribution to SHP
   File.

4. Click on [Upload sample file] and navigate to the zipped .shp file
   with your sample point points or polygons and select it.

5. This will also work with CSV File.

When you download your collected data, any column with extra information
that were present in the uploaded .csv and .shp files will be preserved
in the downloaded data (See Part 6: B). These columns can also be
displayed in the Data Collection pane (see Part B Project
Overview).\ |image5|
