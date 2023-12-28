#https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs
#CQRS stands for Command and Query Responsibility Segregation, a pattern that separates read and update operations for a data store. 
#Implementing CQRS in your application can maximize its performance, scalability, and security. 
#The flexibility created by migrating to CQRS allows a system to better evolve over time and prevents update commands from causing merge conflicts at the domain level.


#https://martinfowler.com/bliki/CQRS.html
# At its heart is the notion that you can use a different model to update information than the model you use to read information. 
# For some situations, this separation can be valuable, but beware that for most systems CQRS adds risky complexity.

# The change that CQRS introduces is to split that conceptual model into separate models for update and display, 
# which it refers to as Command and Query respectively following the vocabulary of CommandQuerySeparation.

# CQRS fits well with event-based programming models. It's common to see CQRS system split into separate services communicating with Event Collaboration.
# This allows these services to easily take advantage of Event Sourcing.

# The other main benefit is in handling high performance applications. CQRS allows you to separate the load from reads and writes allowing you to scale each independently. 
# If your application sees a big disparity between reads and writes this is very handy. Even without that, you can apply different optimization strategies to the two sides. 
# An example of this is using different database access techniques for read and update.
