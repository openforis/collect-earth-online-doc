Project Information Interface
=============================

If you are navigating back to the Project Information (not visiting right after project creation), you can reach this page by finding your Institution on the Home page left panel. Click the [Edit] icon next to the project name to get to the Project Information/Review Project page. The Project Information Interface has two components: Project Details on the left and Project Management on the right.

Project Details
---------------

The **Project Detail** pane includes an overview of your project, including sample collection design, imagery selection, the AOI boundary, and survey questions. 

The **Collection Design** will now show the location of a subset of your plots (a maximum number can be displayed). 

The **Plot Design** and **Sample Design** sections will show a summary of the choices you made or the .csv and .shp files you uploaded. 

**Survey Questions** shows all the **Survey Cards** you created, along with the corresponding **Component Type, Answers, and Rules.**

Project Management
------------------

The **Project Management** pane includes project publication information and important links to manage your project. 

Project Status
^^^^^^^^^^^^^^

First, examine the **Date Created**, **Date Published**, and **Date Closed** for your project. If your project is not published yet, the **Date Published** will not be present. There is also text describing your project status:

- Draft Mode projects: This project is in draft mode. Admins can review, edit, and test collecting the project. Publish the project in order for users to begin collection. Any data collected in a Draft Mode project will not be retained.
- Published projects: This project is published. Users can begin collecting. Limited changes to the project details can be made. Close the project to prevent anymore updates. 
- Closed projects: This project is closed. The project is closed to all changes. Reopen the project for additional collection.

Modify Project Details
^^^^^^^^^^^^^^^^^^^^^^

Next, examine the important links for your project:

- **Publish Project**: Clicking on this will publish your project and allow users to collect data. Note that if a project is not “Published” *only the admins of the institution can see it, not the members*.
- **Close Project**: If you have a published project, you can close it and stop data collection by clicking this button.
- **Edit Project**: This button will take you back to the Project Creation Wizard.

  - When your project is in DRAFT MODE, you can change all aspects of your project.
  - When your project is PUBLISHED, you can change the **Project Name, Description, and Privacy Level**.
  - Delete Project: This will permanently delete your project.

If you accidentally publish a faulty project, you can use it as the template for a revised project and not lose all your work.

External Links
^^^^^^^^^^^^^^

1. Configure Geo-Dash

   i. Clicking on **[Configure Geo-Dash]** will open the Geo-Dash configuration interface.
   ii. For more detail, please see :ref:`geo-dash-implementation`.

2. Collect

   - This will take you to your project data collection interface so you can start collecting data right away.

3. Project Dashboard

   - If you click on **[Project Dashboard]** you will see an overview of the AOI, along with the number of members, contributors, total plots, flagged plots, analyzed plots, unanalyzed plots, and the date the project was created, published and closed.
   - Admins do not count towards the project’s member count.

.. thumbnail:: ../_images/projinfo1.png
    :title: The project dashboard.
    :align: center
    :width: 50%

Export Data
^^^^^^^^^^^

There are three data download options. Two are downloaded in .csv, which can be opened in programs like Microsoft Excel or imported into data analysis software like R:

- Download Plot Data, which downloads your data summarized by plot, 
- Download Sample Data, which downloads your raw data, with information for each point within each plot as its own row. 

The third allows you to download the plot and sample shapes, and an be opened in desktop GIS programs like QGIS.

- Download SHP, which contains the plots and samples as polygons.

All data downloaded from CEO will be in the WGS84 EPSG:4326 projection.

**Download Plot Data**

Downloaded .csv data from Download Plot Data will have the following columns:

1. **PLOT_ID:** the CEO-assigned unique sample plot number or the user provided Plot ID (for .csv and .shp files).
2. **CENTER_LON** and **CENTER_LAT** are the geographic coordinates of the center of your sample plots.
3. **SIZE_M** and **SHAPE** describe the size in meters and the shape (circle or square) of the sample plot.
4. **SAMPLE_POINTS** indicates the number of samples in each plot.
5. **EMAIL** is the user id (email address) of the person that classified the plot.
6. **FLAGGED**: This will be FALSE for plots where data was collected and for plots where data has not been collected yet. It will be TRUE when a user has flagged the quality of the background map as not good enough to analyze the samples (e.g. due to clouds or poor image resolution).

   - Plots can either be flagged or saved by a user, but not both.
   - If a user flags the plot, then goes back and enters data and saves the plot, the plot will not be flagged.

