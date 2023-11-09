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

The instructions below assume you are starting on your **Institution** page >>(see directions in Part 2: A.2-4) and are logged in as an Administrator for your Institution.

The Create Project wizard
-------------------------

In the **Projects** tab on your Institution page, click **[Create New Project]**. This will bring you to the Create Project wizard. The wizard comprises 6 parts: Project Overview, Imagery Selection, Plot Design, Sample Design, Survey, and Rules.

Project Overview
----------------

This section allows you to add general information about the project, including selecting a template (optional), project name, project description, and project options.

1. Use a project template (optional)

   i.   This feature is used to copy all the information—including project info, area, and sampling design—from an existing published project to a new project. This is useful if you have an existing project you want to duplicate for another year or location, or if you are iterating through project design. For a template, you may use any available published or closed project from your institution. You cannot use deleted projects. You cannot use another institution’s private project but you can use another institution’s public project (any website visitor or CEO user). For more on project  privacy settings, see **Visibility** below.

.. tip::
   
   If you do not want to copy another project, simply skip this section, and leave the **Select Template** field set to **Select Project**.

   ii. Click on the **Show Public Projects** checkbox if you would like to view all public projects in CEO that you can use as a template. If you do not check this box, you will only see your institution’s projects.

   iii. Template Filter (Name or ID): To filter the projects, type in a keyword in an existing project’s name or the Project ID Number. You can find the Project ID number by navigating to the project you want to copy and looking at the URL.

   iv. Then click on the dropdown menu under Select Project and click on the project’s name

   v.  When you find the project that you would like to use as a template, click on the project name, then click **Load** to load the template information.

   vii. Click on **Clear** to clear all template information.

.. note::
   If you select a project under **Select Template**, and then if you clear the project selection the Imagery Preview in the next section may display only gray/white. Change the **Default Imagery** to any other source and then back to the source you are interested in and the basemap will reappear.

   viii. Loading a template will create two checkboxes under **Copy Options**, **Copy Template Plots and Samples** and **Copy Template Widgets**. They are checked by default.

      a. If **Copy Template Plots and Samples** is checked, the Plot Review and Sample Design sections will only display an overview of the number of plots, etc. Uncheck this box to change those parameters.
      
      b. **Copy Template Widgets** refers to Geo-Dash options covered in >>Part 6: Geo-Dash Implementation.

2. Enter the project’s **Name** and **Description**.

   i.   The **Name** should be short and will be displayed on the Home page as well as the project’s Data Collection page.

   ii.  You should keep the **Description** short but informative. Users will see these if they click on the project’s pin on the map on the home page. You will also see this when you are administering your project.

   iii. If you are using a template, the **Name** and **Description** will automatically be populated. Be sure to change this to reflect your new project.

3. Select the project’s Visibility.

   i. The Privacy Level radio button changes who can view your project, contribute to data collection, and whether admins from your institution or others creating new projects can use your project as a template.

   -  **Public: All:** All users can see and contribute data to your project. Admins can use your project as a template.

   -  **Users: Logged in Users:** Any user logged into CEO can see and contribute to your project. Admins can use your project as a template.

   -  **Institution: Group Members:** Members of your institution can see and contribute to your project. Admins from other institutions cannot use your project as a template.

   -  **Private: Group Admins:** Only your Institution’s Admins can see and contribute to your project. Admins from other institutions cannot use your project as a template.

4. Select Project Options.

   i. The first option is **Show GEE Script Link on the Collection page.**

      a. This allows users in Data Collection to click on a button labeled Go to GEE Script.

      b. This button will take them to a website with additional information about the plot. An example is shown here:

.. image::

         There are three panels. On the far left, there is a Sentinel 2 composite
         of the last 12 months. It is colored using an infrared color composite
         (near infrared, mid infrared, red). In the center are Landsat 8 and
         Landsat 7 Color Yearly mosaics, with a slider so you can choose between
         years. On the right are NDVI graphs of the plot from MODIS, Landsat 7/8,
         and Sentinel 2. For the Landsat 7/8 and Sentinel graphs, you can click a
         point on the graphs to load specific images in the left and center
         panels.

   ii. The second option is **Show Extra Plot Columns on Collection Page**.

      a) This option is only useful if you are using .csv or .shp files to define your **Plot Design**.

      b) If you have additional columns in your .csv or .shp files, such as elevation information or land cover class, data collectors will be able to see them on the **Data Collection** page under **Plot Information**.

   iii. The third option is **Collect Plot Confidence on Collection Page.** If you want users to be able to tell you how certain they are of their answers to the survey questions, the confidence slider will allow them to assign a value 1-100, where 100 is completely confident of their answers; this value applies to the entire plot. This info will be included in your plot and sample CSV downloads.

   iv.  The fourth option is **Auto-launch Geo-Dash.** This will automatically open the Geo-Dash interface in a new window or new tab when the data collector navigates to a new plot. Unchecking this option means that data collectors will need to click on the Geo-Dash icon under **External Tools** in the **Data Collection** interface.

5. Click **[Next]** when you are finished.

Imagery Selection
-----------------

In the Imagery Selection pane, you can change the default basemap imagery and the imagery basemaps that are available to users in data collection.

1. You can change the Default Imagery, which specifies the default imagery that users will see when they begin data collection on your project.

   i.    You may choose any of the imagery options available to your institution.

   ii.   The default (public) options are MapBox Satellite, Mapbox Satellite w/Labels, and Planet NICFI Public.

   iii.  The Imagery Preview will display the current selection.

   iv.   Your users can switch between all the available imagery layers during analysis.

   v.    PlanetMonthly, PlanetDaily, and SecureWatch do not allow for large area data pulls, so it should not be your default basemap (users will just see a white screen).

   vi.   You will need to set a different default basemap and have your data collectors switch to PlanetDaily once they have zoomed in on a plot to interpret.

   vii.  If your project is comparing land use and cover changes between two years, select one of your focal years’ WMS imagery as the default imagery here. Your users can then easily switch between this year’s imagery and the other year’s imagery in data collection.

   viii. You will need to first set up the imagery feed for one date period under the institution imagery management panel. Refer to instructions in >>Part 4, Section B.

.. note::
   
   Maxar has deprecated multiple data products previously available in CEO, including: DigitalGlobeRecentIMagery; DigitalGlobeRecentImagery+Streets; DigitalGlobeWMSImagery; and EarthWatch.

2. Public Imagery

   i.  This imagery is available for all institutions. If you have a public project, all users (including those not logged in) can see the imagery.

   ii. Click the checkbox next to each imagery source you would like to have available for your project.

3. Private Institution Imagery.

   i.  This imagery will only be visible to institution members, even if you have your project set to public.

   ii. Click the checkbox next to each imagery source you would like to have available for your project.

4. Click **[Next]** when you are finished.

 