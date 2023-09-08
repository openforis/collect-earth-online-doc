Project Creation
================

After you have created an Institution or joined an Institution with Admin privleges and loaded any desired imagery into your INstitution, you are ready to create a new project.

Setting project goals
---------------------

Before starting a data collection effort in CEO, make sure you have concrete goals, indicators, and metrics for your initiative. While this manual focuses on technical issues, other resources are available to help you create these goals, indicators, and metrics. Some helpful resources include:

-  The *Road to Restoration:* *A Guide to Identifying Priorities and Indicators for Monitoring Forest and Landscape Restoration*, found
      at:
      http://www.fao.org/in-action/forest-landscape-restoration-mechanism/resources/detail/en/c/1253837/.
      This guide from FAO & WRI outlines steps toward setting goals,
      choosing indicators, and defining metrics.

If your project is focused on land use or land cover classification, you also need to have a classification scheme and an interpretation key. A classification scheme should be exhaustive, exclusive, consistent with the purpose of the work, and sufficiently descriptive. The scheme can be either single level or hierarchical and it does not need to be of uniform detail. Data collectors refer to an interpretation key—a collection of rules, imagery, and guidance—to classify land cover elements. A comprehensive interpretation key allows data collectors to produce more consistent and reliable results.

-  See Chapters 2 & 3 of the Theoretical Manual from Collect Earth Online, found at https://collect.earth/downloads/CEO_Theoretical_Manual.pdf.

Designing a project is an iterative process, and you will probably need to make multiple edits to projects in CEO as you refine your goals, land use or land cover classification schemes, imagery sources, etc. These changes can be made to a project before your project is published. This means that you can create a project and collect test data in it, and edit any errors you find before publishing the project.

Some things can also be changed after a project is published, including imagery. For example, if you realize after you have created a project that you have forgotten to add an imagery layer, you can add it after project setup with the steps from Part 3.

The survey questions that are asked about each survey point cannot currently be changed after the project is published. Do not start data collection until you are sure that your survey questions are correct.

The instructions below assume you are starting on your **Institution**
page (see directions in Part 2: A.2-4) and are logged in as an
Administrator for your Institution.

A. **Create a new project (wizard)**

1. In the Projects tab on your Institution page, click [Create New
   Project]. This will bring you to the Create Project wizard.

In response to user feedback, CEO implemented a project creation wizard
in the November 2020 update.

2. The wizard comprises 6 parts, each covered in one of the sections
   below.

   A. **Project Overview**

This section allows you to add general information about the project,
including selecting a template (optional), project name, project
description, and project options.

1. Use a project template (optional)

i.   This feature is used to copy all the information—including project
     info, area, and sampling design—from an existing published project
     to a new project. This is useful if you have an existing project
     you want to duplicate for another year or location, or if you are
     iterating through project design. For a template, you may use any
     available published or closed project from your institution. You
     cannot use deleted projects. You cannot use another institution’s
     private project but you can use another institution’s public
     project (any website visitor or CEO user). For more on project
     privacy settings, see **Visibility** below.

ii.  If you do not want to copy another project, simply skip this
     section, and leave the **Select Template** field set to–– **Select
     Project** -.

iii. Click on the **Show Public Projects** checkbox if you would like to
     view all public projects in CEO that you can use as a template. If
     you do not check this box, you will only see your institution’s
     projects.

iv.  Template Filter (Name or ID): To filter the projects, type in a
     keyword in an existing project’s name or the Project ID Number. You
     can find the Project ID number by navigating to the project you
     want to copy and looking at the URL.

v.   Then click on the dropdown menu under Select Project and click on
     the project’s name

vi.  When you find the project that you would like to use as a template,
     click on the project name, then click **Load** to load the template
     information.

vii. Click on **Clear** to clear all template information.

..

   If you select a project under **Select Template**, and then if you
   clear the project selection the Imagery Preview in the next section
   may display only gray/white. Change the **Default Imagery** to any
   other source and then back to the source you are interested in and
   the basemap will reappear.

viii. Loading a template will create two checkboxes under **Copy
      Options**, **Copy Template Plots and Samples** and **Copy Template
      Widgets**. They are checked by default.

a) If **Copy Template Plots and Samples** is checked, the Plot Review
      and Sample Design sections will only display an overview of the
      number of plots, etc. Uncheck this box to change those parameters.

