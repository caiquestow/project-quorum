# 1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

I chose to use a simpler approach, avoiding the use of a database and utilizing resources already present in Python. Speaking of technology, I chose Python and Django for being versatile tools, with an active community and with which I have been more familiar with in recent projects. I prioritized a more modular development, which was easy to visualize and understand for future maintenance and features. I would consider using a database in case the application scales up so that it can use more resources, for example real-time changes and larger volumes of data without compromising performance. 
We can improve the application by applying a docker image, makefile, separate the frontend from the backend and use some cloud. These are my first suggestions.

# 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or“Co-Sponsors”?

For the inclusion of new columns, I would need to modify the existing processing functions to read the new information from the CSV files, and I would also need to update the templates to display this new information. If new data cross-referencing is necessary to present the new results, new processing functions could be created so that the existing ones do not become too complex to maintain and also avoid performance issues.

# 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

It depends a bit on the type of data input. The system is prepared to recognize CSV, one way would be to convert these inputs to CSV following the existing models, and from there the system would already be functional. If it is an API, the processing functions could be modified to interpret JSON instead of CSV.

# 4. How long did you spend working on the assignment?

I spent about 5 hours on it, as I didn't have a base project, I ended up using some extra time to structure one with some documentation features. I also started using Docker, but I was unsure how the person who would run it would do it and ended up returning to an execution via runserver.
