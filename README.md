# Social Media Backend API

This is a RESTful backend API for a basic social media application built using **FastAPI** and **PostgreSQL**. It includes core features such as user authentication, post creation, and voting functionality.

## Features

- **User Authentication**
  - Register new users
  - Login with JWT authentication

- **Post Management**
  - Create new posts
  - View all posts
  - View individual posts
  - Update own posts
  - Delete own posts

- **Voting System**
  - Vote (like) on posts
  - Prevent duplicate votes by the same user

## Tech Stack

- **FastAPI** - Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database interaction
- **Pydantic** - Data validation
- **Passlib** - Password hashing
- **JWT (JSON Web Tokens)** - Authentication
- **Alembic** - Database migrations 

## API Endpoints Overview

### Authentication

- `POST /users/` - Register a new user
- `POST /login` - Login and receive an access token

### Users

- `GET /users/{id}` - Get user details by ID

### Posts

- `POST /posts/` - Create a post
- `GET /posts/` - View all posts
- `GET /posts/{id}` - View a single post
- `PUT /posts/{id}` - Update a post (must be the owner)
- `DELETE /posts/{id}` - Delete a post (must be the owner)

### Voting

- `POST /vote/` - Vote or unvote a post

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://https://github.com/Luytheti/SocialMedia_Backend.git
cd SocialMedia_Backend
