Preparing for Data Collection
=============================

Allow pop-ups
-------------

If it is your first-time collecting data with Collect Earth Online, or you have switched computers, you may need to allow pop-ups from the CEO site. CEO uses pop-up windows to display additional, relevant information about each plot through the Geo-Dash interface.

How to enable pop-ups varies based on the browser you are using. The most used browsers are discussed below. However, if your browser is not covered, simply search online for your browser name & “allow pop-ups” and the search engine should return relevant results.

**For Google Chrome:**

#. Check the address bar. If it is marked with a pop-up blocked icon (see image below), click on the **[popup blocked]** warning.
#. In the popup window that appears, select **Always allow pop-ups from https://collect.earth/.** Then click **[Done]**.
#. If there is no icon, follow the directions here: `Chrome Support <https://support.google.com/chrome/answer/95472>`__.

.. thumbnail:: ../_images/preparing1.png
   :title: The pop-up blocked icon for Chrome.
   :align: center

**For Mozilla Firefox:**

#. Check for a yellow bar below the address bar (see image below). If there, click on the **[Options]** button.
#. In the popup window that appears, select **Allow pop-ups for** collect.earth.
#. If there is no icon, follow the directions here: `Mozilla Support <https://support.mozilla.org/en-US/kb/pop-blocker-settings-exceptions-troubleshooting#w_pop-up-blocker-settings>`__.

.. thumbnail:: ../_images/preparing2.png
   :title: The pop-up blocked icon for Firefox.
   :align: center

Option 1: Work on a public project
----------------------------------

1. From the **Home** page, you can begin collecting data on public projects. There are map pins representing each project at the project location.
2. Select a project by first clicking on a **[map pin]**. Then from the pop-up **Project info** menu, click on the name of one of the projects in the pop-up window.

.. thumbnail:: ../_images/preparing3.png
   :title: Joining a public project.
   :align: center

3. This will take you to the **project’s homepage**, a screen that shows a **Map** of the whole study region on the left & the **Data Collection Toolbar** on the right.
4. Under **Plot Navigation**, Click the green **[Go to first plot]** button to begin collecting information.

.. thumbnail:: ../_images/preparing4.png
   :title: The project's homepage.
   :align: center

Option 2: Select a project from an institution
----------------------------------------------

1. If your institution has a specific project you want to work on, make sure you are logged in and then click on your institution’s name on the left-hand side of the **Home** page. You may want to use the **Enter text to filter** box to find your institution.
2. A drop-down list of the institution’s available projects will open. Select the project of interest by clicking on the project’s name.

.. thumbnail:: ../_images/preparing5.png
   :title: Navigating to a project from an institution.
   :align: center
   :width: 60%

3. This will take you to the project’s home screen as described above.
4. Click the **[Go to first plot]** button to begin collecting information.
5. You can also go to a project through the **Institution’s** page via the **info button**. There are three colors of projects on the **Institution** page. 

   - Blue-green highlighted project names have completed data collection.
   - Yellow project names are partly collected.
   - Red project names have no data collected.

The analysis screen
-------------------

First, make sure you clicked the **[Go to first plot]** button.

Now we will familiarize ourselves with the analysis screen. 

.. tip::
   
   You can access help for the analysis screen at any time by clicking on the purple ? in the top right hand corner of the screen. The help function will point out important features of the data collection page.
   
   .. thumbnail:: ../_images/preparing6.png
      :title: The help for the analysis screen.
      :group: preparing
      :align: center


Map window
^^^^^^^^^^

On the left hand side is the map window:

1. Your **sample plot** will show up as a yellow circle or square in the map window. The sample shape is dependent on how the project has been designed.
2. Each **sample point** is identified with a black circle until it is assigned a label. 

.. tip::
   
   You can change the color of the unassigned sample points from black to white by selecting the corresponding color radio button next to “Unanswered Color” on the right-hand panel.

3. You can zoom in and out using the blue + and – buttons in the upper left-hand corner of the map window, or by scrolling your mouse wheel.
4. Information about the imagery source is shown at the top of the screen.

.. _options-and-survey-questions:

Options and Survey Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the right-hand side are all of the navigation, external tool options, imagery options, and survey questions.

**Navigation options:**

As an institution Member, the **Navigate Through** dropdown menu allows you to choose between:

- **Default**: This will navigate through plots assigned to you and any available unanalyzed plots. In general, you will not need to switch the navigation mode from this option.
- **Unanalyzed Plots**: This option allows you to collect data on unanalyzed plots to contribute to your project.
- **Analyzed plots**: Review your previously analyzed plots. This option will allow you to correct mistakes etc. for previously analyzed plots.
- **Flagged plots**: Review plots you have flagged. 

.. thumbnail:: ../_images/preparing7.png
   :title: Institution member navigation options.
   :width: 60%
   :align: center

As an institution Administrator, the **Navigate Through** dropdown menu ALSO allows you to choose between:

