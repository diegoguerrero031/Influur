# Influur
This repo is aimed to contain the project related to Influur Senior DS Technical Challenge

The challenge consisted in use data from an online retailer, that we want to use to solve some business questions. 

I developed an EDA of the main dataset, data preprocessing and understanding. 

Later I took two approaches to define a segmentation for our customers based on RFM (Recency, Frequency, Monetary), I also fitted a K Means approach based on RFM features so that I can distinguish different sets of customers to focus in an eventual marketing strategy. Segments we got through RFM approach could be a litle more interpretable. 

Finally I built some Buy 'Til You Die models in order to estimate the future amount of transactions for each customers and the probability to keep alive for the business. For this purpose, I used a Beta Geometric / Binomial Negative Distribution model (BG/BND), to capture the probabilistic nature of this non contractual churn risk.

Regarding to BG/BND model, we saw through implementation that concepts arising from RFM approach are the most important elements for the model as well as customer age or longevity. The results obtained through the model could be useful in the sense that we could oriented saome marketing efforts to those clients that are more likely to churn our business. We could think about to give them some kind of discounts or promotions so that we can reatin them for a little bit longer. We could use these information to make decisions related to orient marketing strategy.

Along the code I commented some of the main insights and assumptions to take into account for modeling part.

### The model built to estimate the probability to be alive for a given frequency, recency and customer age (T) could be used through the following processes:

#### Using in the cloud with GCP
In order to use the endpoint deployed in GCP, you should to send a POST request to the URL **https://influurtest-hackgnq7gq-uc.a.run.app/predict** with the following structure:

"{'frequency':30, 'recency':100, 'T':215}"

Here these made reference to the parameters for a given customer.

   - "frequency": Frequency for the customer.
   - "recency": Difference between the first and last purchase for a customer
   - "T": Customer age, it is the difference between the first purchase and the current date

#### Using a local environment
In order to use this method is needed to use Python 3.8.8 installed

**Install the requirements**
pip install -r requirements.txt

**Run the server in local**
uvicorn main:app --port 8080 --reload

**In order to make predictions**
Send a POST request to **http://localhost:8080/predict** with a JSON following the structure bellow:

"{'frequency':30, 'recency':100, 'T':215}"

Here these made reference to the parameters for a given customer.

   - "frequency": Frequency for the customer.
   - "recency": Difference between the first and last purchase for a customer
   - "T": Customer age, it is the difference between the first purchase and the current date

#### Possible responses examples
**Success**
{
    "code": 200,
    "status": "success",
    "data": {
        "prob_alive": "0.9999356018811655"
    }
}

**Failure**
{
    "code": 503,
    "message": {
        "INVALID REQUEST": "{'frequency':30, 'recency':100, 'wrong_variable':215}"
    }
}

As you can see in the failure example there is a wrong variable instead 'T' there is a 'wrong_variable'
