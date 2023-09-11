Built-in & Adding Imagery Sources
=================================

There are two main ways to add background, or basemap imagery to your Institution for use in your Projects. First, CEO includes a handful of built-in imagery options, including imagery from MapBox, Planet NICFI Public, and Sentinel. Second, CEO allows users to connect their own imagery from many different sources, including Google Earth Engine, Bing Maps, XYZ tiles, WMS and more.

Built-in base imagery sources
-----------------------------

There are a handful of built-in imagery options in CEO. Each of these options has different strengths and limitations.

Mapbox
++++++

MapBox is an open-source mapping platform for custom designed maps. The satellite imagery uses different sources based on the zoom level and
geographic availability. According to Mapbox's documentation:

- Zoom levels 0–8 use de-clouded data from NASA MODIS satellites.
- Zoom levels 9–12 use Maxar satellite imagery along with NASA/USGS Landsat 5 & 7 imagery in limited locations.
- Zoom levels 13+ use a combination of open and proprietary sources, including Maxar's Vivid product for most of the world, Nearmap aerial imagery over US cities, and open aerial imagery from Denmark, France, Germany and other regions.

More information can be found `in Mapbox's documentation https://docs.mapbox.com/data/tilesets/reference/mapbox-satellite/`__.

MapBox Satellite and Mapbox Satellite w/Labels are thus composite satellite imagery, where each map tile may be stitched together from imagery acquired on multiple dates. There is not necessarily a single date for an imagery tile. This is the same as, for example, Google Maps and Bing Aerial Imagery.

CEO uses Mapbox's satellite layer as well as one with place and landmark labels.

.. note::
     Maxar has eliminated multiple data products that were previously available on CEO, including: DigitalGlobeRecentIMagery; DigitalGlobeRecentImagery+Streets; DigitalGlobeWMSImagery; and EarthWatch.

Planet NICFI Public
+++++++++++++++++++

Planet NICFI Public is imagery available through a partnership between Norway's Ministry of Climate and Environment, specifically Norway's International Climate and Forest Initiative (NICFI) and Planet. Along with other partners, they have made high-resolution (sub 5 m pixel) imagery available in the tropics. These maps are available on a biannual basis between December 2015 and August 2020 and on a monthly basis after September 2020.

More information can be found here:
https://www.planet.com/pulse/planet-ksat-and-airbus-awarded-first-ever-global-contract-to-combat-deforestation/.

Adding additional basemap imagery
---------------------------------

The built-in imagery is not sufficient as basemaps for some projects, including projects comparing land uses between two time periods, or projects that need imagery from specific dates or months. CEO allows institutions to add new imagery sources through their Institution page. This section discusses the different imagery types that can be added.

The instructions below assume you are starting on your Institution page >>(see directions in Part 2: A.2-4) and are logged in as an Administrator for your Institution.

Under the **Imagery** panel on the **Institution** page, click **[Add New Imagery]**. Under **Select** Type you will see multiple different options. Some, including WMS Imagery and XYZ Imagery, are protocols that can be applied broadly, while other options connect to specific data sources that you generally need to subscribe to.

For Bing Maps, Planet Monthly, Planet Daily, Planet NICFI, SecureWatch, and the MapBox products you will first need to locate your no-authentication API key. You will be asked to provide this key in the CEO imagery setup panel.

We will now talk about how to add imagery for each of these options.

WMS Imagery
+++++++++++

This option can be used to access data your Institution hosts or data services that use WMS or WTMS. Imagery must be accessible using WMS or WTMS. Images stored locally on a user's computer cannot be added to a CEO project, although they can be accessed if you upload them to a WMS or WTMS (as a basemap), or as a Google Earth Engine Asset (for Geo-Dash and/or basemap).

The information needed to set up the WMS server will differ based on the specific imagery you are.

1. The first step of preparing to connect to your WMS with CEO is checking that your WMS is compatible with CEO.

     i. CEO requests data in EPSG:3857. Your WMS server is responsible for reprojecting the imagery it hosts into this requested projection.

     ii. CEO requires the servers to use the https protocol.

