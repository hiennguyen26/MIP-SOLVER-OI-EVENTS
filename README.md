# OiEvents Operations Optimization Machine

**Introduction:**
The events industry produces 600,000 tons of waste every year, excluding food waste. What if there was a marketplace for event organizers to rent used event materials (bamboo, aluminum, decorative pieces, artworks, etc.) to stop waste production? Oi Events is positioned to be at that frontier and help alleviate the landfill crisis. 


To best serve this cause, transparency for C02 emissions and logistical costs by transports worldwide to meet event demands must be tracked. To minimize both of these costs, the rules of storage must be applied to increase the company's efficiency over time. A Mixed-Integer Programming model calculates the packing and transport steps needed to satisfy all event demands. This MIP model can be considered as the foundation for a perpetual operations research machine finding solutions that currently minimize waste, pollution, and operational costs, but also can be further developed to maximize profitability and ensure a high refusal rate for each event component in the system. 


Today, MIP is used commercially to optimize scheduling for production, goods transfers and many other business and governmental purposes, mainly for more efficient allocation of resources.


**Code Specifications:**
1. The MIP model takes in a manually simulated world of 27 global cities with different storage settings and event demands. 
2. The MIP optimize shipping events materials and components that are based on Oi Creative Agency's Pavilions Project to satisfy said demands (shorturl.at/ftFLV)
3. Eucaledian distance is calculated to find carbon emissions rate with different types of transports which includes: freight and truck. 
4. The model generates a cti (CreateTransportIter) as an optimized step to ship containers of materials from one place to another to satisfy event demands. 
5. Run solver.py to start operations research. 

**Notes:**
1. Currently the model can only optimze operations decisions over a span of 1 year calendar of concurrent events around the world. 
2. It currently takes about 3 weeks to run the simulation to do operations research over 5 year.
3. Commercial MIP model multithread proivders such as Guirobi have been contacted but the price for service is more than $7,000 a year.
