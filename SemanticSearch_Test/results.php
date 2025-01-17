<?php
// Access the search query from the URL
if (isset($_GET['query'])) {
    $searchQuery = $_GET['query'];

    $safeQuery = escapeshellarg($searchQuery);

    $output = shell_exec("python3 ./search.py $safeQuery");

}
?>
<html>

    <head>
    <style>

        body {
            font-family: Arial, sans-serif;
            background-color: #607D8B; /* Dark blue-gray background */
        }
    </style>



    </head>

    <title>Results</title>

    <body>


        <h1>Search Results for: <?php echo $searchQuery; ?></h1>

        <div>
            <h2>Python Script Output:</h2>
            <pre><?php echo htmlspecialchars($output); ?></pre>
        </div>


    </body>


</html>