2. Second, to connect your web map service (WMS) to CEO, you need to gather three pieces of information: the base URL for your WMS, the layer name that you want, and any parameters your WMS requires to serve imagery.

     i. **Title:** This will be the displayed name of the imagery.

     ii. **Attribution**: This is the displayed attribution for your imagery. It will appear at the top of the map while users perform
      data collection tasks.

     iii. **URL**: This should be the URL of your WMS/WTMS. It should be preceeded by https://

     iv. **Layer Name**: This is the layer name from your server that you want to display.

     v. **Params (as JSON object)**: If there are any parameters for the layer you want to specify, put them here as a JSON object. Documentation for the WMS getMapService is available online here: https://docs.geoserver.org/stable/en/user/services/wms/reference.html#getmap. These work only if they are parsed by the target WMS. Here are some examples::

          {"TILED": true}
          
          {"VERSION": "1.1.1", "CONNECTID":"63f634af-fc31-4d81-9505-b62b4701f8a9", "FEATUREPROFILE":"Accuracy_Profile", "COVERAGE_CQL_FILTER":"(acquisition_date>'2012-01-01')AND(acquisition_date<'2012-12-31')"}

.. note::
     
     Quotes **MUST BE** "" ASCII/neutral/vertical quotation marks. Using “” smart/typographic/curved quotation marks will cause errors. Use only Unicode U+0022 and U+0027.

     vi. If you need to proxy your imagery for your WMS, please check **Proxy Imagery**. You may need this option if you need to obfuscate a key for your WMS or WTMS.
     
     vii.  If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When
     Saving.**

3. When all fields are filled out, click on **[Add New Imagery]**.

If you are having trouble, we have posted an extensive how-to and troubleshooting guide on the CEO blog. You can view that guide here: >>https://collect.earth/blog/add-wms-to-ceo/.

XYZ Tiles
+++++++++

XYZ Tiles is a flexible way of adding imagery. Services you can now add includes any of the adaptations of Open Street Maps, Yandex, and any other service using XYZ.

1. **Title:** This will be the displayed name of the imagery.

2. **Attribution** for the XYZ Imagery. This will be shown to your users in the data collection pane.

3. Add the **XYZ URL**.

     i. By default, XYZ uses the widely-used Google grid, where (x,y) (0,0) are in the top left.

     ii. In general, it should have the format: <URL>?x={x}&y={y}&z={z} . For example, `https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z} <https://mt1.google.com/vt/lyrs=y&x=%7bx%7d&y=%7by%7d&z=%7bz%7d>`__

     iii. You can also use grids where (x,y) (0,0) are in the bottom left. To do so, you will need to use the following format: <URL>?x={x}&y={-y}&z={z}

.. note::
     Sometimes you will need to edit a provided URL to make it compatible with CEO. For example, the Open Street Map WIKI provides the following URL for the German version of Open Street Maps: `https://a.tile.openstreetmap.de/${z}/${x}/${y}.png <https://a.tile.openstreetmap.de/$%7bz%7d/$%7bx%7d/$%7by%7d.png>`__. As provided this will not work. To make it work, you will need to delete the “a.” subdomain and the “$” characters.
     
     The edited URL does work in CEO: `https://tile.openstreetmap.de/{z}/{x}/{y}.png <https://tile.openstreetmap.de/%7bz%7d/%7bx%7d/%7by%7d.png>`__

4. If you want to add this imagery source to all your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

5. When all fields are filled out, click on **[Add New Imagery]**.

Bing Maps
+++++++++

This imagery option allows you to add Bing Maps with your own API key. The Bing tile system uses the Mercator projection and has 23 levels of zoom (though not all levels are available in all locations). Commonly, the resolution at max zoom is about 0.3 m per pixel. For more information, see  https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system.

.. Note:: 
     *The imagery provided by Bing Maps is composite satellite imagery. This means that each map tile is stitched together from imagery acquired on multiple dates. There is not a single date for an imagery tile*. Some map tiles contain imagery collected over a  multi-day window while other tiles contain imagery collected over a multi-year window. As there is not a single date for an imagery tile, CEO cannot provide the exact date of the imagery used. If you're interested in learning more, the Bing Maps API can be found here:  https://docs.microsoft.com/en-us/bingmaps/rest-services/imagery/imagery-metadata.

