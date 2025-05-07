from app import app, db, Post, User
from datetime import datetime
import random

def create_sample_posts():
    with app.app_context():
        # Get or create admin user
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', password='admin123')
            db.session.add(admin)
            db.session.commit()

        sample_posts = [
            {
                'title': 'Getting Started with Flask',
                'content': '''Flask is a lightweight web framework for Python that's perfect for building web applications. In this guide, we'll explore the basics of Flask and how to create your first application.

Key Features:
- Simple and flexible
- Built-in development server
- Extensive documentation
- Large community support

To get started, you'll need to:
1. Install Flask using pip
2. Create a basic application structure
3. Run your first Flask application

Stay tuned for more advanced topics!''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Understanding Python Decorators',
                'content': '''Decorators are a powerful feature in Python that allows you to modify the behavior of functions or classes. In this article, we'll dive deep into how decorators work and their practical applications.

Common Use Cases:
- Logging
- Timing functions
- Access control
- Caching

Example:
```python
@timer
def my_function():
    pass
```''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Database Design Best Practices',
                'content': '''Designing a good database is crucial for application performance and maintainability. Here are some best practices to follow:

1. Normalization
2. Proper indexing
3. Relationship management
4. Data integrity
5. Performance optimization

Remember: A well-designed database is the foundation of a scalable application.''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Web Security Essentials',
                'content': '''Security should be a top priority in web development. Here are essential security practices:

1. Input validation
2. SQL injection prevention
3. XSS protection
4. CSRF tokens
5. Secure password handling

Always stay updated with the latest security practices!''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'REST API Design Principles',
                'content': '''REST APIs are the backbone of modern web applications. Here's how to design them effectively:

Key Principles:
- Use proper HTTP methods
- Implement versioning
- Handle errors gracefully
- Use appropriate status codes
- Implement pagination

Best practices for API documentation and testing will be covered in the next post.''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Frontend Development Trends 2024',
                'content': '''The frontend landscape is constantly evolving. Here are the latest trends:

1. Component-based architecture
2. Server-side rendering
3. Progressive Web Apps
4. Micro-frontends
5. State management solutions

Stay ahead of the curve by following these trends!''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Docker for Developers',
                'content': '''Docker has revolutionized how we develop and deploy applications. Learn the basics:

1. Containerization concepts
2. Dockerfile creation
3. Docker Compose
4. Best practices
5. Common pitfalls to avoid

Docker makes development environments consistent and deployment easier.''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Testing Strategies in Python',
                'content': '''Testing is crucial for maintaining code quality. Here's a comprehensive guide:

Types of Tests:
- Unit tests
- Integration tests
- End-to-end tests
- Performance tests

Tools:
- pytest
- unittest
- coverage.py
- selenium''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Git Workflow Best Practices',
                'content': '''Effective Git usage is essential for team collaboration. Here's how to do it right:

1. Branch naming conventions
2. Commit message standards
3. Code review process
4. Merge strategies
5. Conflict resolution

A good Git workflow improves team productivity.''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Performance Optimization Tips',
                'content': '''Optimizing application performance is crucial for user experience. Here are key tips:

1. Database query optimization
2. Caching strategies
3. Asset optimization
4. Code profiling
5. Load testing

Remember: Performance is a feature!''',
                'status': 'published',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Microservices Architecture',
                'content': '''Microservices are changing how we build applications. Learn about:

1. Service boundaries
2. Communication patterns
3. Data management
4. Deployment strategies
5. Monitoring and logging

Microservices offer scalability and flexibility.''',
                'status': 'draft',
                'created_at': datetime.now(),
                'user_id': admin.id
            },
            {
                'title': 'Cloud Computing Basics',
                'content': '''Understanding cloud computing is essential for modern development:

1. IaaS vs PaaS vs SaaS
2. Cloud providers comparison
3. Cost optimization
4. Security considerations
5. Migration strategies

The cloud offers flexibility and scalability.''',
                'status': 'draft',
                'created_at': datetime.now(),
                'user_id': admin.id
            }
        ]

        # Clear existing posts
        Post.query.delete()
        
        # Add new sample posts
        for post_data in sample_posts:
            post = Post(**post_data)
            db.session.add(post)
        
        # Commit changes
        db.session.commit()
        print(f"Added {len(sample_posts)} sample posts to the database!")

if __name__ == '__main__':
    create_sample_posts() 