Troubleshooting
===============

Analysis troubleshooting
------------------------

1. If you try to access a project and receive an error message saying you do not have permission (as below), access to the project is limited to institution members. You will need to join your Institution, see :doc:`preparing`.

.. thumbnail:: ../_images/trouble1.png
   :title: Encountering a permissions error in CEO.
   :width: 80%
   :align: center

2. If you are on a **project’s homepage** and click on a plot and get an error window (e.g. if the plot is not found or if that plot has already been classified), after you click through the error there will be no plots on the map. You can either click on Go To Plot and have the first plot for analysis show up or reload the page to get all the survey plots back.
3. While collecting data, if you try to return to a previous plot you analyzed to review it and receive an error message, make sure you have the **Navigate Through** dropdown set to **My Analyzed Plots.**
4. If the background is completely black, the imagery resolution might be too low for the automatically set zoom level. Alternatively, the plot might be in a large waterbody. Zoom out until you see some more map context to confirm whether the issue is imagery resolution or a waterbody.
5. If the background of a new plot is grey, green, brown, or any solid color, the imagery resolution is too low for the automatically set zoom level. Zoom out a bit to display the imagery.
6. If the background of a new plot is white, the currently selected imagery does not exist for the current plot. Choose a different imagery.

Advanced troubleshooting
------------------------

**Interpreting time period represented by Map Box, Bing Maps and other dateless sources:**

Map tiles provided by these sources are created from multiple different satellite images captured over multiple days, months, or years. This means that the image does not represent a specific point in time. For this reason, CEO does not display one date for these imagery sources.

**Browser cache clearing:**

- You may get the message “This plot has already been analyzed” in error when you know that the plot has not been analyzed (e.g. it is a new project).
- If this happens, try clearing your browser cache. Instructions will change based on your browser.

  - For Chrome: https://support.google.com/accounts/answer/32050?co=GENIE.Platform%3DDesktop&hl=en
  - For Firefox: https://support.mozilla.org/en-US/kb/how-clear-firefox-cache
  - For Edge: https://support.microsoft.com/en-us/help/10607/microsoft-edge-view-delete-browser-history

**Image cache clearing:**

- Clear the local storage from the browser console line to remove the cache.
- You can do that by opening the browsers console and running: **localStorage.clear()**

**Geo-Dash is opening in the same tab when opening a new plot:**

- This is usually caused if you are copy and pasting URLs in your browser, and you cut and paste a new link into the ‘Geo-Dash’ tab. This tab is labeled by the browser as the Geo-Dash tab, so when you go to the new tab, CEO tells your browser to put the new plot’s Geo-Dash in the Geo-Dash tab.
- If you copy your CEO URL (e.g., for the collection page) into the "_geodash" tab, then when you try to visit a new plot, CEO will disappear and the Geo-Dash widgets will be displayed in that same tab. CEO uses a named "_geodash" tab to keep the Geo-Dash widgets in one place. Otherwise, they would spawn a new tab for every single plot that you visit.
- All you need to do to avoid this situation is to not copy your CEO URLs into an open Geo-Dash tab.

Report an issue and request new features
----------------------------------------

There are multiple ways to get in touch with us if you are still having an issue or would like to request a new feature.

1. Email `the CEO team <support@collect.earth>`__! We will respond to your email as soon as possible. Please provide as much detail as possible about the issue you are experiencing or the feature you would like to request.
2. You can ask questions on the OpenForis forum, which is available at `<http://www.openforis.org/support>`__. Please tag your question with **collectearthonline**. This is a great way to get help from the community and other users. You can also search for existing questions and answers that may help you.
3. You can also visit our GitHub issues page at `<https://github.com/openforis/collect-earth-online/issues>`__. Please include the steps you took to reproduce the issue, and any screenshots or error messages that may help us understand the problem. If you are requesting a new feature, please provide as much detail as possible about what you would like to see.