- **Analyzed plots**: Examine plots analyzed by any user.
- **Flagged plots**: Examine plots flagged by any user. 
- **Low Confidence**: Examine plots with low plot confidence.
- **User:** Examine plots collected by any user. A dropdown menu allows you to choose which user.
- **QA/QC:** Examine plots where the collected answers have more than a specified level of disagreement. You can also click the **View Disagreements** button to examine user’s responses side by side in a separate window. See the Institution and Project Creation manual for more information.

.. thumbnail:: ../_images/preparing8.png
   :title: Navigation options for Institution administrators.
   :align: center
   :width: 60%

- Under this dropdown menu is the **Plot ID number**.
- The navigation menu contains blue **forward** and **backward** buttons to navigate to different plots, as well as a text box where you can enter a plot ID number and then click **[Go to plot]** to navigate to a specific plot.

**External Tools options:**

- Click **[Re-Zoom]** to return your focus to the focus plot
- **Click [Geodash]** to open the **GeoDash** pane with additional information about the plot (detail see :doc:`start`).
- You can click **[Download Plot KML]** to download a KML file with the plot information. . Downloading the KML allows you to transfer the plot information to another program, such as Google Earth Desktop. Importantly, the KML functionality allows users to determine the coordinates (latitude and longitude) at which points of interest are located.

 .. thumbnail:: ../_images/preparing9.png
    :title: External tools option.
    :width: 60%
    :align: center

- The **Go to GEE Script** button may or may not be present on your dashboard. If it is present, it will take you to an Earth Engine Apps website displaying additional data about the plot.

  - This screen will have 6 panels. On the far left, there is a Sentinel 2 composite of the last 12 months. They are colored as infrared color composite (near infrared, mid infrared, red). Reddish brown is forest, agriculture, grass, and shrubs are a lighter shade of orange. Water is purple, and urban areas are shades of blue and green.
  - In the center are Landsat 8 and Landsat 7 Color Yearly mosaics, with a slider so you can choose between years.
  - On the right are NDVI graphs of the plot from MODIS, Landsat 7/8, and Sentinel 2. For the Landsat 7/8 and Sentinel graphs, you can click a point on the graphs to load specific images in the left and center panels.

**Imagery Options**

- Using the dropdown under **Imagery Options**, you can change the background image by selecting between different imagery on the drop-down list.

.. thumbnail:: ../_images/preparing10.png
   :title: Imagery options drop down menu.
   :width: 60%
   :align: center

- Different images are helpful for comparing different points in time and/or where one imagery source does not have enough detail to answer the **Survey Questions**. Some imagery options also include the names of towns, villages, etc.
- You may need to click **[Update Imagery]** to update the imagery when you select a new imagery source.

.. note::
   
   Some imagery servers are slow. Please be patient when switching to sources like Planet Daily, since their servers can take about 30 seconds to respond to queries sent by the CEO platform.

**Survey Questions**

- This is the area to answer the project’s **Survey Questions**.

.. thumbnail:: ../_images/preparing11.png
  :title: The panel to answer survey questions.
  :width: 60%
  :align: center

- Each project has a different set of numbered survey questions (in the example below only “1” question is in the project).
- You can navigate between questions using the forward and back arrows or the numbers.
- The **Unanswered Color** radio button changes the color of the survey points.
- Your project may have a **confidence slider**.
- The **Save** button will save your survey answers and move on to the next point (it only becomes active when all points have been interpreted).
- **Flag Plot** is used when a survey question cannot be answered, either because the imagery is not of high enough quality or there is another problem; this will advance to the next plot. When you flag a plot, a text box will appear so that you can type in why you flagged the plot. For example, you might write “Cloud” if there is a cloud in the imagery over the plot.
- **Clear All** erases all your survey question answers for this plot.
- **Quit** will return you to CEO’s **Home** page. If you try to leave the page without saving your answers, you will receive a warning and reminder to save your answers if appropriate.

**Survey questions with user-drawn samples**

- Your project may have been set up to allow for user drawn samples.
- If so, you will see two icons under **Survey Questions**, a question mark and a pencil.
- When you have the question mark selected, the Survey Question interface will work as we just discussed.

.. thumbnail:: ../_images/preparing12.png
   :title: Survey question pane with the option of user-drawn samples.
   :width: 60%
   :align: center

- However, if you select the pencil icon, you will see the options that allow you to draw different points, lines, and polygons on the map.

.. thumbnail:: ../_images/preparing13.png
   :title: Adding user-drawn samples.
   :width: 60%
   :align: center

- You can switch between the different shapes by clicking on their respective icons. Note that your project administrator may have restricted the types of geometries (point, line, polygon) that you can create.

Geo-Dash
^^^^^^^^

The **GeoDash** pop-up window will also open with information about the plot if it has been configured for the project. This window contains information to help identify land cover and land use attributes compiled from Google Earth Engine. Depending on the project, Geo-Dash can include plots of time series data (such as how NDVI values have varied over time), Landsat image chips, and more. See :doc:`start` for more information.
