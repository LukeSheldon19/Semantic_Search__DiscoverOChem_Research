<?php
// Initialize variables
$searchQuery = isset($_GET['query']) ? trim($_GET['query']) : null;
$output = "";

if ($searchQuery) {
    // Sanitize the search query
    $safeQuery = escapeshellarg($searchQuery);

    // Execute the Python script and capture the output
    $output = shell_exec("python3 ./search.py $safeQuery 2>&1");

    if ($output === null || $output === "") {
        $output = "Error: Failed to execute the Python script or no output received.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Semantic Search</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #607D8B; /* Dark blue-gray background */
            color: #FFFFFF;
        }

        .search-container {
            position: relative;
            width: 500px;
            margin-bottom: 20px;
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

        .results-container {
            width: 90%;
            max-width: 800px;
            background-color: #455A64;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }

        .results-container h2 {
            color: #FFEB3B;
            margin-bottom: 10px;
        }

        pre {
            background-color: #37474F;
            color: #FFFFFF;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

<div class="search-container">
    <form method="get" action="">
        <input type="text" name="query" class="search-bar" placeholder="Search" value="<?php echo htmlspecialchars($searchQuery); ?>">
    </form>
</div>

<?php if ($searchQuery): ?>
    <div class="results-container">
        <h2>Search Results for: <?php echo htmlspecialchars($searchQuery); ?></h2>
        <pre><?php echo htmlspecialchars($output); ?></pre>
    </div>
<?php endif; ?>

</body>
</html>
