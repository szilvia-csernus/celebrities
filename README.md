# Celebrities Project

## Overview

The Celebrities project is a MongoDB-based application designed to manage a collection of celebrity records. It provides functionality for performing CRUD (Create, Read, Update, Delete) operations on the "celebrities" collection in a MongoDB database.
Created as part of Code Institute's Full-Stack Developer program.

## Tech Stack

- **Backend**: Python
- **Database**: MongoDB
- **Library**: PyMongo

## Main Features

- **Insert Records**: Add single or multiple celebrity records to the database
- **Retrieve Records**: Fetch and display records by name
- **Update Records**: Edit existing celebrity records
- **Delete Records**: Remove records from the database
- **Interactive Menu**: Provides a user-friendly menu for managing the collection

## Architecture

- **Database-Centric**: Focused on managing data in the "celebrities" collection
- **Modular Design**: Functions for each CRUD operation are encapsulated for reusability

## Data and Storage

- **Database**: MongoDB
- **Collection**: "celebrities" in the "myFirstDB" database
- **Data Structure**: JSON-like documents for storing celebrity details

## APIs

- **PyMongo**: Used for database connectivity and operations

## Security

- **Database Connection**: Manages connections securely using PyMongo
- **Data Validation**: Assumes basic validation for CRUD operations (details not provided)

## Testing

- **Manual Testing**: Validates CRUD operations through the interactive menu

## Deployment

- **Local Deployment**: Can be run locally with a MongoDB instance
- **Prerequisites**: Requires Python, PyMongo, and MongoDB setup

## Project Scale

- **Target Audience**: Developers learning MongoDB and database-driven application development
- **Scalability**: Suitable for small-scale database management applications
- **Cost Efficiency**: Minimal infrastructure requirements; runs on a local MongoDB instance
