# Food Origins

We're making the global food supply chain tangible.

## How?

By creating a tool to help people understand the global supply chain and how it affects them as they shop at their local supermarket. It's an app in which users can take a photo of the barcode on a food product and immediately see the countries from which the ingredients were imported.

## Why?

It's easy to show someone a huge set of import and export data, but it's hard for people to translate that into a real understanding of the global food supply network. We want to empower users to discover this for themselves by giving them a tool to visualise the country of origin of each ingredient in the product that they're holding in their hand.

## Tech

We used import/export datasets from the USDA's Foreign Agriculture Service (http://www.fas.usda.gov/data) to figure out which country the ingredients in your food come from. We also used LableAPI (http://developer.foodessentials.com/) to discover ingredients given a barcode. Finally, we used python's pandas library extensively for data munging, the web.py module to run our app, the Folium mapping library to map the data and IBM's Bluemix to deploy the app.
