Geo-Dash Implementation
=======================

The **Geo-Dash** is a dashboard that opens in a second window when users begin to analyze sample plots. Geo-Dash provides users with additional information to help them interpret the imagery and better classify sample points and plots. The Geo-Dash tab can be customized to show information such as an NDVI time series, additional imagery, and a forest degradation widget.

You can configure your **Geo-Dash** by clicking on **[Configure Geo-Dash]** from the **Project Information/ Review Project** page.

This will bring up the **Geo-Dash layout screen**, with four options in the upper right corner of the screen.

.. figure:: ../_images/geodash1.png
    :alt: The Geo-Dash layout screen options
    :align: center
    :width: 50%

Clicking on **[Copy Layout]** will allow you to copy the Geo-Dash from another project. 

.. warning::
   This will delete any existing Geo-Dash you have associated with the project!

.. figure:: ../_images/geodash2.png
    :alt: Copy a different project's widget layout
    :align: center
    :width: 50%

You can add individual Geo-Dash widgets by clicking **[Add Widget].** To find out what each of the widgets do, click on **[Geo-Dash Help]** to open the **Geo-Dash Help Center**. We will also discuss this functionality below.

CEO uses Google Earth Engine to process many of the Geo-Dash widgets. Therefore, the information about Image Visualization for GEE is also useful here, specifically the min and max descriptions: https://developers.google.com/earth-engine/image_visualization.

Common Indices and Data Sources
-------------------------------

Some of the widgets provide access to common indices and data sources. These include NDVI, EVI, EVI2, NDMI, and NDWI, along with Landsat and Sentinel imagery. NDVI, EVI, EVI 2, NDMI, and NDWI indices are available in both image overlays and time series graphs.

The normalized difference vegetation index (NDVI) is used to determine if the cell contains live green vegetation. In map based representations, dead plants and inanimate objects are represented as red, while live healthy plants are represented as green. In numerical representations (e.g. time series graphs), values below 0 represent dead plants or inanimate objects, 0-0.33 represents unhealthy plants, 0.33-0.66 represents moderately healthy plants, and 0.66-1 represents very healthy plants. For more information, see e.g. https://www.usgs.gov/land-resources/nli/landsat/landsat-normalized-difference-vegetation-index

The enhanced vegetation index (EVI) and two-band EVI (EVI 2) are optimized vegetation indexs. They are designed to have higher sensitivity in high biomass regions e.g. along the equator, correct for canopy background signals, and reduce atmospheric influence on index values. In doing so, these indices addresses some of the key limitations of NDVI, however EVI requires more data to calculate and therefore has its own limitations. EVI 2 is in development and can be calculated just from red and near infrared bands. As with NDVI, red is used to represent dead plants/inanimate objects and green to represent healthy plants. The index varies between 0-1, with 0 representing dead plants and 1 representing very healthy plants. For more information on EVI see e.g. https://www.usgs.gov/land-resources/nli/landsat/landsat-enhanced-vegetation-index.

The normalized difference moisture index (NDMI) is used to determine the water content of vegetation. NDMI can be used for drought monitoring and for determining fuel loads (combustibility) for wildfire hazard assessments. Values near -1 indicate plants with low moisture while values near 1 indicate plants with high moisture. More information on NDMI can be found at e.g. https://www.usgs.gov/land-resources/nli/landsat/normalized-difference-moisture-index.

The normalized difference water index (NDWI) is also related to plant water content and plant water stress. It can be used to map water bodies, determine crop health and for wildfire risk analysis. Values near -1 indicate low water content and vegetation cover and values near 1 indicate high water content and vegetation cover. More information on NDWI can be found at e.g. https://edo.jrc.ec.europa.eu/documents/factsheets/factsheet_ndwi.pdf.

Data from Landsat satellites 5, 7, 8 and Sentinel 2 are also available. For more information about these datasets, see: Landsat: https://www.usgs.gov/land-resources/nli/landsat and Sentinel 2: https://sentinel.esa.int/web/sentinel/missions/sentinel-2. When more than one image is available for the date range selected for Landsat, the simpleComposite function in GEE is used to create simple cloud-free composite. It uses the median of the least cloudy pixels. Sentinel 2 data is also reduced using the median of least cloudy pixels.

Widget Formatting Hints
-----------------------

- Titles cannot contain special characters.
- Image parameters use JSON. Quotes used for image parameters in widgets should be vertical, not curly quotes. There should be no spaces in the image parameters.
- Lists can be formatted either as :code:`"1,2,3"` or as :code:`[1,2,3]` for numbers and :code:`"B3,B2,B1"` or :code:`["B3","B2","B1"]` for bands.
- When displaying three bands (e.g. B3, B2, B1 in RGB), Google Earth Engine and therefore the Geo-Dash can use either one or three values for min and max.
- For the Date Ranges, if the end date is longer than the period of record, only the available data will be displayed.

Move & Resize Widgets
---------------------

1. Widgets can be manipulated on the Geo-Dash Widget Layout Editor in the following ways:

   - Drag and drop to change widget position.
   - Resize by dragging from the bottom right corner.
   - Widgets will autotomatically align to a grid.

2. In the Geo-Dash collection page view, widget positions are are updated in real time.

.. figure:: /_images/change_widget_layout.gif
   :align: center

Duplicate, Edit, and Delete Widgets
-----------------------------------

1. You can copy a widget once it has been created by clicking on the **[duplicate icon]** in the upper right hand corner of the widget.
2. You can edit widgets once they are created by clicking on the **[pencil icon]** in the upper right hand corner of the widget.
3. To delete a widget, click on the trashcan in the upper right-hand corner of the widget.

.. figure:: ../_images/geodash3.png
    :alt: Duplicate, edit, or delete a widget.
    :align: center
    :width: 50%