b) **Copy Template Widgets** refers to Geo-Dash options covered in Part
   6: Geo-Dash Implementation.

2. Enter the project’s Name and Description.

i.   The **Name** should be short and will be displayed on the Home page
     as well as the project’s Data Collection page.

ii.  You should keep the **Description** short but informative. Users
     will see these if they click on the project’s pin on the map on the
     home page. You will also see this when you are administering your
     project.

iii. If you are using a template, the **Name** and **Description** will
     automatically be populated. Be sure to change this to reflect your
     new project.

3. Select the project’s Visibility.

i. The Privacy Level radio button changes who can view your project,
   contribute to data collection, and whether admins from your
   institution or others creating new projects can use your project as a
   template.

-  **Public: All:** All users can see and contribute data to your
   project. Admins can use your project as a template.

-  **Users: Logged in Users:** Any user logged into CEO can see and
   contribute to your project. Admins can use your project as a
   template.

-  **Institution: Group Members:** Members of your institution can see
   and contribute to your project. Admins from other institutions cannot
   use your project as a template.

-  **Private: Group Admins:** Only your Institution’s Admins can see and
   contribute to your project. Admins from other institutions cannot use
   your project as a template.

4. Select Project Options.

i. The first option is **Show GEE Script Link on the Collection page.**

a) This allows users in Data Collection to click on a button labeled Go
      to GEE Script.

b) This button will take them to a website with additional information
   about the plot. An example is shown here:

There are three panels. On the far left, there is a Sentinel 2 composite
of the last 12 months. It is colored using an infrared color composite
(near infrared, mid infrared, red). In the center are Landsat 8 and
Landsat 7 Color Yearly mosaics, with a slider so you can choose between
years. On the right are NDVI graphs of the plot from MODIS, Landsat 7/8,
and Sentinel 2. For the Landsat 7/8 and Sentinel graphs, you can click a
point on the graphs to load specific images in the left and center
panels.

ii. The second option is **Show Extra Plot Columns on Collection Page**.

a) This option is only useful if you are using .csv or .shp files to
      define your **Plot Design**.

b) If you have additional columns in your .csv or .shp files, such as
   elevation information or land cover class, data collectors will be
   able to see them on the **Data Collection** page under **Plot
   Information**.

iii. The third option is **Collect Plot Confidence on Collection Page.**
     If you want users to be able to tell you how certain they are of
     their answers to the survey questions, the confidence slider will
     allow them to assign a value 1-100, where 100 is completely
     confident of their answers; this value applies to the entire plot.
     This info will be included in your plot and sample CSV downloads.

iv.  The fourth option is **Auto-launch Geo-Dash.** This will
     automatically open the Geo-Dash interface in a new window or new
     tab when the data collector navigates to a new plot. Unchecking
     this option means that data collectors will need to click on the
     Geo-Dash icon under **External Tools** in the **Data Collection**
     interface.

5. Click **[Next]** when you are finished.

   A. **Imagery Selection**

In the Imagery Selection pane, you can change the default basemap
imagery and the imagery basemaps that are available to users in data
collection.

1. You can change the Default Imagery, which specifies the default
   imagery that users will see when they begin data collection on your
   project.

i.    You may choose any of the imagery options available to your
      institution.

ii.   The default (public) options are MapBox Satellite, Mapbox
      Satellite w/Labels, and Planet NICFI Public.

iii.  The Imagery Preview will display the current selection.

iv.   Your users can switch between all the available imagery layers
      during analysis.

v.    PlanetMonthly, PlanetDaily, and SecureWatch do not allow for large
      area data pulls, so it should not be your default basemap (users
      will just see a white screen).

vi.   You will need to set a different default basemap and have your
      data collectors switch to PlanetDaily once they have zoomed in on
      a plot to interpret.

vii.  If your project is comparing land use and cover changes between
      two years, select one of your focal years’ WMS imagery as the
      default imagery here. Your users can then easily switch between
      this year’s imagery and the other year’s imagery in data
      collection.

viii. You will need to first set up the imagery feed for one date period
      under the institution imagery management panel. Refer to
      instructions in Part 4, Section B.

..

   Maxar has deprecated multiple data products previously available in
   CEO, including: DigitalGlobeRecentIMagery;
   DigitalGlobeRecentImagery+Streets; DigitalGlobeWMSImagery; and
   EarthWatch.

2. Public Imagery

i.  This imagery is available for all institutions. If you have a public
    project, all users (including those not logged in) can see the
    imagery.

