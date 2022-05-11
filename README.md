# Influur
This repo is aimed to contain the project related to Influur Senior DS Technical Challenge

The challenge consisted in use data from an online retailer, that we want to use to solve some business questions. 

I developed an EDA of the main dataset, data preprocessing and understanding. 
Later I took two approaches to define a segmentation for our customers based on RFM (Recency, Frequency, Monetary), I also fitted a K Means approach based on RFM features so that I can distinguish different sets of customers to focus in an eventual marketing strategy. Segments we got through RFM approach could be a litle more interpretable. 
Finally I built some Buy 'Til You Die models in order to estimate the future amount of transactions for each customers and the probability to keep alive for the business. For this purpose, I used a Beta Geometric / Binomial Negative Distribution model, to capture the probabilistic nature of this non contractual churn risk.
Along the code I comment some of the main insights and assumptions to take into account for modeling part.
