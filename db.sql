-- Crear la base de datos
CREATE DATABASE flask_jwt_flutter;
USE flask_jwt_flutter;

-- Crear tabla para los usuarios
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Crear tabla para los nutricionistas
CREATE TABLE nutritionists (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    description TEXT,
    rating DECIMAL(3, 1) NOT NULL DEFAULT 1.0,
    photo VARCHAR(255),
    instagram VARCHAR(20),
    website VARCHAR(100),
    whatsapp VARCHAR(15),
    skill1 VARCHAR(50) NOT NULL,
    skill2 VARCHAR(50),
    skill3 VARCHAR(50)
);

-- Crear tabla para los comentarios
CREATE TABLE comments (
    id CHAR(36) PRIMARY KEY,
    content TEXT NOT NULL,
    photo VARCHAR(255),
    timestamp DATETIME NOT NULL,
    user_id CHAR(36),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Crear tabla para los tips profesionales
CREATE TABLE professional_tips (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    nutritionist_id CHAR(36),
    FOREIGN KEY (nutritionist_id) REFERENCES nutritionists(id)
);

-- Insertar datos en la tabla users
INSERT INTO users (id, name, username, password) VALUES 
(UUID(), 'Yassed Matta', 'yasmat', 'password'),
(UUID(), 'Juan', 'juano', 'password'),
(UUID(), 'kilo', 'kilombo', 'password'),
(UUID(), 'Tina', 'valplata', 'password'),
(UUID(), 'foodie101', 'Chef Coco', 'password'),
(UUID(), 'wanderlust', 'Aventurero', 'password'),
(UUID(), 'petlover', 'Amante', 'password'),
(UUID(), 'fitlife', 'EntuFitness', 'password');

-- Insertar datos en la tabla nutritionists
INSERT INTO nutritionists (id, name, username, email, password, description, rating, photo, instagram, website, whatsapp, skill1, skill2, skill3) VALUES 
(UUID(), 'Dr. Marlon José', 'melojose', 'melo.jose@example.com', 'password', 'Nutritionist specialized in personalized diets to improve health and physical performance.', 4.5, 'assets/imgs/dr_1.jpg', 'melojose_nutri', 'www.melojose.com', '+573045360092', 'Diet planning', NULL, NULL),
(UUID(), 'Dr. Matta', 'dr_matta_nutri', 'matta@example.com', 'password', 'Expert in sports nutrition and weight loss. I help my patients achieve their goals.', 4.8, 'assets/imgs/dr_2.jpg', 'dr_matta_nutri', 'www.drmatta.com', '+573045364492', 'Sports nutrition', 'Weight loss', NULL),
(UUID(), 'Dr. Smith', 'drasmith_nutri', 'dr.smith@example.com', 'password', 'Child specialist. I help parents provide healthy nutrition for their children.', 4.2, 'assets/imgs/dr_3.jpg', 'drasmith_nutri', 'www.drasmithnutrition.com', '+573045376890', 'Child nutrition', NULL, NULL),
(UUID(), 'Dra. García', 'licgarcia', 'dra.garcia@example.com', 'password', 'Dietitian expert in weight control and improvement of eating habits. Together we will achieve your goals!', 4.6, 'assets/imgs/dr_4.jpg', NULL, 'www.licgarcia.com', NULL, 'Weight control', 'Diet planning', 'Eating habits');

-- Insertar datos en la tabla comments
INSERT INTO comments (id, content, photo, timestamp, user_id) VALUES 
(UUID(), 'I discovered a new recipe today. Roast chicken with fresh herbs! So delicious and easy to make.', 'assets/imgs/post_1.jpg', '2024-02-02 12:00:00', (SELECT id FROM users WHERE username = 'Chef Coco')),
(UUID(), 'Had a great workout session today. Feeling strong!', NULL, '2024-02-03 08:00:00', (SELECT id FROM users WHERE username = 'yasmat')),
(UUID(), 'Tried a new smoothie recipe, so refreshing!', NULL, '2024-02-03 09:00:00', (SELECT id FROM users WHERE username = 'juano')),
(UUID(), 'Exploring new hiking trails this weekend!', NULL, '2024-02-03 10:00:00', (SELECT id FROM users WHERE username = 'kilombo')),
(UUID(), 'Meal prepped for the week. Healthy eating on track!', NULL, '2024-02-03 11:00:00', (SELECT id FROM users WHERE username = 'valplata')),
(UUID(), 'Just got a new cookbook. Excited to try new recipes!', NULL, '2024-02-03 12:00:00', (SELECT id FROM users WHERE username = 'Aventurero')),
(UUID(), 'My cat loved the new pet food I bought!', NULL, '2024-02-03 13:00:00', (SELECT id FROM users WHERE username = 'Amante')),
(UUID(), 'Crushed my fitness goals for the month!', NULL, '2024-02-03 14:00:00', (SELECT id FROM users WHERE username = 'EntuFitness'));

-- Insertar datos en la tabla professional_tips
INSERT INTO professional_tips (id, title, content, nutritionist_id) VALUES 
(UUID(), 'Consume Omega-3', 'Incorporate foods rich in omega-3 fatty acids, such as salmon, chia, and nuts. These are beneficial for cardiovascular and brain health.', (SELECT id FROM nutritionists WHERE email = 'melo.jose@example.com')),
(UUID(), 'Maintain Optimal Hydration', 'Drink enough water throughout the day. Adequate hydration is essential for optimal body functioning and can aid in weight loss.', (SELECT id FROM nutritionists WHERE email = 'matta@example.com')),
(UUID(), 'Include Variety in Your Diet', 'Make sure to include a wide variety of foods in your daily diet. This ensures obtaining different essential nutrients for the body.', (SELECT id FROM nutritionists WHERE email = 'melo.jose@example.com')),
(UUID(), 'Control Portions', 'Maintain proper portion control to avoid excess calories. Use smaller plates and pay attention to hunger and satiety signals.', (SELECT id FROM nutritionists WHERE email = 'dr.smith@example.com')),
(UUID(), 'Cook at Home', 'Prepare your meals at home whenever possible. This allows you to have greater control over the ingredients and the quality of your diet.', (SELECT id FROM nutritionists WHERE email = 'dra.garcia@example.com'));
