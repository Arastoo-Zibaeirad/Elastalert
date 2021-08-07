In this project, I modified an open-source application, Elastalert., which is a simple framework for alerting.
Before Elastalert project, which is written by Yelp, it supported only DSL query. After I modified the code, it supports EQL(Event Query Language) and KQL(Kibana Query Language), which are only supported by Elasticsearch. By EQL, we are able to match sequence of events and by KQL we are able to match key-value events. Since all of detection rules are written with these two query languages, it is beneficial for Elastalert to support them.
