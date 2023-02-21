# EMS Product Requirements

<https://sheauhei.atlassian.net/wiki/spaces/~5b8fba767c4eab2c31e2c839/pages/66158593/EMS+Product+Requirements>

* * *

# Product Vision

*   We provide an Energy Management System (EMS) based on VPP technology that solves the problem of inefficient energy use and high electricity costs for commercial, industrial, and residential customers. Our solution optimizes the use of energy resources, including the power grid, solar and wind plants, and microgrids, to meet customer demand while reducing costs and maximizing the Renewable Energy (RE) percentage.
    
*   Our solution offers economic benefits to the user by optimizing energy resource operation, including ESS charging/discharging, dynamic load management of EV chargers, and real-time monitoring and reporting of energy usage. By using our website and mobile app, customers can access detailed information on their energy usage, including real-time and historical data, customizable dashboards, and selectable optimization goals.
    
*   We offer benefits to investors who invest in energy resources, including increased profitability through optimized energy resource operation and the fulfillment of Renewable Portfolio Standards (RPS) requirements. Our solution also offers a flexible and scalable platform with APIs and other integration points to extend the functionality of the service, providing the potential for new revenue streams and business opportunities.
    

# Introduction

The Energy Management System (EMS) is a platform that manages the energy resources of a power system to improve the overall efficiency and reliability of the system. The EMS based on Virtual Power Plant (VPP) technology is designed to manage multiple types of energy resources, including the power grid, solar and wind plants, and microgrids on the user side.

The EMS service is responsible for optimizing energy resources, balancing supply and demand, and ensuring the stability and security of the power system. By managing these energy resources, the EMS can help to reduce overall energy costs, increase the use of renewable energy sources, and improve the resiliency of the power system.

The VPP technology used in the EMS service allows the system to aggregate and manage energy resources from multiple locations, including homes, businesses, and utility-scale power plants. This enables the EMS to optimize the use of energy resources across the power system, maximizing overall efficiency and cost-effectiveness.

By integrating renewable energy sources such as solar and wind power into the EMS, the system can reduce greenhouse gas emissions and help to meet renewable energy (RE100) targets. The EMS can also enable the integration of energy storage systems to improve the efficiency of the power system.

Overall, the EMS is a powerful tool for optimizing energy resources and improving the efficiency and reliability of power systems, while also supporting the transition to a more sustainable and resilient energy future.

# User Requirements

The EMS service is designed to meet the needs of a diverse customer base, including commercial, industrial, and residential customers. These customers require a range of features and capabilities to manage their energy resources effectively, and the EMS service has been developed to meet these needs.

One of the primary requirements of the EMS is the ability to manage a variety of energy resources, including the power grid, solar and wind plants, and microgrids on the user side. The EMS is designed to integrate with these resources and provide a unified platform for managing and optimizing energy usage.

In addition to managing energy resources, the EMS must be capable of performing a range of key functions, including microgrid economic optimization, fulfilling the required Renewable Energy (RE) percentage, load forecasting, solar plant forecasting, demand response dispatching forecasting, real-time monitoring and reporting, financial forecasting and investment analysis. These capabilities allow users to optimize energy usage and reduce costs, while also meeting regulatory requirements and reducing their carbon footprint.

To meet the needs of users, the EMS must also provide a high-quality user experience, including an intuitive dashboard display, selectable optimization goals, and the ability to monitor device health status and operation logs. The dashboard display should be mobile-friendly and provide a clear overview of energy usage and costs, while also allowing users to drill down into specific details as needed. The selectable optimization goals should allow users to set specific targets for energy usage, such as reducing costs or minimizing carbon footprint. Finally, the monitoring of device health status and operation logs is important for ensuring that the energy resources are functioning as intended and detecting potential issues before they become critical.

To ensure a seamless user experience, the EMS should also have a user interface that is easy to navigate and accessible from a range of devices. This requires a mobile-friendly design that is optimized for smartphones and tablets, as well as a role-based access control system that allows users to access the features and capabilities that are relevant to their role.

In summary, the EMS service based on VPP technology is designed to meet the needs of a diverse user base, including commercial, industrial, and residential customers. To meet these needs, the EMS must be capable of managing a range of energy resources, performing key functions such as economic optimization and load forecasting, and providing a high-quality user experience that includes an intuitive dashboard display and role-based access control.

# Technical Requirements

To fulfill the key features and capabilities required by the EMS, the following technical requirements need to be considered:

## Data Analytics

The EMS includes real-time data analytics to provide timely and accurate data on energy consumption and production, financial key performance indices, and dispatching management. Data analytics includes machine learning-based forecasting and optimization to improve the accuracy of the data and the efficiency of the EMS. The analytics supports the following capabilities:

*   Load forecasting
    
*   Solar plant forecasting
    
*   Demand response dispatching forecasting
    
*   Financial key performance index forecasting
    

The dispatching management function will help to prevent the customer's energy usage from exceeding the contract capacity of Taipower utility company.

## Forecasting and Dispatching Optimization

The EMS leverages machine learning-based forecasting and optimization to improve the accuracy of the data and the efficiency of the EMS. The algorithms used are adaptable to different scenarios and can scale as the number of users and microgrids increases. The following features are included:

