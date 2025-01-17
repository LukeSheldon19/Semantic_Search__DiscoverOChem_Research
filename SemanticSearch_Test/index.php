<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Semantic Search</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #607D8B; /* Dark blue-gray background */
        }

        .search-container {
            position: relative;
            width: 500px;
        }

        .search-bar {
            width: 100%;
            padding: 15px 50px;
            border-radius: 30px;
            border: none;
            font-size: 18px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
            outline: none;
        }

        .search-bar::placeholder {
            color: #aaa;
        }

        .search-icon, .mic-icon {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 20px;
            height: 20px;
            cursor: pointer;
        }

        .search-icon {
            left: 20px;
        }

        .mic-icon {
            right: 20px;
        }

        .search-button {
            display: none; /* Hidden, as you only need the icons */
        }
    </style>
</head>
<body>

<div class="search-container">
    <form action="results.php" method="get">
        <input type="text" name="query" class="search-bar" placeholder="Search">
    </form>
</div>

</body>
</html>