ii. Click the checkbox next to each imagery source you would like to
    have available for your project.

3. Private Institution Imagery.

i.  This imagery will only be visible to institution members, even if
    you have your project set to public.

ii. Click the checkbox next to each imagery source you would like to
    have available for your project.

4. Click **[Next]** when you are finished.

   A. **Plot Design—Background**

A well-prepared sample can provide a robust estimate of the parameters
of interest for the population (percent forest cover, for example). This
is often the most important factor in producing a reliable inventory or
accuracy assessment. The goal of a sample is to provide an unbiased
estimate of some population measure (e.g. proportion of area), with the
smallest variance possible, given constraints including resource
availability.

The first step of the built in CEO sample design is the plot design. The
second step, selecting samples within a plot, is covered in the next
section (Sample (point) design). Using these two steps, many sampling
designs are possible with CEO. For information on uploading your own
sample as a .csv or .shp file, please see Part 4: Plot & Sample
Design--CSV & SHP.

For example, suppose you are quantifying forest cover on a landscape.
For this approach, sample points are used to classify land cover and are
then summarized at the plot level to create an estimate of the plot’s
forest cover percent. Information about plots can then be used to
estimate the forest cover at the landscape level and detect patterns or
trends. The accuracy of your landscape level estimates will depend on
how many plots you classify & how variable the landscape is, among other
factors. More detailed theoretical information is available in CEO’s
Project Development Manual (found at
https://collect.earth/downloads/CEO_Theoretical_Manual.pdf).

Also, some terminology might help for the two types of sampling
available in CEO. **Simple random sampling** means that all points have
an equal probability of being selected. It produces unbiased parameters.
However geographic balance with small sample sizes can be difficult.
Also, rare classes may not receive sufficient coverage. If you have rare
classes you want to detect, we highly recommend using a stratified
sampling approach. For this, you can create a stratified sample in SEPAL
(available online at `sepal.io <about:blank>`__) or using QGIS or ArcGIS
and import it using the upload csv or shp (see Part 4: Part 4: Plot &
Sample Design--CSV & SHP). There will also be a stratified sample option
coming to CEO soon.

The second type is **systematic gridded sampling**. This is a grid of
points placed over the landscape at regular intervals. This provides
excellent geographic balance, but it is not possible to calculate
unbiased estimates of population metric variance.

There are two main approaches for specifying an area of interest (AOI)
and sampling design: 1. using CEO’s built-in system and 2. Creating a
sample in another program (QGIS, ArcGIS, etc.) and importing it into
CEO. We will first discuss the built-in sampling design, and then
discuss uploading your own sample as a .csv or .shp file.

B. **Plot Design—CEO’s built in system**

CEO’s built in system enables users to create sampling designs using an
easy-to-use interface. There are two key parts, selecting the AOI and
Plot Generation.

1. Select your AOI. There are three approaches.

i. The easiest way to select your project AOI is by drawing a box in the
   map window in the right hand pane (Collection Map Preview).

a) Locate your area of interest by zooming in/out using the scroll wheel
      of your mouse, or the + and – boxes in the map window. You can pan
      the map by clicking on it and dragging the map window.

b) Hold the CRTL-key (command key on a Mac) down and draw a box while
   keeping the left mouse key pressed down.

c) Hold the SHIFT-key down and draw a box to zoom in.

d) The coordinate boxes will populate once the box is drawn and you let
   your mouse key go. Coordinates are displayed in lat/long using
   **WGS84 EPSG:4326**.

ii. You can also manually enter your Boundary Coordinates into the boxes
    provided.

.. image:: media/image2.png
   :width: 0.30208in
   :height: 0.30208in

iii. | The third approach is to upload a project boundary shapefile. To
       use this option, click on the **[Upload project boundary]**
       button. Navigate to your file, and click **[Open]**. Your
       shapefile should be a zipped folder with the requisite shapefile
       component pieces (.shp, .prj, etc.). Once you click open, you
       should see the **File:** text populate with your file name and
       your project boundary appear in the Collection Map Preview pane.
     | Please note that if you have multi-part polygons each one will be
       assigned the number of plots indicated. This is indicated in the
       green text.

|image2|\ You can upload shapefiles with multiple shapes for stratified
sampling (coming soon). Each strata will appear with its corresponding
area in hectares. The number of plots will be **per strata**. This is
indicated in the green text.