*   The use of neural networks, decision trees, and clustering algorithms for different applications.
    
*   High accuracy, interpretability, and explainability of the models.
    

Regarding energy dispatching optimization, we use the omeof engine (Open Energy Modelling Framework) to model the energy network topology, and run the optimization tasks for the energy resources addressed in the topology, and the objective functions. The dispatching service is AWS-based.

### Local EMS Installed on User-side (Microgrid)

The local EMS is installed on the user-side microgrid, which communicates with the energy dispatching engine in the cloud to receive the scheduled dispatching tasks and execute them at the correct timing. The tasks may include ESS discharging, EV charger limiting, and more. By executing these tasks, the local EMS helps to optimize energy usage and reduce costs for the customer.

In addition, the local EMS ensures the stability and safety of the energy resources by monitoring the state of the microgrid and its energy resources. It can detect potential issues and take corrective actions to prevent equipment damage or outages. The local EMS also ensures that energy resources are dispatched according to the customer's needs and preferences and that the energy resources are used efficiently to maximize cost savings. By working in concert with the cloud-based energy dispatching engine, the local EMS optimizes energy usage and reduces costs while ensuring the stability and safety of the microgrid's energy resources.

### Data Retention Requirements

The EMS should retain data for historical analysis and regulatory compliance. The data retention period should be determined based on the regulatory requirements and the analysis needs of the EMS. The following requirements should be considered:

*   By default, all data should be retained as long as the user subscription is active.
    
*   By customer request, customer-specific data should be removed from the database.
    

### Service Level Agreement (SLA)

The EMS service level agreement should be defined to ensure a good customer relationship and satisfaction. The following SLA targets should be considered:

*   99% availability.
    
*   The expected response time for support tickets.
    
*   Expected uptime and availability targets.
    

### Customer Support

The EMS should provide 24/7 technical support to ensure that customer issues are addressed in a timely and efficient manner. The following support requirements should be considered:

*   Contracting a 3rd party customer support team to provide support to customers.
    
*   Offering support via email, phone calls, and the online ticket reporting system.
    
*   Integrating an NLP engine like ChatGPT to interpret customer problems and offer troubleshooting guidance.
    

These technical requirements should be considered when designing and developing the EMS to ensure that the system can meet the needs of the target customer demographic and fulfill the key features and capabilities required by the EMS.

# Security and Integration Requirements

1.  **Security Requirements:** The EMS service must comply with Taiwan's regulations and GDPR. User data must be encrypted during transmission through HTTPS, and access control must be implemented to ensure that only authorized users can access specific microgrids and data within the EMS service. A role-based access control system will be implemented, with username, password, and captcha identification to prevent credential stuffing.
    
2.  **Integration Requirements**: Currently, no integration with other systems or platforms such as billing or accounting software is required.
    
3.  **Scalability Requirements**: The EMS service must be scalable to handle a growing number of users and microgrids. The architecture should be designed to accommodate a large customer base.
    
4.  **User Authorization and Access Control**: The EMS service must have a role-based access control system, ensuring that only authorized users can access specific microgrids and data within the EMS service. It must also prevent credential stuffing.
    
5.  **Extensibility Requirements**: Currently, no specific requirements for extensibility are needed. However, providing APIs or other integration points for customers to extend the functionality of the EMS service may be considered in the future.
    
6.  **Data Retention Requirements**: The user's data should not be removed from our database as long as the subscription is active. By customer request, customer-specific data will be removed from the database. Historical data will be retained to support regulatory compliance and historical analysis.
    
7.  **Service Level Agreement (SLA)**: The EMS service must provide a high level of service availability with an expected uptime of at least 99%. The expected response times for support tickets and the specific targets for availability will be defined in the Service Level Agreement (SLA).
    
8.  **Customer Support:** The EMS service must provide 24/7 technical support to ensure customers can access help when needed. The support channel will include email, phone calls, and online ticket reporting. The service will also have a dedicated customer support team to help customers install the local EMS device, troubleshoot issues, and answer any questions related to the service. Video tutorials and webinars will also be available to assist customers in learning how to use the EMS service.
    

# Pricing and Subscription Models

In order to provide flexibility to customers, the EMS service will offer multiple pricing and subscription models. These models will include a one-time fee for installation and onboarding, a fixed monthly subscription fee, and an additional service fee based on usage or additional features.

The one-time fee for installation and onboarding will be a flat fee and will cover the cost of setting up the EMS service for the customer's specific needs. This fee will vary depending on the complexity of the installation and the number of energy resources being managed.

The fixed monthly subscription fee will be based on the number and types of energy resources being managed, as well as the level of service required by the customer. Customers will be able to choose from different service levels, each with a corresponding monthly fee.

In addition to the one-time and monthly fees, there will be an additional service fee for usage or for additional features. This fee will be based on the actual usage of the EMS service, such as the number of energy resources being managed or the level of data processing required. It may also be applied for additional features such as advanced analytics or reporting.

The pricing and subscription models will be designed to provide customers with flexibility and the ability to scale up or down as needed. Customers will be able to choose the pricing and subscription models that best fit their needs and budget.