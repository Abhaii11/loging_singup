INSERT INTO users (first_name, last_name, username, email, password, user_type)
VALUES ('John', 'Doe', 'johndoe', 'john@example.com', 'hashed_password', 'Doctor');

INSERT INTO blogs (title, image, category, summary, content, is_draft, author_id)
VALUES ('Mental Health Tips', 'mental.jpg', 'Mental Health', 'Tips for managing stress...', 'Full content here...', FALSE, 1);