7. **FLAGGED_REASON**: A user provided reason for flagging the plot.
8. **CONFIDENCE**: Collected user confidence.
9. **COLLECTION_TIME**: date and time the user collected the plot data. Time in UTC.
10. **ANALYSIS_DURATION**: Amount of time, in seconds, the user spent analyzing the plot.
11. **COMMON_SECUREWATCH_DATE**: Most common SecureWatch date used.
12. **TOTAL_SECUREWATCH_DATE**: Number of SecureWatch dates used.
13. If you used a .csv or .shp file for plot design, any additional data columns you uploaded will be preserved in the .csv download. They will be preceded by PL_(column name).
14. All the following columns will have information about each of the survey questions broken down by answer. They are labeled **QUESTION TEXT:ANSWER TEXT**. For example, LULC:Built Surface would indicate that “LULC” was the question and “Built Surface” was the answer. In the plot summary download, these are quantified as fraction (max 1) of the sample points in the plot that were assigned that answer.

    - For example, suppose you have four sample points within your plot and two answers (e.g. land cover class) to choose from.
    - If one sample point is assigned to one answer and the other three points to the second answer, the data when downloaded will say ‘25’ for the first answer and ‘75’ for the second answer.
    - For proactive sampling, percentages are based on sample count, NOT AREA.

**Download Sample Data**

If you would like your plot data analyzed differently, the Download Sample Data option is a better fit. Downloaded .csv data from Download Sample Data will have the following columns:

1. **PLOT_ID**: the CEO-assigned unique sample plot number or the user provided Plot ID (for .csv and .shp files).
2. **SAMPLE_ID**: the CEO-assigned unique sample point number or the user provided Sample ID (for .csv and .shp files).
3. **LON** and **LAT** are the geographic coordinates of the center of your sample points.
4. **EMAIL:** is the user id (email address) of the person that classified the plot.
5. **FLAGGED**: This will be FALSE for plots where data was collected and for plots where data has not been collected yet. It will be TRUE when a user has flagged the quality of the background map as not good enough to analyze the samples (e.g. due to clouds or poor image resolution).
6. **COLLECTION_TIME**: The date and time when the user classified the plot. Time zone is UTC.
7. **ANALYSIS_DURATION**: Time in seconds that the user took to analyze the plot. 
8. **IMAGERY_TITLE**: Name of the Imagery layer that the user had selected while analyzing the plot.
9. **IMAGERY_ATTRIBUTIONS**: Any attribution for the imagery used.

.. note::
      
      If multiple imagery sources were used, only the name of the last imagery layer used will be recorded. There is no way to know all the layers used by the user, e.g. if you want to check that two years of imagery were used.

10. If you used a .csv or .shp file for sample plot design, any additional data columns you uploaded will be preserved in the .csv download. They will be preceded by PL_(column name).
11. If you used a .csv or .shp file for sample point design, any additional data columns you uploaded will be preserved in the .csv download. They will be preceded by SMPL_(column name).
12. All the following columns will have information about each of the survey questions. They will be labeled **QUESTION TEXT**, where question text is the literal text of the question.

If you are using SecureWatch imagery, you will have four additional columns:

13. **IMAGERYDATESECUREWATCH** will have a value for any samples which were classified while a specific date was selected from the imagery date dropdown.
14. **IMAGERYSTARTDATESECUREWATCH**, **IMAGERYENDDATESECUREWATCH**, and **FEATUREPROFILESECUREWATCH** will have values for any samples which were classified while a date range and feature profile were selected. 
15. Imagery properties are associated with samples (not plots) because users are free to change these properties while  classifying samples. Thus, any given plot may have some of its samples classified with one map image and other samples classified with a different map image.
