# Project Overview

A brief description of the project, its purpose, and key features.

## Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    ```

2. **Set Up the Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Database**
    - Update PostgreSQL settings in `settings.py`.

5. **Run Migrations**
    ```bash
    python manage.py migrate
    ```

6. **Run the Server**
    ```bash
    python manage.py runserver
    ```

## API Documentation

- **Available Queries and Mutations**: 

**Query: Get All Posts**
```graphql
query {
    allPosts {
        id
        title
        content
        createdAt
        likes {
            id
            user {
                username
            }
        }
        shares {
            id
            user {
                username
            }
        }
    }
}
```

**Query: Get All Users**
```graphql
query {
    allUsers {
        id
        username
        email
        bio
    }
}
```

**Query: Get All Comments**
```graphql
query {
    allComments {
        id
        text
        createdAt
        user {
            username
        }
        post {
            title
        }
    }
}
```

**Query: Get All Likes**
```graphql
query {
    allLikes {
        id
        createdAt
        user {
            username
        }
        post {
            title
        }
    }
}
```

**Query: Get All Shares**
```graphql
query {
    allShares {
        id
        sharedAt
        user {
            username
        }
        post {
            title
        }
    }
}
```

**Mutation: Create Post**
```graphql
mutation {
    createPost(title: "GraphQL Post", content: "Demo content for GraphQL post") {
        post {
            id
            title
        }
    }
}
```

**Mutation: Create User**
```graphql
mutation {
    createUser(username: "demoUser", password: "password", email: "demo@example.com", bio: "Hello world!") {
        user {
            id
            username
            email
        }
    }
}
```

**Mutation: Create Comment**
```graphql
mutation {
    createComment(userId: 1, postId: 1, text: "This is a comment") {
        comment {
            id
            text
        }
    }
}
```

**Mutation: Create Like**
```graphql
mutation {
    createLike(userId: 1, postId: 1) {
        like {
            id
            createdAt
        }
    }
}
```

**Mutation: Create Share**
```graphql
mutation {
    createShare(userId: 1, postId: 1) {
        share {
            id
            sharedAt
        }
    }
}
```
- **GraphQL Playground**: [Link to demo](#)