1. **Title:** This will be the displayed name of the imagery.

2. **Imagery Id:** Only Aerial and AerialWithLabels are currently implemented. Note that the AerialWithLabels imagery uses the legacy static tile service, which is deprecated, and current data will not be refreshed. It therefore may have older imagery than the Bing Aerial dataset.

3. **Access Token:** Your BingMaps key. For more information or to obtain your own key, see https://docs.microsoft.com/en-us/bingmaps/getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key.

4. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

5.  When all fields are filled out, click on **[Add New Imagery]**.

+-----------------------------------------------------------------------+
| Directions for requesting a Bing maps key:                            |
|                                                                       |
| -  To use Bing Maps imagery for your projects, you can create your    |
|    own FREE Bing maps key to connect your institution's projects to   |
|    your Bing Maps account. The full directions for creating a key are |
|    here:                                                              |
|    https://docs.microsoft.com/en-us/bingm                             |
| aps/getting-started/bing-maps-dev-center-help/getting-a-bing-maps-key |
|                                                                       |
| -  Visit https://www.bingmapsportal.com/ to request a Bing key or     |
|    copy your existing key.                                            |
|                                                                       |
|    -  Sign in. You will need a Bing maps account or Microsoft account |
|       (https://docs.microsoft.com/en-us/bingmaps/ge                   |
| tting-started/bing-maps-dev-center-help/creating-a-bing-maps-account) |
|                                                                       |
|    -  Once you have logged in, click on **My account**, then click on |
|       **My Keys**                                                     |
|                                                                       |
|    -  If you already have a key, click **Show key** or **Copy key**   |
|                                                                       |
|    -  If you do not have a key, click on **Click here to create a new |
|       key**.                                                          |
|                                                                       |
|    -  Fill out the information. Application URL is optional (and I    |
|       might suggest not using it) but if you do, use                  |
|       https://collect.earth as your Application URL                   |
|                                                                       |
|    -  You will create a **Basic** key. If you need more imagery, you  |
|       will need to talk to Microsoft and request an **Enterprise      |
|       key** (https://www.microsoft.com/en-us/maps/                    |
|       create-a-bing-maps-key#enterprise)                              |
+-----------------------------------------------------------------------+

Planet Monthly
++++++++++++++

Planet offers multiple data products (product specification here: https://support.planet.com/hc/en-us/articles/360022233473-Planet-Imagery-Product-Specifications). This option pulls from the Planet Monthly mosaic product, which allows you to display imagery from a specific month. User help is available here: https://developers.planet.com/docs/apps/explorer/.

1. **Title:** This will be the displayed name of the imagery.

2. **Default Year**: The default year that will be displayed when the map loads.

3. **Default Month**: The default month that will be displayed when the map loads. Use integer format 1-12.

4. **Access Token**: Your Planet access token. This can be accessed through your My Account page on the Planet website.

5. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.** 

6. When all fields are filled out, click on **[Add New Imagery]**.

.. tip::
     Default Year & Default Month will let you put in any integer, positive or negative. The up and down arrow keys start at 0. Please type year in the YYYY format and month as an integer between 1-12.

PlanetDaily
+++++++++++

PlanetDaily is another imagery product available from Planet. It allows users to detect land use and land cover change in near real time. This data source allows you to select a start and end date, with up to daily imagery resolution. Your study area might not have full coverage every day.

1.  **Title:** This will be the displayed name of the imagery.

2. **Access Token:** Your PlanetDaily API key. This can be accessed through your My Account page on the Planet website.

3.  **Start Date:** Starting date for the imagery you are interested in; you can input the date using numeric keys or with the calendar widget on the right side.

4.   **End Date:** Ending date for the imagery you are interested in.

5.  If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

6. When all fields are filled out, click on **[Add New Imagery]**.

Planet NICFI
++++++++++++

This allows you to add your own Planet NICFI key, instead of using CEO's. 

.. note::
     
     You will need an account from the Planet NICFI program: https://www.planet.com/nicfi/. This is separate from your 'normal' Planet account.

1. **Title:** This will be the displayed name of the imagery.

2. **Access Token:** Your Planet NICFI API key. This can be accessed through your My Account page on the Planet website.

3. **Default Time:** Choose the default time period of imagery to display. Note that the time periods available from NICFI are actively being changed. THESE ARE SUBJECT TO CHANGE BASED ON PLANET AND NICFI's DECISIONS.

4. **Default Band**: Choice between Visible (RGB) and Infrared false color.

5.  If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

6. When all fields are filled out, click on **[Add New Imagery]**.

SecureWatch Imagery
+++++++++++++++++++

SecureWatch is a service from Maxar focused on monitoring for new land use/land cover changes and comparing current land use/land cover with over 20 years of historic images. For more information see: https://www.digitalglobe.com/products/securewatch.

>>https://gcs-docs.s3.amazonaws.com/Access/Miscellaneous/DevGuides/WMS/WMS_Map.htm?Highlight=key

1. **Title:** This will be the displayed name of the imagery.

2. **Connect ID:** This is your API key. You need to use a no-auth key here, which should be a string of letters and numbers separated by dashes.

3. **Start Date:** Starting date for the imagery you are interested in; you can input the date using numeric keys or with the calendar widget on the right side.

4. **End Date:** Ending date for the imagery you are interested in.

5.  If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

6. When all fields are filled out, click on **[Add New Imagery]**.

Sentinel 1 Imagery
++++++++++++++++++

Sentinel 1 information is only available from April 2014 to present (Sentinel 1A launch). Sentinel data is available in CEO through GEE. If multiple images are available for the region and dates selected, the median reducer is used to produce a single image.

1. **Title:** This will be the displayed name of the imagery.

2. **Default Year**: The default year that will be displayed when the map loads.

3. **Default Month**: The default month that will be displayed when the map loads. Use integer format 1-12.

4. **Band Combination**: Preset combinations of bands for most uses. VH and VV are single polarization, VH/VV and HH/HV are dual polarization. More info https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/acquisition-modes.

5. **Min:** Minimum value for bands that will get mapped to 0 for visualization. This can be one value for all bands, or a value for each of the three bands. This should be one number. Acceptable values for each band's minimum are the same as for Sentinel imagery available through GEE generally; see https://developers.google.com/earth-engine/datasets/catalog/sentinel\ *.* Min can be as low as -50, but 0 is frequently used.

6. **Max:** Maximum value for bands that will get mapped to 255 for visualization. This can be one value for all bands, or a value for each of the three bands. This should be one number. Acceptable values for each band's maximum are the same as for Sentinel imagery available through GEE generally. See link above. Max can be as high as 1, but .3 is frequently used.

7. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

8. When all fields are filled out, click on **[Add New Imagery]**.

Sentinel 2 Imagery
++++++++++++++++++

Sentinel 2 imagery is available from June 2015-present. Sentinel 2 imagery is displayed in CEO from GEE. If multiple images are available for the region and dates selected, the median reducer is used to produce a single image.

1.  **Title:** This will be the displayed name of the imagery.

2. **Default Year**: The default year that will be displayed when the map loads.

3. **Default Month**: The default month that will be displayed when the map loads. Use integer format 1-12.

4. **Band Combination**: Select one of the options available, including True Color, False Color Infrared, False Color Urban, Agriculture, Healthy Vegetation, and Short Wave Infrared.

     i. **True Color**: The True color band combination uses the red (B4), green (B3), and blue (B2) channels. Its purpose is to display imagery the same way our eyes see the world. Just like how we see, healthy vegetation is green, urban features often appear white and grey and water is a shade of dark blue depending on how clean it is.

     ii. **False Color**: The False-color infrared band combination is meant to emphasize healthy and unhealthy vegetation. By using the near-infrared (B8) band, it's especially good at reflecting chlorophyll. It is most commonly used to assess plant density and health, as plants reflect near-infrared and green light while absorbing red. Since they reflect more near-infrared than green, plant-covered land appears deep red. Denser plant growth is darker red. Cities and exposed ground are gray or tan, and water appears blue or black.

     iii. **False Color Urban**: The false color urban band combination uses SWIR (B12), near-infrared (B8), and blue (B2). This composite is used to visualize urbanized areas more clearly. Vegetation is visible in shades of green, while urbanized areas are represented by white, grey, or purple. Soils, sand, and minerals are shown in a variety of colors.

     iv. **Agriculture:** The agriculture band combination uses SWIR-1 (B11), near-infrared (B8), and blue (B2). It's mostly used to monitor the health of crops because of how it uses short-wave and near-infrared. Both these bands are particularly good at  highlighting dense vegetation that appears as dark green.

     v. **Healthy Vegetation:** Because near-infrared (which vegetation strongly reflects) and red light (which vegetation absorbs), the vegetation index is good for quantifying the amount of vegetation. The formula for the normalized difference vegetation index is (B8-B4)/(B8+B4). While high values suggest dense canopy, low or negative values indicate urban and water features.

     vi. **Short-wave Infrared:** The short-wave infrared band combination uses SWIR (B12), NIR (B8A), and red (B4). This can help to estimate how much water is present in plants and soil, as water reflects SWIR wavelengths. Shortwave-infrared bands are also useful for distinguishing between cloud types (water clouds versus ice clouds), snow and ice, all of which appear white in visible light.

5. **Min:** Minimum value for bands that will get mapped to 0 for visualization. This can be one value for all bands, or a value for each of the three bands. This should be a single number. Acceptable values for each band's minimum are the same as for Sentinel imagery available through GEE generally; see https://developers.google.com/earth-engine/datasets/catalog/sentinel For example, 0 could be used.

6. **Max:** Maximum value for bands that will get mapped to 255 for visualization. This should be a single number. Acceptable values for each band's maximum are the same as for Sentinel imagery available through GEE generally. See link above. For example, values of 2800-4000 are frequently used.

7. **Cloud Score**: Allowable cloud cover. Values can be 0-100.

8. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

9. When all fields are filled out, click on **[Add New Imagery]**.

GEE Image Asset
+++++++++++++++

Google Earth Engine (GEE) Assets include user's uploaded assets along with assets provided by other users and GEE. Information on Assets can be found here: https://developers.google.com/earth-engine/guides/asset_manager. More detail on uploading your own assets is below. Note that Image Asset refers to a single image (e.g. a GeoTIFF layer) while ImageCollection Asset refers to a stack of images (e.g. GeoTiff layers of the same location over different dates).

1. **Title:** This will be the displayed name of the imagery.

2. **Asset ID:** The Asset ID for your image asset. Will have a format similar to: USDA/NAIP/DOQQ/n_4207309_se_18_1_20090525

3. **Visualization Parameters (JSON format)**: Any visualization parameters for your layer. For example, {"bands":["R","G","B"],"min":90,"max":210}

4. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

5. When all fields are filled out, click on **[Add New Imagery]**.

We have created an extensive how-to and troubleshooting guide for adding GEE Image Assets and Image Collection Assets to CEO. It is available in CEO's blog here: >>https://collect.earth/connecting-gee-raster-data/. Additionally, we have directions for uploading your own image assets to >>GEE in the following section.

GEE ImageCollection Asset
+++++++++++++++++++++++++

Google Earth Engine (GEE) Assets include user's uploaded assets along with assets provided by other users and GEE. Information on Assets can be found here: https://developers.google.com/earth-engine/guides/asset_manager. More detail on uploading your own assets is below. Note that Image Asset refers to a single image (e.g. a GeoTIFF layer) while ImageCollection Asset refers to a stack of images (e.g. GeoTiff layers of the same location over different dates).

1. **Title:** This will be the displayed name of the imagery.

2. **Asset ID:** The Asset ID for your image asset. Will have a format similar to: LANDSAT/LC08/C01/T1_SR

3. **Start Date**: The default start date of imagery to display.

4. **End Date**: The default end date of imagery to display.

5. **Visualization Parameters (JSON format)**: Any visualization parameters for your layer. For example, {"bands":["B4","B3","B2"],"min":0,"max":2000}

6.  If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

7. When all fields are filled out, click on **[Add New Imagery]**.

.. note::
     To display the GEEImageCollection, CEO uses the 'mean' reducer in Earth Engine. This takes the mean of any images in the image collection during the time period specified.

We have created an extensive how-to and troubleshooting guide for adding GEE Image Assets and Image Collection Assets to CEO. It is available in CEO's blog here: >>https://collect.earth/connecting-gee-raster-data/.

+-----------------------------------------------------------------------+
| Uploading GeoTIFF images to GEE:                                      |
|                                                                       |
| -  Visit https://code.earthengine.google.com/                         |
|                                                                       |
| -  Navigate to **Assets**                                             |
|                                                                       |
| -  Click **New**, then under **Image Upload** click **GeoTIFF**.      |
|                                                                       |
| -  A new window will pop up. Click **Select** and navigate to the     |
|    GeoTIFF asset.                                                     |
|                                                                       |
| -  Alter the **Asset ID** name if you would like.                     |
|                                                                       |
| -  Check the default settings, e.g. if your data has a start/end time |
|    then add those.                                                    |
|                                                                       |
| -  Click **Upload.**                                                  |
|                                                                       |
| -  Wait for your asset to upload. When it does, click on the asset    |
|    name and a new window will pop up.                                 |
|                                                                       |
| -  Next to ImageID there are two interlocking squares.                |
|                                                                       |
| -  Click on this to copy your ImageID to the clipboard (you'll need   |
|    this to connect to CEO).                                           |
|                                                                       |
|    a. You can also click on the “Bands” tab to get more information   |
|       about your image. This is very useful for specifying your       |
|       visualization parameters in CEO.                                |
|                                                                       |
|    b. Can also add gamma etc. information, see                        |
|                                                                       |
| https://developers.google.com/earth-engine/guides/image_visualization |
+-----------------------------------------------------------------------+

MapBox Raster
+++++++++++++

MapBox Raster serves raster tiles including Mapbox Satellite. For more information see: https://docs.mapbox.com/help/glossary/raster-tiles-api/.

1. **Title:** This will be the displayed name of the imagery.

2. **Layer Name** is the desired layer name from MapBox.

3. **Access Token** will be your no-auth key from MapBox. For more information, see https://docs.mapbox.com/help/glossary/raster-tiles-api/.

4. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

5.  When all fields are filled out, click on **[Add New Imagery]**.

MapBox Static
+++++++++++++

Mapbox Static serves raster tiles generated from a `Mapbox GL <https://docs.mapbox.com/help/glossary/mapbox-gl/>`__-based style. This API has additional parameters that can be used to refine the results of a request. More information see: https://docs.mapbox.com/help/glossary/static-tiles-api/

1.  **Title:** This will be the displayed name of the imagery.

2. **User Name** will be your MapBox user name.

3. **Map Style ID** will be the id from MapBox.

4. **Access Token** will be your MapBox no-auth key. For more information see https://docs.mapbox.com/help/glossary/static-tiles-api/.

5.  If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

6. When all fields are filled out, click on **[Add New Imagery]**.

Open Street Maps
++++++++++++++++

Open streets Maps is an open source mapping product. This provides Open Street Map's Standard Tile Layer >>(Standard tile layer - OpenStreetMap Wiki). This product is useful for orienting users, since it has street and place names.

1. **Title:** This will be the displayed name of the imagery.

2. If you want to add this imagery source to all of your institution's projects, check the box next to **Add Imagery to All Projects When Saving.**

3.  When all fields are filled out, click on **[Add New Imagery]**.

Notes on imagery
----------------

For imagery options with dates, the dates you input are the default Dates that the imagery will be restricted to on the collection page. However, the user will be able to change these when exploring the map as there are start & end date widgets on the collection page sidebar (there are examples in the **Data Collection Manual**). For SecureWatch, the user will also be able to choose between FeatureProfiles. Without specifying a FeatureProfile, the most recent available imagery between the start and end dates displayed on the map.

SecureWatch and the Planet products will not return imagery if the map is zoomed out too much. This results in a white map canvas being displayed at the project overview level usually. Simply click the "Go to first plot" button on the Collection page to zoom in to the plot level, and then the imagery should appear.

For SecureWatch, the date shown when data is collected will be added to the project .csv data available for download >>(See Part 7: E “Download your data”).

Adding imagery from multiple time periods
-----------------------------------------

Adding multiple imagery options with different default time periods can make data collection easier for projects that compare two or more time periods to detect land use and land cover change. WMS/WMTS that you can use to create basemaps from different time points include GeoServer, Planet Monthly, Planet Daily, Secure Watch, Bing Maps, Mapbox Raster, and Mapbox Static.

GeoServer
+++++++++

For GeoServer, how to add different years of imagery depends on your server.

If your different years are stored as different layers, alter the GeoServer Layer Name field when you add the second layer. Make sure your title/attribution/etc. fields are accurate for the new layer.

If your server uses filtering to display imagery from different years you will need to alter the GeoServerParams field (again, making sure the information in your other fields is correct).

Once you have decided the best approach for your server, repeat the steps in >>Part 3 B.1 above for each time period you would like to add.

.. note::

     Some years may not contain any imagery, due to the sparseness of the data within the database. If no imagery for the selected time range appears, you will need to change your GeoServerParams field, possibly to change the feature profile or date ranges.

Planet Monthly, Planet Daily, and Planet NICFI
++++++++++++++++++++++++++++++++++++++++++++++

For all Planet products, you simply need to change the time period fields to add layers with different default time periods. Users will be able to change the time period displayed during data collection; however, this is the default that will be shown first.

.. tip::
     
     Be sure to change the Title field to reflect the correct default Year, Month, and Day for each new layer that you add.

Secure Watch
++++++++++++

For this Maxar product, you simply need to change the time period fields to add layers with different default time periods. Users will be able to change the time period displayed during data collection; however, this is the default that will be shown first.

.. top:: 
     
     Be sure to change the Title field to reflect the correct default Year, Month, and Day for each new layer that you add.

Sentinel 1 & 2
++++++++++++++

Users will be able to change the default Year and Month during data collection. However, additional layers with different default years and months can be added based on user preference.

.. tip::
     
     Be sure to change the Title field to reflect the correct default Year, Month, and Day for each new layer that you add.

GEE Image Asset
+++++++++++++++

Different Image Assets that cover different periods of time can be added using the Imagery interface. However, if you have multiple images of the same area over different periods of time, consider using CEO's GEE's ImageCollection functionality rather than multiple Image assets.

GEE ImageCollection Asset
+++++++++++++++++++++++++

Users will be able to change the default Year and Month during data collection. However, additional layers with different default years and months      can be added based on user preference.

.. tip::

     Be sure to change the Title field to reflect the correct default Year, Month, and Day for each new layer that you add.

Editing and deleting imagery
----------------------------

After you have added imagery you may need to change the default dates of the Visualization Parameters.

1. Navigate to your **Institution** page.

2. Next to the imagery you would like to edit, there is an editing hand button.

3. When you click on the editing hand button, it will take you back to the imagery creation form.

4. Edit the values as needed, using the information in this section as a guide.

5. Check the **Add Imagery to All Projects When Saving** box if you would like to add your imagery to all of the institution's projects.

6. When you are done, click **Save Imagery Changes**.

7. You can delete imagery by clicking the trash can icon next to the imagery name.

.. tip::
     
     There is currently no way to 'preview' what imagery will be visible in your new layer in the 'Add Imagery' workflow. There are two ways to work around this. 
     
     First, if your data source has a data viewing portal, you can use this to explore the imagery and determine what is available for the time periods you are interested in. 
     
     Second, you can add the imagery layer, then open an existing project from your institution. The imagery will be available in the dropdown menu (if you are switching between a project **Data Collection** window and an **Institution** window, you may need to refresh the project window to get    the new layer to appear). You can then check if the imagery is displaying correctly and go back to the **Institution** page to edit the imagery based on what you see.

Estimating imagery costs
------------------------

Before setting up a project in CEO, it is important to estimate how much imagery will be used for budgetary and resource allocation. Here is a quick guide to help.

When is imagery used? 
+++++++++++++++++++++

Imagery data is used whenever there is a map on the page. This means that on CEO, all these pages can use data:

* Home

* Data Collection

* Create Project

* Review Project

* Project Dashboard

* GeoDash (specific options or modules)

On these pages, when the map first loads, imagery data is used. Every time a user zooms or pans the map window, imagery is used. The largest amount of use will probably be with Data Collection.

Estimating imagery use for a project
++++++++++++++++++++++++++++++++++++

Each organization that provides imagery sets their own rules for how many tiles you can download per year given the kind of account that you have with them. Therefore, it is important to estimate this before setting up a project.

Additionally, services may “count” imagery against your quota differently. For example, Planet uses a rule “\ *Every Pixel is Charged Once*\ ” so you can download a pixel multiple times but it is only charged once >>(see here: You will also need to know this. https://support.planet.com/hc/en-us/articles/360021227554--When-is-a-Planet-product-charged-against-my-quota-). You will also need to know this.

To figure out how much imagery you are likely to use for a single project, count the number of plots. Then determine how many users will classify each plot. Next, try to factor in how often people will zoom or pan their maps for context when answering the survey questions for a plot. Multiply these numbers together.

Next, decide if you are using the Geo-Dash and ask yourself how many map widgets you will display on your Geo-Dash page. Multiply that number by the number of plots to get the amount of Geo-Dash imagery you will need. Keep in mind that Geo-Dash imagery counts against our annual limit for user memory/processing in GEE, whereas the usual global layers on CEO (Bing Maps, SecureWatch, Planet) have separate annual tile-based limits. For GEE, we recommend clipping and pre-processing the imagery to image assets or imageCollection assets for the collection area. This eliminates processing on-the-fly for each user that is collecting, as Geo-Dash can just grab the pre-processed image asset.

Finally, add a few extra tile downloads for loading the maps while creating and reviewing the project.

Once you have a sense of how many map images you will need for your project, you will then need to look up the tile counting policy for the imagery service that you are using. For example, some of them count 15 tiles as 1 unit of usage. Others use different counting rules.

.. tip::
     
     To reduce imagery use, consider setting your default background imagery to a cheaper source and only switching to more expensive paid imagery when you are at the correct zoom level.

Synthetic Aperture Radar (SAR) data in CEO for forest degradation
-----------------------------------------------------------------

Observations of backscatter variations over time in satellite SAR data can be attributed to structure and moisture. For forests, these can be linked to changes in the moisture conditions of the trees and soil as well as changes in forest structure. These are extremely useful for e.g. detecting forest degradation.

Color display of SAR data for detecting forest degradation is possible in CEO using Sentinel 1 data, WMS data, and GEE Image Assets and ImageCollection assets.

For information on detecting forest degradation through our GEE widget functionality, >>please see Part 4: E Project options.

For information on detecting forest degradation through our Geo-Dash widget, >>please see Part 6: I (Forest) Degradation tool.

For more information on SAR, please see:

1. Kellndorfer, Josef. “Using SAR Data for Mapping Deforestation and Forest Degradation.” SAR Handbook: Comprehensive Methodologies for Forest Monitoring and Biomass Estimation. Eds. Flores, A., Herndon, K., Thapa, R., Cherrington, E. NASA. 2019. DOI: .10.25966/68c9-gw82; available online at:  https://gis1.servirglobal.net/TrainingMaterials/SAR/Ch3-Content.pdf

2. >>https://www.servirglobal.net/Global/Articles/Article/2674/sar-handbook-comprehensive-methodologies-for-forest-monitoring-and-biomass-estimation

3. This one page guide from SERVIR & SilvaCarbon: https://servirglobal.net/Portals/0/Documents/Articles/2019_SAR_Handbook/SAR_VegIndices_1page_new.pdf
