Clevergrid : launch a jupyter server
---
We will run a jupyter notebook on a remote GPU server with the Clevergrid platform.

We have to remember some concepts in Clevergrid.

* All applications is stateless. That means no data is kept over the life of the application
* Add-ons are stateful. We will link a python runner application from Clevergrid to a Cellar add-on as storage
* We provide some environment variables as configuration


prerequisites
---
* You need a Clever-cloud or a Clevergrid account

* We will use the Clever CLI [Clever cloud CLI](https://www.clever-cloud.com/doc/clever-tools/getting_started/#installing-clever-tools)

Steps by steps jupyter setting up
----
1. Create an application from the [Clevergrid dashboard](https://dashboard.clevergrid.io/)
    * choose your organization
    * click on `Create an application`
    * set up a name and choose `Python Webapp`
    
    > We need a web application which stays up listening http requests
    
    * choose the needed instance size. One node is probably enough for a jupyter application

1. Set up your application environment variables
    * go to the  `Environment variables` tabs from your application dashboar
    * Make sure that your Webapp has `PORT` environment variable set at `8080`
    > this is the default listening port listening by Clevergrid
    * Provide a `BUCKET_NOTEBOOK_NAME` environment variable with the name you want give to your Cellar bucket
    * Set `PYTHON_VERSION` at `3.6`
    > We want use python3.6
    * Set the path to your starting script by setting up `CC_MLPYTHON_START_SCRIPT` environment variable to  `start.sh`
    * Make sure to click on `update changes`

1. Create a Cellar Add-on
    * Go to your [Clevergrid dashboard](https://dashboard.clevergrid.io/)
    * click on `add a storage service` and choose `Cellar S3 storage`
    * select a pricing and ink it to your application
    * name it
    > Linking to your application set up some specific environment variables for you

1. Go to this cloned git repository
    > We will now use the [Clever cloud CLI](https://www.clever-cloud.com/doc/clever-tools/getting_started/#installing-clever-tools)
    * make sure you are login to your Clevergrid account : `clever login`
    * link the repository to your application :
       * `clever link <Your App ID>`
       > You can find your App Id from the application overview tab from [Clevergrid dashboard](https://dashboard.clevergrid.io/)

1. Deploy your application
    * `clever deploy`

1. You have logs from the `clever deploy` command or from the overview application page on [Clevergrid dashboard](https://dashboard.clevergrid.io/)

    Find the token at the end of these logs and copy-paste it into your available jupyter application here :
    
       <App Id>.cleverapps.io
