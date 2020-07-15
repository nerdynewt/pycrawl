<?php
$servername = "localhost";
$username = "vishnu";
$password = "CrapWeasel";
$dbname = "search_index";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$queries = array();
parse_str($_SERVER['QUERY_STRING'], $queries);
$sql = "SELECT url, title FROM search_index where content like '%$queries[q]%'";
$result = $conn->query($sql);
echo $queries['q'];
if (!empty($result) && $result->num_rows > 0) {
// if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo '<li><a href="'. $row["url"].'">'.$row["title"]."</a></li>\n";
  }
} else {
  echo "0 results";
}
$conn->close();
?>
